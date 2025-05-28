<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import {ElMessage } from 'element-plus'

const name = ref("")

const dataPageFrom = ref({
  currPage: 1,
  pageSize: 10,
  total: 0,
})

const dataForm = ref({
  name: "",
  city: "",
  county: "",
  type: "",
  id: ""
})

const tableData = ref()
const dialogName = ref("新增企业")
const dialogFormVisible = ref(false)
const optionType = ref("add")
const formLabelWidth = ref("100px")
const formRef = ref()

const rules = {
  name: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ],
  city: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ],
  county: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ],
  type: [
    {required: true, message: "该项不能为空", trigger: 'blur'}
  ]
}

function closeDataForm(){
  dataForm.value.name = ""
  dataForm.value.city = ""
  dataForm.value.county = ""
  dataForm.value.type = ""
}

function addData(){
  optionType.value = "add"
  dialogName.value = "新增企业"
  dialogFormVisible.value = true
}

function updateData(row){
  optionType.value = "update"
  dialogName.value = "编辑企业"
  dialogFormVisible.value = true

  dataForm.value.name = row.name
  dataForm.value.city = row.city
  dataForm.value.county = row.county
  dataForm.value.type = row.type
  dataForm.value.id = row.id
}

async function deleteData(row){
  const baseURL = import.meta.env.VITE_API_BASEURL;
  try {
    const res = await axios.post(baseURL + '/enterprise/delete', {id: row.id})
    await queryData()
    ElMessage({
      message: res.data.message,
      type: 'success',
      duration: 1000
    })
  }catch(err){
    ElMessage({
      message: err,
      type: 'error',
      duration: 3000
    })
  }
}

async function saveData(){
  const baseURL = import.meta.env.VITE_API_BASEURL;
  try{
    if (optionType.value === 'add'){
      const res = await axios.post( baseURL + `/enterprise/add`, dataForm.value)
      const currPage = Math.trunc((dataPageFrom.value.total + 1) / dataPageFrom.value.pageSize) + 1
      await handleCurrentChange(currPage)
      ElMessage({
        message: res.data.message,
        type: 'success',
        duration: 1000
      })
    }
    else{
      const res = await axios.post( baseURL + `/enterprise/update`, dataForm.value)
      await queryData()
      ElMessage({
        message: res.data.message,
        type: 'success',
        duration: 1000
      })
    }
  }catch(err){
    ElMessage({
      message: err,
      type: 'error',
      duration: 3000
    })
  }
  dialogFormVisible.value = false
}

async function submitForm(){
  try{
    await formRef.value.validate()
    await saveData()
  }
  catch (err){
    ElMessage.error('请填写完整表单');
  }
}

async function exportData(){
  const baseURL = import.meta.env.VITE_API_BASEURL;
  let url = baseURL + `/enterprise/export`
  try{
    const res = await axios.get(url, {responseType: 'blob'})

    const downUrl = window.URL.createObjectURL(new Blob([res.data]))
    const link = document.createElement('a')
    link.href = downUrl
    link.setAttribute('download', 'exported_data.xlsx')
    document.body.appendChild(link)
    link.click()

    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  }catch(err){
    ElMessage.error("导出失败")
  }
}

async function queryData() {
  const baseURL = import.meta.env.VITE_API_BASEURL;
  let url = baseURL + `/enterprise/query?page=${dataPageFrom.value.currPage}&pageSize=${dataPageFrom.value.pageSize}`
  if (name.value){
    url += `&name=${name.value}`
  }
  try{
    const res = await axios.get( url)
    tableData.value = res.data.data
    dataPageFrom.value.total = res.data.total
  }catch(err){
    ElMessage({
      message: err,
      type: 'error',
      duration: 3000
    })
  }
}

async function handleSizeChange(r) {
  dataPageFrom.value.pageSize = r
  await queryData()
}
async function handleCurrentChange(r) {
  dataPageFrom.value.currPage = r
  await queryData()
}

onMounted(() => {
  queryData()
})

</script>

<template>
  <el-form class="scratch" :inline="true">
    <el-form-item label="企业名称 : ">
      <el-input v-model="name"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="queryData">查询</el-button>
      <el-button type="primary" @click="addData">新增</el-button>
      <el-button type="primary" @click="exportData">导出</el-button>
    </el-form-item>
  </el-form>

  <el-table :data="tableData" style="width: 100%" class="table">
    <el-table-column prop="id" label="序号"></el-table-column>
    <el-table-column prop="city" label="所在市"></el-table-column>
    <el-table-column prop="name" label="企业名称"></el-table-column>
    <el-table-column prop="county" label="所在县、区"></el-table-column>
    <el-table-column prop="type" label="企业类型"></el-table-column>

    <!-- “编辑”“删除”功能连接 -->
    <el-table-column label="操作">
      <template #default="scope">
        <el-button size="small" @click="updateData(scope.row)">编辑</el-button>
        <el-button size="small" type="danger" @click="deleteData(scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>

  <div class="page" style="padding: 20px;">
    <el-pagination
        size="small"
        background
        layout="total, sizes, prev, pager, next, jumper"
        :total="dataPageFrom.total"
        :page-sizes="[10, 20, 30 ,40]"
        :page-size="dataPageFrom.pageSize"
        :current-page="dataPageFrom.currPage"
        class="mt-4"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
    />
  </div>

  <el-dialog :title="dialogName" v-model="dialogFormVisible" @close="closeDataForm" width="450px">
    <el-form :model="dataForm" label-width="auto" :rules="rules" ref="formRef">
      <el-form-item label="企业名称" :label-width="formLabelWidth" prop="name">
        <el-input v-model="dataForm.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="企业类型" :label-width="formLabelWidth" prop="type">
        <el-input v-model="dataForm.type" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="所在市" :label-width="formLabelWidth" prop="city">
        <el-input v-model="dataForm.city" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="所在县、区" :label-width="formLabelWidth" prop="county">
        <el-input v-model="dataForm.county" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="submitForm">确 定</el-button>
    </div>
  </el-dialog>
</template>

<style scoped>
.scratch{
  display: flex;
  justify-content: center; /* 水平居中 */
  padding: 20px;
}
.table{
  display: flex;
  height: calc(100vh - 400px);
  justify-content: center; /* 水平居中 */
  margin: 30px;
}
.page{
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: flex-end; /* 垂直底部对齐 */
  margin: 30px;
}
.dialog-footer{
  display: flex;
  justify-content: right;
  align-items: flex-end;
  padding: 10px;
}
</style>