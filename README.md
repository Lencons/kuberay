# Ray Project

The Ray Project provides a distributed computing system supporting traditional HPC workloads as well a machine learning specific services.

* Project Documentation: https://docs.ray.io/en/latest/index.html

This project is used for test and validation activies within my Homelab and will generally be in a state of flux depending on what I am playing with. Don't expect complete or fully functional examples of anything.

The components provided are:

* **KubeRay Operator Kustomize Configuration** - This Kustomize configuration I use with Ranchr/Fleet to manage a RKE2 instance as a general testing and development environment. This configuraiton has been generated from the Ray Project Helm charts and modified to expose KubeRay services. For a trusted HomeLab environment, the KubeRay Helm charts didn't really work for what I needed and rather than re-work them I simplified it using Kustomize.
* **KubeRay Cluster Manifests** - Some YAML manifests to deploy various RayClusters into environments which I use.
* **KubeRay GUI** - A RayCluster management GUI that interacts with the KubeRay APIServer to give sort of a GPUaaS style portal interface. (NOTE - This is current work in progress as I sort out some KubeRay system issues in my environment)
* **Workloads** - A collection of Python scripts to kick of Ray jobs and demostrate processing within the RayCluster.

## Usage

The KubeRay Operator needs to be deployed into a Kubernetes instance which can be done either from the Ray Project KubeRay Helm charts or from the Kustomize configuration provided here. Last time I tried the APIServer didn't deploy in a usable manner from the Helm charts which is why I created the Kustomize configuration. If the APIServer isn't required, the Operator can be just deployed from the project Helm Charts.

Once the KubeRay Operator has been deployed, then a RayCluster needs to be created. This can be done via the Ray projects Helm charts or via the provided manifests. If workloads are to be initiated from the RayCluster head node, then no external services are required. But if a remote workstation is to be used, make sure RayCluster has its services exposed via NodePort or a LoadBalancer.

The RayCluster head node will expose a collection of services which will be available on the exposed services. You may need to use your Kubernetes skills to work though any port mappings or LoadBalancer allocations.

To run the test workloads on the RayCluster, check the README.md out within the `workloads` directory.

## Ray Project and KubeRay

KubeRay is a open-source Kubernetes operator that manages Ray applications on Kubernetes. It offers several key components:

* *KubeRay core*: This is the official, fully-maintained component of KubeRay that provides three custom resource definitions, RayCluster, RayJob, and RayService. These resources are designed to run a wide range of computational workloads.
* *RayCluster*: KubeRay completely manages the lifecycle of RayCluster, including cluster creation/deletion, autoscaling, and ensuring fault tolerance.
* *RayJob*: With RayJob, KubeRay automatically creates a RayCluster and submits a job when the cluster is ready. RayJob can also be configured automatically delete the RayCluster once the job finishes.
* *RayService*: RayService is made up of two parts: a RayCluster and a Ray Serve deployment graph. RayService offers zero-downtime upgrades for RayCluster and high availability.

The KubeRay community also manage some key components useful with operating KubeRay:

* *KubeRay APIServer*: It provides a layer of simplified configuration for KubeRay resources. The KubeRay API server can be used to back user interfaces for KubeRay resource management via internal tooling.
* *KubeRay Python client*: This Python client library provides APIs to handle RayCluster from Python applications.

* GitHub: https://github.com/ray-project/kuberay

### KubeRay Helm Charts

The KubeRay project provide an official repository of Helm charts to support the deployment of KubeRay resources into Kubernetes.

The Helm repository is located at https://ray-project.github.io/kuberay-helm/ and can generally be added to most Kubernetes instances through the platforms Application/Helm UI, or can be deployed by the host CLI:

```bash
# Add the Helm repo
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
```

The minimum resources required for a Kubernetes instance is the KubeRay Operator which provides the top level management of all KubeRay resources. With the KubeRay Operator installed, the creation of clusters, jobs or other assets can be managed through project or locally customised Helm charts, direct manifests or other custom management utilities.

```bash
# Install both CRDs and KubeRay operator v1.1.0.
helm install kuberay-operator kuberay/kuberay-operator --version 1.2.2
```
