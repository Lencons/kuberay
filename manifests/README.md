# Kubernetes Configuration Manifests

This is a collection of YAML manifests for the deployment of RayKube services and resources. Details on the specific capability of each manifest is documented within the header comments of each YAML file.

## Manifests Templates

Template manifests provide the basics for the creation of resources and include operational notes and information in relation to the configuration attributes.

## Testing Manifests

Manifests identified as `test` define minimal resources for the basic testing of capability and will generally not be significant enough to be used for any useful processing.

Testing is assumed to be performed on a single node Kubernetes instance and the manifest assume that NodePort is used to expose services. The expected Kubernetes instance for testing provides a least 16 CPU's and 24GB memory.
