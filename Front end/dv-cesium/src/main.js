import { createApp } from 'vue'
import "element-plus/dist/index.css"
import Element from "element-plus";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import './style.css'
import App from './App.vue'
import router from './router'

const htmlLayerParam = {
    1: {
        "layer": "TileLayer",
    },
    2: {
        "jsonPath": "/jsonData/anyi_qyfb.json",
        "class_name": "public-map-popup qyfb-box",
        "img_src": "./img/mapicon/qy.png",
        "layer": "qyfb",
    },
    4: {
        "layer": "yqfw",
        "jsonPath": "/jsonData/anyi_yqfw.json",
        "alt": 100
    },
    5: {
        "jsonPath": "/jsonData/anyi_kzqj.json",
        "class_name": "public-map-popup",
        "img_src": "./img/mapicon/qj.png",
        "layer": "kzqj",
    },
    6: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup yjc-box",
        "img_src": "./img/mapicon/yjc.png",
        "layer": "yjc-yq",
    },
    7: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup yjc-box",
        "img_src": "./img/mapicon/yjc.png",
        "layer": "ysc-yq",
    },
    8: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup ysf-box",
        "img_src": "./img/mapicon/ysf.png",
        "layer": "chz-yq",
    },
    9: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/kt.png",
        "layer": "kt-yq",
        "vLayer": "vkt-yq",
    },
    10: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/zb.png",
        "layer": "zb-yq",
    },
    11: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/gouqu.png",
        "layer": "gouqu-yq",
        "vLayer": "vgouqu-yq"
    },
    12: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/sk.png",
        "layer": "sk-yq",
        "vLayer": "vsk-yq",
    },
    13: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/ql.png",
        "layer": "ql-yq",
    },
    17: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/sd.png",
        "layer": "sd-yq",
    },
    18: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "layer": "sg-yq",
    },
    19: {
        "jsonPath": "/jsonData/anyi_whlx.json",
        "color": "#ff8000",
        "width": 5,
        "layer": "whlx-yq",
    },
    20: {
        "jsonPath": "/jsonData/anyi_hl.json",
        "color": "#0033ff",
        "width": 3,
        "layer": "hl-yq",
    },
    21: {
        "jsonPath": "/jsonData/anyi_yjwzqj.json",
        "class_name": "public-map-popup qyfb-box",
        "img_src": "./img/mapicon/yjwz.png"
    },
    15: {
        "jsonPath": "/jsonData/anyi_rs.json",
        "layer": "rs-yb",
        "class_name": "public-map-popup fxy-ordinary",
        "img_src": "./img/mapicon/fxy-yb.png",
        "type": "一般",
    },
    16: {
        "jsonPath": "/jsonData/anyi_rs.json",
        "layer": "rs-jd",
        "class_name": "public-map-popup fxy-larger-b",
        "img_src": "./img/mapicon/fxy-zd-b.png",
        "type": "较大",
    },
}

const sjfkLayerName = {
    "1": ["djfk1", "djfkv1"],
    "2": ["djfk2", "djfkv2"],
    "3": ["djfk3", "djfkv3"],
    "4": ["djfk4", "djfkv4"]
}

const staticData = {
    "title": "安义化工园区“一园一策一图”VR平台",
    "tilePath": [
        // "/gouqu_3dtiles/tileset.json",
        "/3dtiles/1/tileset.json",
        "/3dtiles/2/tileset.json",
        "/3dtiles/3/tileset.json",
        "/3dtiles/4/tileset.json",
        "/3dtiles/5/tileset.json",
        "/3dtiles/6/tileset.json",

    ],
    // "tilePath": "http://182.109.88.42:10010/xinganTileset/tileset.json",
    "tdtKey": "8899fd3e86aa994f71465b1c56a98727",
    // "zoomPosition": [115.4674, 27.81283, 7000, 360, -45],
    "zoomPosition": [115.6493, 28.79954, 7000, 360, -45],
    "terrainPath": "https://data.mars3d.cn/terrain",
    'api': "./api",
    "yjkjJson": "/jsonData/anyi_yjkj.json",
    "htmlLayerParam": htmlLayerParam,
    "sjfkLayerName": sjfkLayerName,
    "yjwzJson": "/jsonData/anyi_yjwz.json",
    "jydwJson":{
        "园区救援队伍": "/jsonData/anyi_yqjy.json",
        "企业救援队伍": "/jsonData/anyi_qyjy.json",
    },
    "qjmn": {
        1: "/jsonData/anyi_qjmn1.json",
        2: "/jsonData/anyi_qjmn2.json",
        3: "/jsonData/anyi_qjmn3.json",
        4: "/jsonData/anyi_qjmn4.json",
    }
}

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.use(Element)
app.use(router)
app.provide('staticData', staticData)
app.mount("#app")
