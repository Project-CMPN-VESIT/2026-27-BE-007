"use client";

import Sidebar from "@/components/dashboard/Sidebar";
import Header from "@/components/dashboard/Header";
import { SidebarProvider, useSidebar } from "@/components/dashboard/SidebarContext";

function DashboardLayoutContent({ children }: { children: React.ReactNode }) {
  const { isSidebarOpen } = useSidebar();

  return (
    <div className="flex flex-col h-screen bg-white text-slate-900 font-sans">
      <Header />
      <div className="flex-1 flex overflow-hidden">
        {isSidebarOpen && <Sidebar />}
        <main className="flex-1 overflow-auto bg-white">{children}</main>
      </div>
    </div>
  );
}

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <SidebarProvider>
      <DashboardLayoutContent>{children}</DashboardLayoutContent>
    </SidebarProvider>
  );
}
