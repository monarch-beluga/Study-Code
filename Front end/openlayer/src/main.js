import "ol/ol.css";
import "layui/dist/css/layui.css"
import "./style.css";
import {Map, View} from "ol";
import TileLayer from "ol/layer/Tile.js";
import {XYZ} from "ol/source.js";
import VectorLayer from "ol/layer/Vector.js";
import VectorSource from "ol/source/Vector.js";
import {GeoJSON} from "ol/format.js";
import {Fill, Stroke, Style} from "ol/style.js";
import { Draw } from 'ol/interaction';
import {ScaleLine, defaults as defaultControls} from 'ol/control';
import "layui/dist/layui.js"

const staticData = {
    "center": [115.01998901367189, 28.324127197265625],
    "map": "./map.json",
    "tdtKey": "8899fd3e86aa994f71465b1c56a98727",
}

let key = staticData.tdtKey
const imageTileLayer = new TileLayer({
    source: new XYZ({
        minZoom: 10,
        url: "https://t0.tianditu.gov.cn/img_w/wmts?layer=img&style=default&tilematrixset=c&Service=WMTS&Request=GetTile&Version=1.0.0&Format=tiles&TileMatrix={z}&TileCol={x}&TileRow={y}&tk=" + key,
    }),
})

const vectorTileLayer = new TileLayer({
    source: new XYZ({
        crossOrigin: "anonymous",
        minZoom: 10,
        url: "https://t0.tianditu.gov.cn/DataServer?T=vec_w&x={x}&y={y}&l={z}&tk=" + key,
    }),
})

const annTileLayer = new TileLayer({
    source: new XYZ({
        crossOrigin: "anonymous",
        minZoom: 7,
        url: "https://t0.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=133266f7bdee1720f415c3326db1cfb8",
    }),
})

let vectorSource = new VectorSource({
    url: staticData.map,
    format: new GeoJSON()
})

const vectorLayer = new VectorLayer({
    source: vectorSource,
    style: new Style({
        stroke: new Stroke({
            color: "#3388ff",
            width: 2,
        })
    })
})

let view = new View({
    center: staticData.center,
    zoom: 9,
    projection: "EPSG:4326",
    maxZoom: 18,
    minZoom: 8,
})
const map = new Map({
    target: "map",      // 指定id属性
    view: view,
    controls: defaultControls({
        zoom: false,
        rotate: true,
        attribution: {}
    }).extend([
        new ScaleLine({
            units: "metric"
        })
    ]),
    layers: [imageTileLayer, annTileLayer, vectorLayer],
});


let drawLayer = new VectorLayer({
    source: new VectorSource(),
    style: new Style({
        fill: new Fill({
            color: 'rgba(0, 0, 255, 0)'
        }),
        stroke: new Stroke({
            color: '#0000ff',
            width: 3,
            lineDash: [10]
        })
    })
})
map.addLayer(drawLayer)
let currentBaseLayer = 'img';
function clearVectorLayer(){
    drawLayer.getSource().clear();
}

let buttons = document.querySelectorAll(".buttons button");

buttons[0].onclick = function () {
    let view = new View({
        center: staticData.center,
        zoom: 9,
        projection: "EPSG:4326",
        maxZoom: 18,
        minZoom: 8,
    })
    map.setView(view);
}

buttons[1].onclick = function () {
    let drawSource = new VectorSource();
    let mapDoc = document.querySelector('#map')
    mapDoc.style.cursor = "pointer";
    let draw = new Draw({
        source: drawSource,
        type: 'Polygon',
        style: new Style({
            fill: new Fill({
                color: 'rgba(51,136,255,0.2)'
            }),
            stroke: new Stroke({
                color: '#3388ff',
                width: 3,
                lineDash: [5, 5]
            })
        })
    });
    map.addInteraction(draw);
    draw.on("drawend", function (){
        clearVectorLayer()
        drawLayer.setSource(drawSource);
        map.removeInteraction(draw);
        mapDoc.style.cursor = "default";
    })
}

buttons[2].onclick = function () {
    clearVectorLayer()
}

buttons[3].onclick = function () {
    let canvas = map.getViewport().querySelector('canvas');
    let link = document.createElement('a');
    link.href = canvas.toDataURL('image/png');
    link.download = 'map.png';
    link.click();
}


let switchBtn = document.getElementById('switchBaseMap')
switchBtn.onclick = function () {
    let layers = map.getLayers();
    layers.removeAt(0)
    if (currentBaseLayer === 'img') {
        layers.insertAt(0, vectorTileLayer)
        switchBtn.style.backgroundImage = 'url("/satellite.jpg")'
        currentBaseLayer = "vec"
    }
    else
    {
        layers.insertAt(0, imageTileLayer)
        switchBtn.style.backgroundImage = 'url("/topo.jpg")'
        currentBaseLayer = "img"
    }
}


let s = document.getElementById('dropdown')
s.onclick = function () {
    let e = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    let layer = layui.layer;
    layer.open(
        {
            type: 1, // page 层类型
            area: ['500px', '400px'],
            title: '区域查询',
            shade: 0.6, // 遮罩透明度
            shadeClose: false, // 点击遮罩区域，关闭弹层
            content:
                `
      <div class="search-popup">
        <form class="layui-form" lay-filter="searchForm">
          <div class="select-container">
            <select name="county" lay-filter="county">
              <option value="">请选择县区</option>
            </select>
            <select name="town" lay-filter="town">
              <option value="">请选择乡镇</option>
            </select>
            <select name="village" lay-filter="village">
              <option value="">请选择村</option>
            </select>
          </div>
          <div class="button-container">
            <button type="button" class="layui-btn" lay-submit lay-filter="searchSubmit">搜索</button>
            <button type="button" class="layui-btn layui-btn-primary" id="cancelSearch">取消</button>
          </div>
        </form>
      </div>
                `
        }
    );
    layui.form.render('select', 'searchForm')
}

