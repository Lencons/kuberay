# KubeRay Operator Deployment

This Kustomize configuration deploys the KubeRay Operator and API Server services into an environment. The Helm charts that are provided by the Ray project have some limitations with them when deploying them directly from the project repository. This is primarly around running the API Server without authentication and configuring the server to use an Ingress frontend for the REST API. These issues are not necessarly an issue with the project provided Helm charts, but more around the expectation on how they would be deployed into a production environment.

## Operator Namespace

A Namespace is not created as part of this Kustomize configuration. This is to ensure that within Rancher the Namespace is created within the correct Project rather than being dumped in the "Not in a Project" bucket.

Before attempting to deploy, the Namespace `kuberay-operator` needs to exist within the cluster.

## CRD Deployment

Kustomize doen't support the ability to place dependancies between resources within the configuration. This would create the issue if the KubeRay CRD were included within the main Kustomization configuration that if the deployment of the resource was attempted before the definition was deployed by Kustomize then it the Kustomize deployment would fail. Run it a second time and it should be fine.

This Kustomization configuration is intended to work with Rancher and Fleet. Fleet provides the ability to define dependencies between Bundles and will scan the directory heirarchy for `fleet.yaml` Bundle configuration before deploying resources. This allows the CRD's to be contained within their own `crds/` directory as a Bundle and the root Bundle to be configured to be depended upon it.

```yaml
dependsOn:
  - selector:
    bindle: kuberay-crds
```

Fleet will then deploy the `kuberay-crds` Bundle first as a Kustomize deployment then deploy the root Bundle on `kuberay-crds` success.
