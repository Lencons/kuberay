'use client';

import { redirect, useSearchParams } from 'next/navigation';
import Clusters from '@/app/ui/dashboard/clusters';
//import { fetchRayClustersNamespace } from '@/app/lib/kuberay';
import { fetchRayClustersNamespaceDummy } from '@/app/lib/kuberay-dummy';
import { inter } from '@/app/ui/fonts';

export default function Page () {

  // Get login details, redirect to home to login if missing.
  const searchParams = useSearchParams();
  const username = searchParams.get('username') ?? '';
  const kuberayURL = searchParams.get('kuberay_url') ?? '';
  if (username === '') redirect('/');

  const clusters = fetchRayClustersNamespaceDummy('default');
  console.log(clusters);
  
  return (
    <main>
      <h1 className={`${inter.className} mb-4 text-xl md:text-2xl`}>
        Dashboard
      </h1>
      <div className="mt-6 grid grid-cols-1">
        <Clusters clusters={clusters} />
      </div>
    </main>
  );
}
