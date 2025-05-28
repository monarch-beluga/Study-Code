<script setup>
import {toRefs, inject, ref} from "vue";
import qyxxPage from "./qyxxPage.vue";
import qyYjwzPage from "./qyYjwzPage.vue";
import qyYjkjPage from "./qyYjkjPage.vue";
import qyJydwPage from "./qyJydwPage.vue";
import {useRouter} from "vue-router";

const props = defineProps({
  info: String
})
const {info} = toRefs(props)

const changePage1 = inject('changePage1')
const mapTreeChange = inject("mapTreeChange")
const initViewrPs = inject("initViewrPs")
const initQjmnLayer = inject("initQjmnLayer")
const initQyfwLayer = inject("initQyfwLayer")
const initQyYjkjLayer = inject("initQyYjkjLayer")
const initQyYjwzLayer = inject("initQyYjwzLayer")

const uRouter = useRouter()
function backHome(){
  uRouter.push("/map/main/survey")
  changePage1("page")
  initViewrPs()
  for (let i=6; i <= 13; i++)
    mapTreeChange(i, false)
  mapTreeChange(15, false)
  mapTreeChange(16, false)
  initQjmnLayer()
  initQyfwLayer()
  initQyYjkjLayer()
  initQyYjwzLayer()
  mapTreeChange(5, true)
}

const currentTab = ref("企业信息")
const tabs = {
  "企业信息": qyxxPage,
  "应急物资": qyYjwzPage,
  "应急空间": qyYjkjPage,
  "救援队伍": qyJydwPage
}
function pageFun() {
  initQyYjkjLayer()
}



</script>

<template>
  <div class="container cur-page-container">
    <div class="main-header">
      <div class="title">{{info}}</div>
      <div class="back-home">
        <div class="center-info cursor-p" @click="backHome">
          <img src="/images/back-home.png" class="img" alt>
          <span>返回</span>
        </div>
      </div>
    </div>

    <div class="main-container">
      <component :is="tabs[currentTab]" :info="info"></component>
    </div>
    <div class="page-mode">
      <div
          v-for="(tab, index) in tabs"
          :key="index"
          :class="{active: currentTab === index}"
          @click="currentTab=index;pageFun()"
      >
        {{index}}
      </div>
    </div>
  </div>

</template>

<style scoped>
.container{
  position: absolute;
  width: 100%;
  height: 100%;
}
.container .main-header{
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  width: 100%;
  height: 6vh;
  pointer-events: auto;
}
.title{
  position: absolute;
  bottom: 2px;
  left: 74px;
  font-family: YouSheBiaoTiHei, YouSheBiaoTiHei;
  font-weight: 400;
  font-size: 24px;
  color: #fff;
  line-height: 38px;
  letter-spacing: 3px;
  text-shadow: 2px 3px 0px rgba(17, 20, 22, .2196);
  text-align: left;
  font-style: normal;
  text-transform: none;
}
.back-home {
  position: absolute;
  bottom: 2px;
  right: 30px;
}
.back-home .center-info{
  display: flex
;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 13px;
}
.cursor-p {
  cursor: pointer;
}
.back-home .img{
  width: 36px;
  height: 36px;
}
.back-home .center-info span{
  margin-right: 10px;
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
.container .main-container{
  position: absolute;
  inset: 80px 40px 40px;
}
</style>