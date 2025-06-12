<script setup>
import axios from "axios";
import {ref} from "vue";
import {useRouter} from "vue-router";
import {storage} from "../store/storage.js"
import {Lock, User} from "@element-plus/icons-vue";

const currTab = ref('ordinary')
const formRef = ref()
const tabs = {
  'root': '机构用户',
  "ordinary": "企业用户"
}

const formData = ref({
  name: "",
  pwd: '',
  permissions: 'ordinary'
})

const rules = {
  name: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ],
  pwd: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ]
}

const uRouter = useRouter()

const loginFun = async function() {
  const baseURL = import.meta.env.VITE_API_BASEURL;
  try {
    const res = await axios.post(baseURL + '/auth/login', formData.value);
    if (res.data.status === 200) {
      ElMessage({
        message: res.data.message,
        type: 'success',
        duration: 1000
      })
      storage.set("token", res.data.token);
      if (formData.value.permissions === 'root')
        await uRouter.push('/form/root')
      else
        await uRouter.push('/form/user?name=' + formData.value.name)
    }
    else{
      ElMessage({
        message: res.data.message,
        type: 'error',
        duration: 1000
      })
    }
  }catch(err) {
    ElMessage({
      message: err,
      type: 'error',
      duration: 1000
    })
  }
}

const btnSubmit = async function () {
  try{
    await formRef.value.validate()
    await loginFun()
  }
  catch (err){
    ElMessage.error('用户账号密码为空');
  }
}
</script>

<template>
<div class="body">
  <nav class="navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="javascript:;">江西省化学品生产使用环境信息管理系统--线路板行业新污染物治理试点</a>
    </div>
    <ul class="navbar-nav">
      <li><a href="/hxp/user/regedit">注册用户</a></li>
      <li><a href="/hxp/user/forgetpassword">忘记密码</a></li>
    </ul>
  </nav>
  <div class="main">
    <div class="maininleft">
    </div>
    <div class="mainin">
      <div class="lg_user_type">
        <ul class="g_clearfix">
          <li v-for="(tab, index) in tabs"
              :id="index"
              style="cursor: pointer;"
              :class="currTab === index ? 'cur' : ''"
              @click="currTab=index;formData.permissions=index"
          >
            {{tab}}
          </li>
          </ul>
      </div>
      <div class="mainin1">
        <el-form :model="formData"  :rules="rules" ref="formRef">
          <el-form-item label="用户名：" label-position='top' prop="name">
            <el-input size="large" clearable v-model="formData.name" class="loginuser" placeholder="登录名">
              <template #prefix>
                <el-icon><User /></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item label="密码：" label-position='top' prop="pwd">
            <el-input size="large" show-password v-model="formData.pwd" type="password" class="loginpwd" placeholder="登录密码">
              <template #prefix>
                <el-icon><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
        </el-form>
        <el-button class="tijiao" @click="btnSubmit">登录</el-button>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
.body {
  /* background: #006eb0 url(./index/lgbg.png) center top no-repeat; */
  clear: both;
  margin: 0 auto;
  width: 100%;
  min-width: 960px;
  height: 100vh;
  min-height: 720px;
  /* background-color: #c0c0c0; */
  background-color: rgb(57, 103, 185);
  /* background-image: url(./images/loginbg3.png); */
  background-image: none;
  background-position: 80% center;
  background-repeat: no-repeat;
}
nav.navbar {
  background-color: rgb(242, 243, 244) !important;
  /* background-image: url(./images/nav_bg.jpg); */
  background-position: center center;
  color: #efefef;
  height: 56px;
  border-bottom: 2px solid rgb(214 223 223 / 18%);
  box-shadow: 0px 20px 20px -20px #5E5E5E;
  display: flex;
}
nav.navbar .navbar-header {
  line-height: 56px;
  font-size: 24px;
  flex: auto;
  padding-left: 8px;
}
nav.navbar .navbar-header a, nav.navbar .navbar-nav a {
  color: #0f0f0f;
}
nav.navbar .navbar-header a:hover{
  color: #00b2ff;
}
nav.navbar .navbar-nav a:hover{
  color: #00b2ff;
}
nav.navbar .navbar-nav {
  display: flex
;
  text-align: right;
  line-height: 36px;
  font-size: 14px;
  float: right;
  background-color: transparent;
}
nav.navbar .navbar-nav li {
  line-height: 56px;
  margin-right: 8px;
  display: inline-block;
}
nav.navbar .navbar-header a, nav.navbar .navbar-nav a {
  color: #0f0f0f;
}
.main {
  margin: 0 auto;
  width: 1200px;
  overflow: hidden;
  background-position: center center;
  display: flex
;
}
.maininleft {
  width: 600px;
  height: 409px;
  margin-top: 80px;
  background-image: linear-gradient(0deg, rgb(57, 103, 185) 0%, transparent 30%),
  linear-gradient(90deg, rgb(57, 103, 185) 0%, transparent 30%),
  linear-gradient(180deg, rgb(57, 103, 185) 0%, transparent 30%),
  linear-gradient(270deg, rgb(57, 103, 185) 0%, transparent 30%),url('/images/login_img1.png');
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.lg_user_type ul li.cur {
  color: #0068b7;
  border-bottom: 1px solid #fff;
  background-color: #fff;
}
.mainin {
  margin: 0 auto;
  width: 320px;
  overflow: hidden;
  clear: both;
  padding-top: 80px;
}
.main .lg_user_type {
  color: #000;
  font-family: Microsoft YaHei, \\5FAE\8F6F\96C5\9ED1, Verdana, Arial, Helvetica, SimSun, \\5B8B\4F53;
  font-size: 14px;
  border: 0;
  margin: 0;
  padding: 0;
}
.lg_user_type ul {
  margin: 0;
  padding: 0;
  display: flex;
}
.lg_user_type ul li {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  cursor: pointer;
  font-size: 18px;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  color: #000;
  text-align: center;
  height: 47px;
  line-height: 47px;
  border-bottom: 1px solid #e5ebed;
  background-color: #f3f6f8;
}
.lg_user_type ul li:first-child {
  border-right: 1px solid #e5ebed;
  border-radius: 5px 0 0 0;
}
.lg_user_type ul li:last-child {
  border-right: 1px solid #e5ebed;
  border-radius: 0 5px 0 0;
}
.mainin1 {
  margin: 0 auto 0 auto;
  width: 320px;
  height: 320px;
  background-color: rgb(255, 255, 255);
  border-radius: 0 0 2px 2px;
}
.mainin1 .el-form {
  margin: 19px 0 0 19px;
  float: left;
  padding: 0;
  overflow: hidden;
  width: 280px;
}
.mainin1 .el-form .el-form-item {
  float: left;
  width: 100%;
  overflow: hidden;
  padding-bottom: 16px;
  clear: both;
  font-family: "Microsoft YaHei";
  font-size: 14px;
  line-height: 37px;
}
.el-input :deep(.el-input__wrapper) {
  background-color: #ecf5fa !important;
}

.tijiao {
  display: block;
  margin: 12px auto;
  height: 42px;
  width: 190px;
  border: none;
  background: url(/images/dl.png) no-repeat;
  font-weight: bold;
  text-align: center;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
}

</style>