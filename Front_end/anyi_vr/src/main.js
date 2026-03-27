import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index.js";
import '@dvgis/dc-sdk/dist/dc.min.css'

// 在 main.js 中添加
import Schema from 'async-validator';

// 禁用 async-validator 的警告
Schema.warning = () => {};
const app = createApp(App)
app.use(router)
app.mount("#app")
