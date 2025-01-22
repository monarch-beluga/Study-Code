import { createApp } from 'vue'
import "element-plus/dist/index.css"
import Element from "element-plus";
import './style.css'
import App from './App.vue'

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
        "type": "1",
        "layer": "yjc-yq",
    },
    7: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup ysf-box",
        "img_src": "./img/mapicon/ysf.png",
        "type": "2",
        "layer": "fm-yq",
    },
    8: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/sk.png",
        "type": "5",
        "layer": "sk-yq",
    },
    9: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/kt.png",
        "layer": "kt-yq",
        "type": "6"
    },
    10: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/gouqu.png",
        "layer": "gq-yq",
        "type": "7"
    },
    11: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/ql.png",
        "layer": "ql-yq",
        "type": "8"
    },
    12: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xfs-box",
        "img_src": "./img/mapicon/sd.png",
        "layer": "sd-yq",
        "type": "9"
    },
    13: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup xsf-box",
        "img_src": "./img/mapicon/wd.png",
        "layer": "wd-yq",
        "type": "10"
    },
    14: {
        "jsonPath": "/jsonData/anyi_yjkj.json",
        "class_name": "public-map-popup sk-box",
        "img_src": "./img/mapicon/zb.png",
        "layer": "zb-yq",
        "type": "11"
    },
}

const sjfkLayerName = {
    "1": "一级防控",
    "2": "二级防控",
    "3": "三级防控",
}

const staticData = {
    "title": "安义化工园区“一园一策一图”VR平台",
    "tilePath": [
        "/3dtiles/1/tileset.json",
        "/3dtiles/2/tileset.json",
        "/3dtiles/3/tileset.json",
        "/3dtiles/4/tileset.json",
        "/3dtiles/5/tileset.json",
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
}

const app = createApp(App)
app.use(Element)
app.provide('staticData', staticData)
app.mount("#app")
