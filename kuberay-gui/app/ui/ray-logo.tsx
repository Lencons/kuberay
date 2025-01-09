import Image from 'next/image';
import { Roboto } from 'next/font/google';

// Font that is reasonably close to the Ray project font.
const roboto = Roboto({ weight: '400' });

export default function RayLogo() {
    return (
        <div
            className={`${roboto.className} flex flex-row items-center leading-none text-white`}
        >
        <Image
            className="h-14 w-14"
            src="/ray-logo.png"
            width="96"
            height="96"
            alt="Ray Project logo"
        />
        <p className="text-[36px]">KubeRay</p>
      </div>
    );
}