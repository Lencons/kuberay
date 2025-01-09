import { ArrowPathIcon, ServerStackIcon } from '@heroicons/react/24/outline';
import clsx from 'clsx';
import Image from 'next/image';
import { inter } from '@/app/ui/fonts';
import { RayCluster } from '@/app/lib/kuberay';

export default function Clusters({
  clusters,
}: {
  clusters: RayCluster[];
}) {
  return (
    <div className="flex w-full flex-col md:col-span-4">
      <h2 className={`${inter.className} mb-4 text-lg md:text-xl`}>
        Active Clusters
      </h2>
      <div className="flex grow flex-col justify-between rounded-xl bg-gray-50 p-4">
        <div className="bg-white px-6">
          {clusters.map((cluster, i) => {
            return (
              <div
                key={cluster.name}
                className={clsx(
                  'flex flex-row items-center justify-between py-4',
                  {
                    'border-t': i !== 0,
                  },
                )}
              >
                <div className="flex items-center">
                  <ServerStackIcon
                    className="h-12 w-12 p-2 text-green-500"
                  />
                  <div className="min-w-0 px-2">
                    <p className="truncate text-sm font-semibold md:text-base">
                      {cluster.name}
                    </p>
                    <p className="hidden px-2 text-sm text-gray-500 sm:block">
                      {cluster.version}
                    </p>
                  </div>
                </div>
                <p
                  className={`${inter.className} truncate text-sm font-medium md:text-base`}
                >
                  {cluster.user}
                </p>
              </div>
            );
          })}
        </div>
        <div className="flex items-center pb-2 pt-6">
          <ArrowPathIcon className="h-5 w-5 text-gray-500" />
          <h3 className="ml-2 text-sm text-gray-500 ">Updated just now</h3>
        </div>
      </div>
    </div>
  );
}
