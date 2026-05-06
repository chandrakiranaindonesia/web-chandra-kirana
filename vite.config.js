import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        tentang: resolve(__dirname, 'tentang-kami.html'),
        layanan: resolve(__dirname, 'layanan.html'),
        portofolio: resolve(__dirname, 'portofolio.html'),
        legalitas: resolve(__dirname, 'legalitas.html'),
        testimoni: resolve(__dirname, 'testimoni.html'),
        kontak: resolve(__dirname, 'kontak.html')
      }
    }
  }
});