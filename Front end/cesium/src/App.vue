<script setup>
import * as Cesium from 'cesium'
import 'cesium/Build/Cesium/Widgets/widgets.css';
import {onMounted} from 'vue'

  Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmZTg2NjE4OC00MDdlLTQ5MTAtOWE1Yi01ODE4NDNmZTg0NGYiLCJpZCI6MjY3MzcyLCJpYXQiOjE3MzYyNTE1MjZ9.rNEN-2zDT2yCOXP1T4yyr6axw7mM_Y-28e8hGvUzPdg'

  const addWorldTerrainAsync = async (viewer) => {
    try {
      viewer.terrainProvider = await Cesium.createWorldTerrainAsync({
        requestVertexNormals: true,
        requestWaterMask: true,
      });
    } catch (error) {
      console.log("Failed to add world imagery: ${error}");
    }
  };

  onMounted(function () {
    let key = "8899fd3e86aa994f71465b1c56a98727";
    let viewer = new Cesium.Viewer('cesiumContainer', {
      // 取消cesium默认控件
      infoBox: false,
      homeButton: false,
      geocoder: false,
      sceneModePicker: false,
      baseLayerPicker: false,
      navigationHelpButton: false,
      animation: false,
      timeline: false,
      fullscreenButton: false,
      // 天空盒子
      skyBox: new Cesium.SkyBox({
        sources : {
          positiveX : './SkyBox_Textures/px.png',
          negativeX : './SkyBox_Textures/nx.png',
          positiveY : './SkyBox_Textures/py.png',
          negativeY : './SkyBox_Textures/ny.png',
          positiveZ : './SkyBox_Textures/pz.png',
          negativeZ : './SkyBox_Textures/nz.png'
        }
      }),
    });
    //显示地形
    // addWorldTerrainAsync(viewer)
    viewer.cesiumWidget.creditContainer["style"].display = 'none';
    viewer.camera.setView({
      // fromDegrees()方法，将经纬度和高程转换为世界坐标
      destination:Cesium.Cartesian3.fromDegrees(116.006,29.68,3000.0),
      orientation:{
        // 指向
        heading:Cesium.Math.toRadians(0),
        // 视角
        pitch:Cesium.Math.toRadians(-30),
        roll:0.0
      }
    });


    viewer.imageryLayers.get(0).show = false

    // 加载天地图影像地图
    let layers = viewer.imageryLayers;
    let ImgLayer = layers.addImageryProvider(
        new Cesium.WebMapTileServiceImageryProvider({
          url: "https://{s}.tianditu.gov.cn/img_w/wmts?service=wmts&request=GetTile&version=1.0.0" +
              "&LAYER=img&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}" +
              "&style=default&format=tiles&tk="+key,
          layer: "tdtImgLayer",
          style: "default",
          subdomains: ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
          format: "tiles",
          tileMatrixSetID: "GoogleMapsCompatible",
          maximumLevel: 18,
          minimumLevel: 0,
    }))

    let VecLayer = layers.addImageryProvider(
        new Cesium.WebMapTileServiceImageryProvider({
          url: "https://{s}.tianditu.gov.cn/vec_w/wmts?service=wmts&request=GetTile&version=1.0.0" +
              "&LAYER=vec&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}" +
              "&style=default&format=tiles&tk="+key,
          layer: "tdtVecLayer",
          subdomains: ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
          style: "default",
          format: "tiles",
          tileMatrixSetID: "GoogleMapsCompatible",
          maximumLevel: 18,
          minimumLevel: 0,
    }))

    let CiaLayer = layers.addImageryProvider(
        new Cesium.WebMapTileServiceImageryProvider({
          url: "https://{s}.tianditu.gov.cn/cia_w/wmts?service=wmts&request=GetTile&version=1.0.0" +
              "&LAYER=cia&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}" +
              "&style=default&format=tiles&tk="+key,
          layer: "tdtCiaLayer",
          subdomains: ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
          style: "default",
          format: "tiles",
          tileMatrixSetID: "GoogleMapsCompatible",
          maximumLevel: 18,
          minimumLevel: 0,
        }))

    let CvaLayer = layers.addImageryProvider(
        new Cesium.WebMapTileServiceImageryProvider({
          url: "https://{s}.tianditu.gov.cn/cva_w/wmts?service=wmts&request=GetTile&version=1.0.0" +
              "&LAYER=cva&tileMatrixSet=w&TileMatrix={TileMatrix}&TileRow={TileRow}&TileCol={TileCol}" +
              "&style=default&format=tiles&tk="+key,
          layer: "tdtCvaLayer",
          subdomains: ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"],
          style: "default",
          format: "tiles",
          tileMatrixSetID: "GoogleMapsCompatible",
          maximumLevel: 18,
          minimumLevel: 0,
        }))
    VecLayer.show = false;
    CvaLayer.show = false;




    // 隐藏loge

  })

</script>

<template>
  <div id="cesiumContainer" ref="cesiumContainer"></div>
</template>

<style scoped>

#cesiumContainer{
  width: 100%;
  height: 100%;
}

</style>
