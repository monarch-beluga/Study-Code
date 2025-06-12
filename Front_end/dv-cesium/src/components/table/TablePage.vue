<script setup>
import {inject, ref, toRefs} from "vue";
import YjzyPage from "./YjzyPage.vue";
import JydwPage from "./JydwPage.vue";
import {useRouter} from "vue-router";

const staticData = inject("staticData")
let title = staticData.title
const props = defineProps({
  info: String
})
const {info} = toRefs(props)
const uRouter = useRouter()
const tabs = {
  "/map/main/survey":  "园区概况",
  "/map/main/rs":  "风险源",
  "/map/main/space":  "应急空间",
  "/map/main/pac": "多级防控",
  "/map/main/pd": "情景模拟",
  "/table/supplies": "应急物资",
  "/table/rt": "救援队伍",
  "/zzt": "作战图"
}
const pages = {
  "/table/supplies": YjzyPage,
  "/table/rt": JydwPage
}
const changePage = inject("changePage")
function funClick(index) {
  changePage(index)
}
</script>

<template>
  <div class="w100 h100 relative main-content" id="MainContent">
    <div class="main-header">
      <div class="title">{{title}}</div>
    </div>
    <div class="main-container">
      <div class="container page-container">
        <div class="w100 h100 img-box">
          <div class="content">
            <component :is="pages[uRouter.currentRoute.value.path]"></component>
          </div>
        </div>
      </div>
    </div>
    <div class="page-mode">
      <div
          v-for="(tab, index) in tabs"
          :key="tab"
          :class="{active: uRouter.currentRoute.value.path === index}"
          @click="uRouter.push(index)"
      >
        {{tab}}
      </div>
    </div>
  </div>
</template>

<style scoped>
.content{
  padding: 20px 0;
  height: calc(100% - 32px);
}
.main-content .main-container{
  position: absolute;
  inset: 54px 40px;
}
.main-content{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  unicode-bidi: isolate;
  background: url('/images/header.png') no-repeat center / 100% 100%, url('/images/pro-bg.png') center center / 100% 100% no-repeat, rgb(0, 0, 0);
}
.container{
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: auto;
  background: #1c73c333
}
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
.container .img-box{
  pointer-events: all;
  overflow: hidden auto;
}
</style>