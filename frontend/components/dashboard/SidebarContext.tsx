"use client";

import { useState, createContext, useContext } from "react";

export interface SidebarContextType {
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
  setSidebarOpen: (open: boolean) => void;
}

export const SidebarContext = createContext<SidebarContextType>({
  isSidebarOpen: true,
  toggleSidebar: () => {},
  setSidebarOpen: () => {},
});

export const useSidebar = () => useContext(SidebarContext);

export function SidebarProvider({ children }: { children: React.ReactNode }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <SidebarContext.Provider
      value={{
        isSidebarOpen,
        toggleSidebar: () => setIsSidebarOpen((prev) => !prev),
        setSidebarOpen: setIsSidebarOpen,
      }}
    >
      {children}
    </SidebarContext.Provider>
  );
}
