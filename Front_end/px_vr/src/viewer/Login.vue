<script setup>

import {ref} from 'vue'
import axios from "axios";
import {storage} from "../store/storage.js";
import {useRouter} from "vue-router";

const username = ref("")
const password = ref("")
const router = useRouter();

async function login() {
  const res = await axios("./api/users.json")
  const data = res.data
  if (username.value === data.user && password.value === data.password) {
    storage.set("login", "activate")
    const r = await axios("./api/tokens.json")
    const token = r.data.token
    storage.set("token", token)
    await router.push("/map")
  }
  else {
    ElMessage({
      message: "用户密码错误",
      type: 'error',
      duration: 3000
    })
  }
}

</script>

<template>
  <div class="login">
    <div class="login-title">江西萍乡化工园区</div>
    <div class="get-ingo">
      <p class="title">用户登录</p>
      <el-input v-model="username" class="username input"></el-input>
      <el-input v-model="password" class="password input" type="password"></el-input>
      <el-button type="primary" class="login-to" @click="login">登录</el-button>
    </div>
  </div>
</template>

<style scoped>
.login{
  width: 100%;
  height: 100%;
  background: url(/login/login-bg.png);
  background-size: 100% 100%;
  position: relative;
}
.login-title{
  position: absolute;
  top: 18%;
  right: 25%;
  transform: translate(50%);
  font-size: 40px;
  color: #00afe9;
}
.get-ingo{
  width: 500px;
  position: absolute;
  text-align: center;
  top: 45%;
  right: 25%;
  transform: translateY(-40%) translate(50%);
  color: #fff;
  padding: 30px;
  background: url(/login/login-content-bg.png), url(/login/login-content-bg-left-top.png) no-repeat left top, url(/login/login-content-bg-left-button.png) no-repeat left bottom, url(/login/login-content-bg-right-top.png) no-repeat right top, url(/login/login-content-bg-right-button.png) no-repeat right bottom;
  background-repeat: no-repeat;
  background-size: 100% 100%, 25px, 25px, 25px, 25px;
}
.get-ingo .title{
  font-size: 20px;
}
.get-ingo .username{
  background: url(/login/login-input.png) no-repeat, url(/login/login-user.png) no-repeat 10px center;
  background-size: 100% 100%, 20px;
}
.get-ingo .input{
  margin: 30px 0;
  width: 300px;
  padding: 10px 10px 10px 40px;
  background-color: #0000;
  color: #fff;
  border-width: 0px;
  font-size: 18px;
}
.get-ingo .password{
  background: url(/login/login-input.png) no-repeat, url(/login/login-pwd.png) no-repeat 10px center;
  background-size: 100% 100%, 20px;
}
.get-ingo .login-to{
  width: 300px;
  margin: 30px 0;
}
</style>