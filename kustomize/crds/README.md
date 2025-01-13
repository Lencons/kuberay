# KubeRay Customer Resource Definitions

The CRD's for KubeRay are defined as their own Fleet Bundle so the Operator can be made dependent on it. Otherwise, at least of first deployment, the Kustomize configuration will fail because the Deployments cannot fine the CRD's.
