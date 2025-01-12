/**
 * API integration with KubeRay API server services.
 */
'use client';

import { useEffect } from 'react';

export type RayCluster = {
    name: string;
    namespace: string;
    user: string;
    version: string;
  };

const HEADERS = { headers: { accept: 'application/json'}};


export function fetchRayClusters(
  kuberay_api: string,
): Array<RayCluster> {

  const url = kuberay_api + '/apis/v1/clusters';
  console.log(`URL: ${url}`);

  useEffect(() => {
    fetch(url, {
      method: 'GET',
      headers: {
        'accept': 'application/json',
      }
    })
      .then((res) => res.json())
  }, []);

  let clusters: RayCluster[] = [];

  return clusters;
}


export function fetchRayClustersNamespace(
  kuberay_api: string,
  namespace: string,
): Array<RayCluster> {
  let clusters: RayCluster[] = [];

  const { data, error, isLoading } = useSWR('url', fetcher)

  if (error) console.log(error);


  return clusters;
}
