<script setup>
import {ref, onMounted, onUnmounted} from "vue"
import {getBusinessDetail, getCurrBusiness} from "../module/Map/Business.js";
import {useRouter} from "vue-router";
import * as DC from '@dvgis/dc-sdk'

const router = useRouter();
const title = ref("")
const routes = [
  {
    path: "/map/sub/companyInfo",
    name: "企业信息"
  },
  {
    path: "/map/sub/companySup",
    name: "应急物资"
  },
  {
    path: "/map/sub/companyRt",
    name: "救援队伍"
  },
  {
    path: "/map/sub/companySpace",
    name: "应急空间"
  }
]

function featureToWall(feature){
  let layer = new DC.VectorLayer('qyfw')
  $viewer.addLayer(layer)
  let wall = new DC.Wall(feature)
  wall.setStyle({
    material: new DC.WallTrailMaterialProperty({
      color: DC.Color.fromCssColorString("#e1d930"),
      speed: 10
    })
  })
  layer.addOverlay(wall)
  $viewer.flyTo(layer, 3)
}

onMounted(async ()=>{
  title.value = getCurrBusiness()
  const detail = await getBusinessDetail()
  featureToWall(detail['feature'])
})
onUnmounted(() => {
  $viewer.getLayer("qyfw").remove()
  $viewer.zoomToPosition(DC.Position.fromArray([113.6710986691894, 27.60570497563303, 9000, 360, -90]))
})
</script>

<template>
  <div class="main-header">
    <div class="title">{{title}}</div>
    <div class="back-home">
      <router-link to="/map/main/survey">
        <div class="center-info cursor-p">
          <img src="/images/back-home.png" class="img" alt>
          <span>返回</span>
        </div>
      </router-link>
    </div>
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
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  width: 100%;
  height: 6vh;
  pointer-events: auto;
}
.main-header .title{
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
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 13px;
}
.back-home .center-info:hover{
  background: #266894;
  border-radius: 18px;
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

.main-container{
  position: absolute;
  inset: 80px 40px 40px;
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
.page-mode>a{
  text-decoration: none;
}
.page-mode div{
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
.page-mode div.active{
  color: #f6fcff;
  background-image: url('/images/mode-tab-ac.png');
}
</style>