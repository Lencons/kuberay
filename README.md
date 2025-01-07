# Ray Project

The Ray Project provides a distributed computing system.

* Project Documentation: https://docs.ray.io/en/latest/index.html

## KubeRay

KubeRay is a open-source Kubernetes operator that manages Ray applications on Kubernetes. It offers several key components:

* *KubeRay core*: This is the official, fully-maintained component of KubeRay that provides three custom resource definitions, RayCluster, RayJob, and RayService. These resources are designed to run a wide range of computational workloads.
* *RayCluster*: KubeRay completely manages the lifecycle of RayCluster, including cluster creation/deletion, autoscaling, and ensuring fault tolerance.
* *RayJob*: With RayJob, KubeRay automatically creates a RayCluster and submits a job when the cluster is ready. RayJob can also be configured automatically delete the RayCluster once the job finishes.
* *RayService*: RayService is made up of two parts: a RayCluster and a Ray Serve deployment graph. RayService offers zero-downtime upgrades for RayCluster and high availability.

The KubeRay community also manage some key components useful with operating KubeRay:

* *KubeRay APIServer*: It provides a layer of simplified configuration for KubeRay resources. The KubeRay API server can be used to back user interfaces for KubeRay resource management by internal tooling.
* *KubeRay Python client*: This Python client library provides APIs to handle RayCluster from your Python application.

* GitHub: https://github.com/ray-project/kuberay

### KubeRay Helm Charts

The KubeRay project provide an official repository of Helm charts to support the deployment of KubeRay resources into Kubernetes.

The Help repository is located at https://ray-project.github.io/kuberay-helm/ and can generally be added to most Kubernetes instances through the platforms Application/Help UI, or can be deployed by the host CLI:

```bash
# Add the Helm repo
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
```

The minimum resources required for a Kubernetes instance is the KubeRay Operator which provides the top level management of all KubeRay resources. With the KubeRay Operator installed, the creation of clusters, jobs or other assets can be managed through project or locally customised Helm charts, direct manifests or other custom management utilities.

```bash
# Install both CRDs and KubeRay operator v1.1.0.
helm install kuberay-operator kuberay/kuberay-operator --version 1.1.0
```
