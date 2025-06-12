<script setup>
import {useRouter} from "vue-router";

const router = useRouter();
const title = "江西省中国科学院庐山植物园VR平台"
const routes = [
  {
    path: "/map/main/survey",
    name: "简介"
  }
]

</script>

<template>
  <div class="main-header">
    <div class="title">{{title}}</div>
  </div>
  <div class="main-container">
    <router-view/>
  </div>
  <div class="page-mode">
    <div
        v-for="(route, index) in routes"
        :key="index"
        :class="{active: router.currentRoute.value.path === route.path}"
        @click="router.push(route.path)"
    >
      {{route.name}}
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