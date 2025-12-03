<script setup>
import {useRouter} from "vue-router";
import {storage} from "../store/storage.js";

const router = useRouter();
const title = "萍乡化工园区“一园一策一图”VR平台"
const routes = [
  {
    path: "/map/main/survey",
    name: "园区概况"
  },
  {
    path: "/map/main/rs",
    name: "风险源"
  },
  {
    path: "/map/main/space",
    name: "应急空间"
  },
  {
    path: "/map/main/pac",
    name: "多级防控"
  },
  {
    path: "/map/main/pd",
    name: "情景模拟"
  },
  {
    path: "/table/supplies",
    name: "应急物资"
  },
  {
    path: "/table/rt",
    name: "救援队伍"
  },
  {
    path: "/table/zzt",
    name: "作战图"
  }
]

function loginOut(){
  storage.set("login", "")
  storage.set("token", "")
  router.push("/login")
}

</script>

<template>
  <div class="main-header">
    <div class="title">{{title}}</div>
    <div class="login-out">
      <div class="center-info cursor-p" @click="loginOut">
        <img src="/login/login-out.png" class="img" alt>
        <span>返回</span>
      </div>
    </div>
  </div>
  <div class="main-container">
    <router-view/>
  </div>
  <div class="page-mode">
    <router-link v-for="route in routes"
                 :to="route.path">
      <div :class="{active: router.currentRoute.value.path === route.path}">
        {{route.name}}
      </div>
    </router-link>
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
.main-header .login-out{
  position: absolute;
  top: 10px;
  right: 40px;
  height: 36px;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10px;
  cursor: pointer;
}
.login-out .center-info{
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 13px;
}
.main-header .login-out:hover{
  background: #266894;
  border-radius: 18px;
}
.main-header .login-out .img{
  width: 16px;
  height: 16px;
  margin-right: 5px;
}
.main-header .login-out span{
  font-size: 13px;
}
.main-container{
  position: absolute;
  inset: 54px 40px;
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