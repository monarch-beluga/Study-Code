<script setup>
import {inject, ref, toRefs} from 'vue'
import YjkjPage from "./YjkjPage.vue";
import SjfkPage from "./SjfkPage.vue";
import KzqjPage from "./KzqjPage.vue";

const staticData = inject("staticData")

const props = defineProps({
  info: String
})
const {info} = toRefs(props)

const currentTab = ref(info.value)
const mapTreeChange = inject("mapTreeChange")
const showSjfkLayer = inject("showSjfkLayer")
let title = staticData.title

const tabs = {
  "应急空间": YjkjPage,
  "三级防控": SjfkPage,
  "360全景": KzqjPage,
}

function sjfkLayerClose() {
  let l = ['1', '2', '3'];
  l.forEach((item) => {
    showSjfkLayer(item, false)
  })
}

function yjkjLayerClose() {
  for (let i=6; i <= 14; i++)
    mapTreeChange(i, false)
}

function pageFun(index) {
  if (index === "应急空间"){
    sjfkLayerClose()
    yjkjLayerClose()
    mapTreeChange(6, true)
  }
  else if (index === "三级防控"){
    yjkjLayerClose()
    showSjfkLayer("1", true)
  }
  else {
    sjfkLayerClose()
    yjkjLayerClose()
  }
}

const changePage = inject("changePage")
function zztClick() {
  changePage("作战图")
}

</script>

<template>
  <div class="main-header">
    <div class="title">{{title}}</div>
  </div>
  <div class="main-container">
    <component :is="tabs[currentTab]"></component>
  </div>
  <div class="page-mode">
    <div
        v-for="(tab, index) in tabs"
        :key="index"
        :class="{active: currentTab === index}"
        @click="currentTab=index;pageFun(index)"
      >
      {{index}}
    </div>
    <div
        :class="{active: currentTab === '作战图'}"
        @click="currentTab='作战图';zztClick()"
    >
      作战图
    </div>
  </div>
</template>

<style scoped>
  .main-header{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40px;
    pointer-events: auto;
  }
  .main-header .title{
    position: absolute;
    inset: 0;
    margin: auto;
    width: 640px;
    height: 40px;
    font-size: 24px;
    font-weight: 400;
    z-index: 99;
    font-family: YouSheBiaoTiHei;
    color: #eff8fc;
    line-height: 40px;
    text-align: center;
    letter-spacing: 8px;
    font-weight: bolder;
    background: linear-gradient(to bottom, #e2eaf0, #aed1f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .main-container{
    position: absolute;
    inset: 40px;
  }
  .page-mode{
    position: absolute;
    top: auto;
    bottom: 55px;
    left: 50%;
    z-index: 99;
    transform: translate(-50%);
    display: flex;
    pointer-events: auto;
  }
  .page-mode>div{
    background-image: url('/images/mode-tab.png');
    background-size: cover;
    width: 136px;
    height: 50px;
    font-size: 16px;
    text-align: center;
    font-weight: 700;

    color: #bfd3e5;
    line-height: 32px;
    padding-top: 12px;
    margin-right: -20px;
    font-style: italic;
    cursor: pointer;
    box-sizing: border-box;
  }
  .page-mode>div.active{
    color: #f6fcff;
    background-image: url('/images/mode-tab-ac.png');
  }
</style>