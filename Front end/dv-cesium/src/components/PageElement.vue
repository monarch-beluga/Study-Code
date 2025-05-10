<script setup>
import {inject, provide, ref, toRefs} from 'vue'
import YjkjPage from "./yjkj/YjkjPage.vue";
import SjfkPage from "./sjfk/SjfkPage.vue";
import YqgkPage from "./yqgk/YqgkPage.vue";
import rsPage from "./fxy/rsPage.vue";
import QjmnPage from "./qjmn/QjmnPage.vue";

const staticData = inject("staticData")
const stopSpeak = inject("stopSpeak")
const initViewrPs = inject("initViewrPs")

const props = defineProps({
  info: String
})
const {info} = toRefs(props)

const currentTab = ref(info.value)
const mapTreeChange = inject("mapTreeChange")
const showSjfkLayer = inject("showSjfkLayer")
const initQjmnLayer = inject("initQjmnLayer")
let title = staticData.title

const tabs = {
  "园区概况": YqgkPage,
  "风险源": rsPage,
  "应急空间": YjkjPage,
  "多级防控": SjfkPage,
  "情景模拟": QjmnPage,
}

function sjfkLayerClose() {
  let l = ['1', '2', '3', '4'];
  l.forEach((item) => {
    showSjfkLayer(item, false)
  })
}

function pageFun(index) {
  if (currentTab.value !== index){
    currentTab.value = index
    stopSpeak()
    initViewrPs()
    for (let i=5; i <= 13; i++)
      mapTreeChange(i, false)
    mapTreeChange(15, false)
    mapTreeChange(16, false)
    mapTreeChange(17, false)
    mapTreeChange(18, false)
    sjfkLayerClose()
    initQjmnLayer()

    if (index === "应急空间"){
      mapTreeChange(6, true)
    }
    else if (index === "多级防控"){
      showSjfkLayer("1", true)
    }
    else if (index === "园区概况"){
      mapTreeChange(5, true)
    }
    else if (index === "风险源"){
      mapTreeChange(15, true)
      mapTreeChange(16, true)
    }
    else if (index === "情景模拟"){
      mapTreeChange(18, true)

    }
  }
}
provide("pageFun", pageFun)

const tab1s = {
  "应急物资": "应急物资",
  "救援队伍": "救援队伍",
  "作战图": "作战图"
}
const changePage = inject("changePage")
function funClick(index) {
  changePage(index)
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
        @click="pageFun(index)"
      >
      {{index}}
    </div>
    <div
        v-for="(tab, index) in tab1s"
        :key="index"
        :class="{active: currentTab === index}"
        @click="currentTab=index;funClick(index)"
    >
      {{index}}
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