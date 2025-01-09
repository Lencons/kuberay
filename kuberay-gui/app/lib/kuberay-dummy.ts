/**
 * Dummy Data Functions for KubeRay Interface.
 * 
 * Data to be used for application testing and development when access to
 * a operaional KubeRay cluster is not available. Replaces each of the API
 * functions within kuberay.ts with functions that do not connect to a
 * remote KubeRay cluster.
 */

import { RayCluster } from './kuberay';

// List of clusters across several namespaces.
export const CLUSTERS: RayCluster[] = [
  {
    name: 'default cluster 1',
    namespace: 'default',
    user: 'kuberay',
    version: '2.2.40',
  },
  {
    name: 'default cluster 2',
    namespace: 'default',
    user: 'kuberay',
    version: '2.2.40',
  },
  {
    name: 'default cluster 3',
    namespace: 'default',
    user: 'kuberay',
    version: '2.2.40',
  },
  {
    name: 'default cluster 1',
    namespace: 'kuberay',
    user: 'kuberay',
    version: '2.2.40',
  },
  {
    name: 'default cluster 2',
    namespace: 'kuberay',
    user: 'kuberay',
    version: '2.2.40',
  },
  {
    name: 'default cluster 3',
    namespace: 'kuberay',
    user: 'kuberay',
    version: '2.2.40',
  },
];

/**
 * Cluster API dummy functions. 
 */

export function fetchRayClusters(): Array<RayCluster> {
  return CLUSTERS;
}

export function fetchRayClustersNamespaceDummy(
  namespace: string,
): Array<RayCluster> {
  return CLUSTERS.filter(cluster => cluster.namespace === namespace);
}

export function fetchRayCluster(
  namespace: string,
  name: string,
): RayCluster | undefined {
  const cluster: RayCluster[] =
    CLUSTERS
      .filter(cluster => cluster.namespace === namespace)
      .filter(cluster => cluster.name === name);

  return cluster.length ? cluster[0] : undefined;
}