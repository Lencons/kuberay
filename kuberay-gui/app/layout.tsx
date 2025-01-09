import type { Metadata } from "next";
import "./globals.css";
import { inter } from "./ui/fonts";

export const metadata: Metadata = {
  title: "KubeRay Cluster Manager",
  description: "Simple client side GUI for managing RayClusters within Kubernetes.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${inter.className} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
