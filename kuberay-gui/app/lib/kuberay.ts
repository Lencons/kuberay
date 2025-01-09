/**
 * API integration with KubeRay API server services.
 */
'use client';

import useSWR from 'swr';

export type RayCluster = {
    name: string;
    namespace: string;
    user: string;
    version: string;
  };

const fetcher = (arg: any, ...args: any) =>
        fetch(arg, ...args).then(res => res.json());

export function fetchRayClustersNamespace(
  namespace: string,
): Promise<Array<RayCluster>> {
  let clusters: RayCluster[] = [];
  const { data, error, isLoading } = useSWR('url', fetcher)

  if (error) console.log(error);


  return clusters;
}
