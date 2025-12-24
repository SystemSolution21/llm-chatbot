// Include Vite client types to support import.meta.env and other Vite features
/// <reference types="vite/client" />

// Define the structure of environment variables used in the application
interface ImportMetaEnv {
    readonly VITE_API_URL: string;
}

// Extend the global ImportMeta interface to include specific environment variables
interface ImportMeta {
    readonly env: ImportMetaEnv;
}

// Declare modules for CSS and SCSS files to allow importing them in TypeScript
declare module "*.module.css";
declare module "*.module.scss";
