from typing import Tuple

import ray
from ray.data import Dataset, Preprocessor
from ray.data.preprocessors import StandardScaler
from ray.train.xgboost import XGBoostTrainer
from ray.train import Result, ScalingConfig, Checkpoint
import xgboost
import pandas as pd


class Predict:

    def __init__(self, checkpoint: Checkpoint):
        self.model = XGBoostTrainer.get_model(checkpoint)
        self.preprocessor = Preprocessor.deserialize(checkpoint.get_metadata()["preprocessor_pkl"])

    def __call__(self, batch: pd.DataFrame) -> pd.DataFrame:
        preprocessed_batch = self.preprocessor.transform_batch(batch)
        dmatrix = xgboost.DMatrix(preprocessed_batch)

        return {"predictions": self.model.predict(dmatrix)}


def train_xgboost(
    train_dataset: Dataset,
    valid_dataset: Dataset,
    num_workers: int = 1,
    use_gpu: bool = False,
) -> Result:
    """Train a XGBoost Trainer with the provided datasets.
    
    Parameters
    ----------
    train_dataset
        Dataset of training data.
    valid_dataset
        Dataset of validation data.
    num_workers
        Number of Ray workers to create for training. (default: 1)
    use_gpu
        Flag to enable GPU processing support. (default: False)

    Returns
    -------
    Result
        Training result.
    """

    # Scale some random columns
    columns_to_scale = ["mean radius", "mean texture"]
    preprocessor = StandardScaler(columns=columns_to_scale)
    train_dataset = preprocessor.fit_transform(train_dataset)
    valid_dataset = preprocessor.transform(valid_dataset)

    # XGBoost specific params
    params = {
        "tree_method": "approx",
        "objective": "binary:logistic",
        "eval_metric": ["logloss", "error"],
    }

    trainer = XGBoostTrainer(
        scaling_config=ScalingConfig(num_workers=num_workers, use_gpu=use_gpu),
        label_column="target",
        params=params,
        datasets={"train": train_dataset, "valid": valid_dataset},
        num_boost_round=100,
        metadata = {"preprocessor_pkl": preprocessor.serialize()}
    )
    result = trainer.fit()
    return result


def predict_xgboost(
    result: Result,
    test_dataset: Dataset,
) -> Dataset:
    """Run a predition on a dataset.....
    
    Parameters
    ----------
    result

    """
    scores = test_dataset.map_batches(
        Predict, 
        fn_constructor_args=[result.checkpoint], 
        concurrency=1, 
        batch_format="pandas"
    )
    
    predicted_labels = scores.map_batches(lambda df: (df > 0.5).astype(int), batch_format="pandas")
    return predicted_labels


if __name__ == '__main__':

    # Get the Breast Cancer dataset and break it into the training subsets.
    dataset = ray.data.read_csv("data/breast_cancer.csv")
    train_dataset, valid_dataset = dataset.train_test_split(test_size=0.3)
    test_dataset = valid_dataset.drop_columns(["target"])


    result = train_xgboost(
        train_dataset,
        valid_dataset,
        num_workers=2,
        use_gpu=False,
    )
    print('DONE!!!')
#    print(result.metrics)

    labels = predict_xgboost(result, test_dataset)
    print(f"PREDICTED LABELS")
    labels.show()