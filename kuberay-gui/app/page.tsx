'use client';

import { redirect, useSearchParams } from 'next/navigation';

import RayLogo from '@/app/ui/ray-logo';
import { inter } from '@/app/ui/fonts';
import LoginForm from '@/app/ui/login-form';

export default function Page() {

  // If we have a username set, redirect to the dashboard.
  const searchParams = useSearchParams();
  const username = searchParams.get('username') ?? '';
  if (username !== '') redirect('/dashboard');

  return (
    <main className="flex min-h-screen flex-col p-6">
      <div className="flex h-20 shrink-0 items-end rounded-lg bg-blue-500 p-4 md:h-42">
        <RayLogo />
      </div>
      <div className="mt-4 flex grow flex-col gap-4 md:flex-row">
        <div className="flex flex-col justify-center gap-6 rounded-lg bg-gray-50 px-6 py-10 md:w-2/5 md:px-20">
          <p className={`${inter.className} text-l text-gray-800 md:text-2xl md:leading-normal`}>
            This is a simple example of a portal for the provisioning and
            management of compute clusters using the KubeRay API service.
          </p>
        </div>
        <div className="flex items-center justify-center p-6 md:w-3/5 md:px-8 md:py-12">
          <LoginForm />
        </div>
      </div>
    </main>
  );
}
