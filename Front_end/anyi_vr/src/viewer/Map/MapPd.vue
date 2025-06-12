<script setup>

import {CaretLeft, CaretRight} from "@element-plus/icons-vue";
import {inject, ref, onMounted, onUnmounted} from "vue";
import {getPdLayer, initPdLayer, removePdLayer} from "../../module/Map/PdLayer.js";

const MapLayerTreeChange = inject("MapLayerTreeChange")
const initMainMapLayer = inject("initMainMapLayer")
const panelDisplay = ref(true)

const tabs = [
  {
    index:1,
    title: "情景模拟一",
    content: "危险化学品泄漏:安义工业园区化工集中区东阳片区一某企业二氯二甲基硅烷储罐泄漏，如不采取措施，将造成污染事故，影响到潦河下游水质。"
  },
  {
    index:2,
    title: "情景模拟二",
    content: "危险化学品运输泄漏事故:安义工业园区化工集中区东阳大道，一辆载有二甲苯的储罐车发生交通事故，导致部分二甲苯泄漏，二甲苯通过路边雨水井进入雨水管道，如不采取措施，将造成污染事故，影响到潦河下游水质。"
  },
  {
    index:3,
    title: "情景模拟三",
    content: "危险化学品泄漏:安义工业园区化工集中区万埠片区江西晶安高科股份有限公司盐酸罐区，因储罐阀门破损导致盐酸泄漏，如不采取措施，将造成水污染事故，影响到潦河下游水质。"
  },
  {
    index:4,
    title: "情景模拟四",
    content: "重金属废水泄漏:安义工业园区化工集中区东阳片区二某企业因设备故障，含铊废水泄露，如不采取措施，废水流出企业后，将造成污染事故，影响到潦河下游水质。"
  },
]

function FunClick(item){
  panelDisplay.value = false
  getPdLayer(item.index)
}

onMounted(() => {
  MapLayerTreeChange(18, true)
  initPdLayer()
})
onUnmounted(() => {
  try{
    initMainMapLayer()
    removePdLayer()
  }catch (err){

  }
})

</script>

<template>
  <div class="telescopic-panel" @click="panelDisplay = !panelDisplay">
    <el-icon v-show="panelDisplay" ><CaretLeft /></el-icon>
    <el-icon v-show="!panelDisplay"><CaretRight /></el-icon>
  </div>
  <div class="panel-container no-select" v-show="panelDisplay">
    <el-carousel
        type="card"
        style="overflow: hidden"
        height="360px"
        :autoplay="false">
      <el-carousel-item
          v-for="tab in tabs"
          style="background: #2e4274"
      >
        <div class="content-box flex f-d-c">
          <div class="title">{{tab.title}}</div>
          <div class="content h0 flex-1">
            <div class="bg-box"></div>
            <div class="describe-box">{{tab.content}}</div>
          </div>
          <div class="footer-btn">
            <div class="start-btn" @click="FunClick(tab)">开始模拟</div>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<style scoped>
.telescopic-panel{
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 50%;
  left: 0;
  width: 20px;
  height: 60px;
  border-radius: 0 6px 6px 0;
  box-shadow: inset 0 0 40px #409eff;
  pointer-events: all;
  color: #fff;
  transform: translateY(-50%);
  cursor: pointer;
}

.no-select{
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.panel-container{
  position: absolute;
  inset: 0;
  margin: auto;
  width: 960px;
  height: 440px;
  pointer-events: all;
}
.content-box {
  padding: 10px 0;
  width: 100%;
  height: 100%;
  color: #fff;
}
.f-d-c {
  flex-direction: column;
}
.flex {
  display: flex;
}
.content-box .title {
  padding-left: 40px;
  height: 80px;
  line-height: 80px;
  font-size: 44px;
  font-weight: 700;
  font-style: initial;
  background: #3a7bd5;
  background: -webkit-linear-gradient(to right,#3a7bd5,rgba(255,255,255,.1));
  background: linear-gradient(to right, #3a7bd5, #ffffff1a);
}
.content-box .content {
  margin-top: 20px;
  padding: 0 20px;
}
.h0 {
  height: 0;
}
.flex-1 {
  flex: 1;
}
.content-box .content .describe-box {
  line-height: 36px;
}
.content-box .footer-btn {
  margin-bottom: 40px;
  height: 40px;
  line-height: 40px;
  text-align: center;
}
.start-btn, .start-btn:focus, .start-btn:hover {
  padding: 0 10px;
  display: inline-block;
  position: relative;
  min-width: 96px;
  border: none;
  border-radius: 8px;
  background: #491cc5;
  background: -webkit-linear-gradient(to bottom,#491cc5,#5f80f5);
  background: linear-gradient(to bottom, #491cc5, #5f80f5);
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  box-shadow: 0 0 10px #ffffff80;
  transition: transform ease-in .1s, box-shadow ease-in .25s;
  transform: skew(8deg);
}
</style>