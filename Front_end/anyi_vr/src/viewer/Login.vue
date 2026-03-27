<script setup>

import {ref} from 'vue'
import axios from "axios";
import {storage} from "../store/storage.js";
import {useRouter} from "vue-router";

const formData = ref({
  username: "",
  password: ""
})
const formRef = ref()
const rules = {
  username:[
    {required: true, message: "该项不能为空", trigger: "blur"}
  ],
  password:[
    {required: true, message: "该项不能为空", trigger: "blur"}
  ]
}
const router = useRouter();

async function login() {
  const baseUrl = import.meta.env.VITE_API_BASE_URL;
  try {
    const res = await axios.post(baseUrl + "/auth/login", formData.value)

    const { status, type, message, data } = res.data;
    if (status === 200){
      storage.set("username", data.username)
      console.log(data.username)
      storage.set("token", data.token)
      storage.set("role", data.role)
      await router.push("/map")
    }
    ElMessage({
      message: message,
      type: type,
      duration: 3000
    })

  }
  catch(error){
    ElMessage({
      message: error.message,
      type: 'error',
      duration: 3000
    })
  }
}

const btnLogin = async function () {
  try{
    await formRef.value.validate()
    await login()
  }
  catch (err){
    ElMessage.error('用户账号密码为空');
  }
}

</script>

<template>
  <div class="login">
    <div class="login-title">江西安义化工园区</div>
    <div class="get-ingo">
      <p class="title">用户登录</p>
      <div class="content">
        <el-form :model="formData"  :rules="rules" ref="formRef">
          <el-form-item label-position='top' prop="username">
            <el-input size="default" clearable v-model="formData.username" class="username input" placeholder="登录名">
            </el-input>
          </el-form-item>
          <el-form-item label-position='top' prop="password">
            <el-input size="default" show-password v-model="formData.password" type="password" class="password input" placeholder="登录密码">
            </el-input>
          </el-form-item>
        </el-form>
      </div>
      <el-button type="primary" class="login-to" @click="btnLogin">登录</el-button>
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
.get-ingo .content{
  margin: 0 auto;
  width: 300px;
  justify-content: center;
}
.get-ingo .username{
  background: url(/login/login-input.png) no-repeat, url(/login/login-user.png) no-repeat 10px center;
  background-size: 100% 100%, 20px;
}
.get-ingo .input{
  margin: 20px 0;
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