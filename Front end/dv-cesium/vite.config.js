import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import DC from '@dvgis/vite-plugin-dc'

// https://vite.dev/config/
export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8080/zhyq",
        changeOrigin: true,
        rewrite:(path) => path.replace(/^\/api/, "/api")
      },
    },
  },
  plugins: [vue(), DC()],
  base: "./",
  build:{
    rollupOptions:{
      output:{
        manualChunks(id) {
          if (id.includes('node_modules/@dvgis')) {
            return 'dvgis';
          }
          else if (id.includes('node_modules/@cesium')) {
            return 'cesium';
          }
          else if (id.includes('node_modules/element-plus')) {
            return 'element-plus';
          }
        }
      }
    }
  }
})
