import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index.js";
import '@dvgis/dc-sdk/dist/dc.min.css'

const app = createApp(App)
app.use(router)
app.mount("#app")
