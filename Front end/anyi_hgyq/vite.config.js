import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import DC from '@dvgis/dc-sdk'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), DC()],
})
