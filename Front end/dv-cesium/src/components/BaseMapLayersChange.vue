<script setup>
import {inject, ref} from 'vue'

const setTer = inject("setTer")
const BaseMapChange = inject("BaseMapChange")

const curr = ref("天地图影像")
const layers = {
  "天地图矢量": 0,
  "天地图影像": 1,
  "高德矢量": 2,
  "高德影像": 3,
}
const img_src = {
  0: "/images/vecBaseLayer.png",
  1: "/images/imgBaseLayer.png",
  2: "/images/vecBaseLayer.png",
  3: "/images/imgBaseLayer.png",
}

let isTer = false
function terChange(){
  setTer(isTer)
  isTer = !isTer
}

</script>

<template>
  <div class="layers-box-content">
    <ul class="layers-box">
      <li
        v-for="(index,l) in layers"
        :key="l"
        :class="{on: curr===l}"
        @click="curr=l;BaseMapChange(index)"
        >
        <div>
          <img :src="img_src[index]">
        </div>
        <div>{{l}}</div>
      </li>
    </ul>
  </div>
  <div class="show-terrain" style="margin-left: 10px; color: rgb(255, 255, 255);">
    <el-checkbox @change="terChange" label="显示地形" checked></el-checkbox>
  </div>
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
.show-terrain .el-checkbox.is-checked{
  color: #fff;
}

</style>