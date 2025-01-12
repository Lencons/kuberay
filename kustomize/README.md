# KubeRay Operator Deployment

This Kustomize configuration deploys the KubeRay Operator and API Server services into an environment. The Helm charts that are provided by the Ray project have some limitations with them when deploying them directly from the project repository. This is primarly around running the API Server without authentication and configuring the server to use an Ingress frontend for the REST API. These issues are not necessarly an issue with the project provided Helm charts, but more around the expectation on how they would be deployed into a production environment.
