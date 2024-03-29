import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      '/solve': {
        target: 'http://localhost:5000/',
        changeOrigin: true,
      },
      '/hello': {
        target: 'http://localhost:5000/',
        changeOrigin: true,
      },
    }
  }
})
