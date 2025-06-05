<script setup>
import {ref} from 'vue'
import MapLayersChangeBox from "../common/MapLayersChangeBox.vue";
import {faMap} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {changeBaseLayer} from "../module/Map/BaseLayer.js";
import setTer from "../module/Map/TerrainLayer.js";

const isTer = ref(true)
const currLayer = ref(1)
const layers = {
  "天地图矢量": {
    index: 0,
    img: "./images/vecBaseLayer.png"
  },
  "天地图影像": {
    index: 1,
    img: "./images/imgBaseLayer.png"
  },
  "高德矢量": {
    index: 2,
    img: "./images/vecBaseLayer.png"
  },
  "高德影像": {
    index: 3,
    img: "./images/imgBaseLayer.png"
  }
}

</script>

<template>
<MapLayersChangeBox>
  <template #title>
    <div class="name"><span><font-awesome-icon :icon="faMap"/>底图</span></div>
  </template>
  <template #content>
    <div class="layers-box-content">
      <ul class="layers-box">
        <li
            v-for="(layer,name) in layers"
            :class="{on: currLayer===layer.index}"
            @click="currLayer=layer.index;changeBaseLayer(layer.index)"
        >
          <div>
            <img :src="layer.img" alt=""/>
          </div>
          <div>{{name}}</div>
        </li>
      </ul>
    </div>
    <div class="show-terrain" style="margin-left: 10px; color: rgb(255, 255, 255);">
      <el-checkbox @change="setTer(isTer)" label="显示地形" v-model="isTer"></el-checkbox>
    </div>
  </template>
</MapLayersChangeBox>
</template>

<style scoped>
.layers-box{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  width: 354px;
  padding: 0 10px;
  box-sizing: border-box;
}
.layers-box li{
  margin-top: 10px;
  cursor: pointer;
}
.layers-box li div:first-child{
  width: 76px;
  height: 76px;
  background: red;
  border: 2px solid white;
  box-sizing: border-box;
}
.layers-box li.on div:first-child{
  border: solid 2px #337fe5;
}
.layers-box li:hover div:first-child{
  border: solid 2px #337fe5;
}

.layers-box li div:first-child img{
  width: 100%;
  height: 100%;
}

.layers-box li div:last-child{
  width: 76px;
  height: 20px;
  line-height: 20px;
  color: #fff;
  font-size: 12px;
  text-align: center;
}

.layers-box li.on div:last-child{
  color: #337fe5;
}

.layers-box li:hover div:last-child{
  color: #337fe5;
}
.show-terrain .el-checkbox {
  color: #fff;
}
.show-terrain .el-checkbox :deep(.el-checkbox__label){
  color: #fff;
}
</style>