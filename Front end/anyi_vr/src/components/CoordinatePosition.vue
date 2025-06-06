<script setup>
import * as DC from '@dvgis/dc-sdk'
import MapLayersChangeBox from "../common/MapLayersChangeBox.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faMapPin} from "@fortawesome/free-solid-svg-icons";
import {ref} from "vue"

let coordLng = ref(0)
let coordLat =  ref(0)
let coordEle = ref(0)
const coordTools = {
  "经度": coordLng,
  "纬度": coordLat,
  "高度": coordEle
}

function viewFlyToPoint() {
  const p = DC.Position.fromArray([coordLng.value, coordLat.value, coordEle.value, 360, -90, 0])
  $viewer.flyToPosition(p)
}

</script>

<template>
  <MapLayersChangeBox>
    <template #title>
      <div class="name"><span><font-awesome-icon :icon="faMapPin"/>坐标定位</span></div>
    </template>
    <template #content>
      <div class="cur-content">
        <div v-for="(item, index) in coordTools">
          <span>{{index}}:</span>
          <el-input
              v-model="item.value"
              size="small">
          </el-input>
        </div>
      </div>
      <div class="cur-btn">
        <el-button
            type="primary"
            @click="viewFlyToPoint"
            size="small">
          坐标定位
        </el-button>
      </div>
    </template>
  </MapLayersChangeBox>
</template>

<style scoped>
.cur-content>div span{
  width: 54px;
}
.cur-btn{
  margin: 10px 0;
  display: flex
;
  justify-content: center;
  align-items: center;
}
.cur-content>div{
  margin-top: 10px;
  padding: 0 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
:deep(.el-input__wrapper) {
  background: #3f4854b3 !important;
  border: none !important;
  border-radius: 5px;
  box-shadow: none;
}
:deep(.el-input__wrapper input){
  color: #fff
}
.el-button{
  background-color: rgba(13,100,167,.8);
  color: #fff;
  border: none;
}
.el-button:hover{
  background-color: rgba(86, 147, 193, 0.86);
}
.el-button:active{
  background-color: rgba(14, 84, 138, 0.84);
}
</style>