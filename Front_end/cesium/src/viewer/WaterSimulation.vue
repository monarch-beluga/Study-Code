<script setup>
import * as Cesium from "cesium";
import { FluidRenderer } from "../utils/waterSimulation.js";
import { mapManager } from "../utils/mapManager";

let viewer = mapManager.getViewer()

async function WaterSimulation() {
  // const result = CreateWallByCenter(115.615, 27.910, 2000, 1000)
  ElMessage({
    message: "点击地图选定模拟位置",
    type: 'success',
    duration: 3000
  })
  // viewer.entities.add(result.entity)
  let waterFluid;
  let handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);
  handler.setInputAction((movement) => {
    if (waterFluid) return;
    let cartesian = viewer.scene.pickPosition(movement.position);
    let cartographic = Cesium.Cartographic.fromCartesian(cartesian);
    let lon = Cesium.Math.toDegrees(cartographic.longitude);
    let lat = Cesium.Math.toDegrees(cartographic.latitude);
    viewer.camera.flyTo({
      destination: Cesium.Cartesian3.fromDegrees(lon, lat, 10000),
      duration: 3, // 飞行时间（秒）
      orientation: {
        heading: Cesium.Math.toRadians(0), // 朝向
        pitch: Cesium.Math.toRadians(-90), // 俯视
        roll: 0
      },
      complete: async () => {
        waterFluid = new FluidRenderer(viewer, {
          lonLat: [lon, lat],
          // 纹理尺寸
          width: 2048,
          height: 2048,
          // 渲染范围 根据地形自行调整渲染高度
          dimensions: new Cesium.Cartesian3(4000, 4000, 1000),
          fluidParams: new Cesium.Cartesian4(0.85, 0.25, 0.0001, 0.1),
          customParams: new Cesium.Cartesian4(15, 20, 0.2, 10),
          radius: 0.005,

          // 归一化高度 最大高与上面的z对齐
          minHeight: 0,
          maxHeight: 1000
        });
        viewer.camera.flyTo({
          destination: Cesium.Cartesian3.fromDegrees(lon, lat-0.05, 4000),
          duration: 3, // 飞行时间（秒）
          orientation: {
            heading: Cesium.Math.toRadians(0), // 朝向
            pitch: Cesium.Math.toRadians(-45), // 俯视
            roll: 0
          }})
        ElMessage({
          message: "点击地图产生水流",
          type: 'success',
          duration: 3000
        })
      }
    })

    handler.destroy();
  }, Cesium.ScreenSpaceEventType.LEFT_CLICK);

}


</script>

<template>
  <div class="flood-controls">
    <el-card class="box-card">

      <div class="button-group">
        <el-button
            type="primary"
            @click="WaterSimulation"
        >
          开始
        </el-button>
      </div>

    </el-card>
  </div>
</template>

<style scoped>
.flood-controls {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 100;
  width: 100px;
}

.button-group {
  display: flex;
  justify-content: space-between;
}
</style>