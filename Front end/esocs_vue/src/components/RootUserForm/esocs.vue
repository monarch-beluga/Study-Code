<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";

const firmName = ref("")
const name = ref("")
const cas = ref("")

const dataPageFrom = ref({
  currPage: 1,
  pageSize: 10,
  total: 0
})

const formRef = ref()

const dataForm = ref({
  city: null,
  firmName: null,
  productName: null,
  useLink: null,
  name: null,
  cas: null,
  concentration: null,
  usage: null,
  usageNet: null,
  unit: null,
  type: null,
  id: null
})

const tableData = ref()
const dialogName = ref("新增企业")
const dialogFormVisible = ref(false)
const optionType = ref("add")
const formLabelWidth = ref("100px")

function closeDataForm(){
  dataForm.value.city = null
  dataForm.value.firmName = null
  dataForm.value.productName = null
  dataForm.value.useLink = null
  dataForm.value.name = null
  dataForm.value.cas = null
  dataForm.value.concentration = null
  dataForm.value.usage = null
  dataForm.value.usageNet = null
  dataForm.value.unit = null
  dataForm.value.type = null
}

function addData(){
  optionType.value = "add"
  dialogName.value = "新增化学物质信息"
  dialogFormVisible.value = true
}

function updateData(row){
  optionType.value = "update"
  dialogName.value = "编辑化学物质信息"
  dialogFormVisible.value = true

  dataForm.value.city = row.city
  dataForm.value.firmName = row.firmName
  dataForm.value.productName = row.productName
  dataForm.value.useLink = row.useLink
  dataForm.value.name = row.name
  dataForm.value.cas = row.cas
  dataForm.value.concentration = row.concentration
  dataForm.value.usage = row.usage
  dataForm.value.unit = row.unit
  dataForm.value.type = row.type
  dataForm.value.id = row.id
}

async function deleteData(row){
  const baseURL = import.meta.env.VITE_API_BASEURL;
  try {
    const res = await axios.post(baseURL + '/esocs/delete', {id: row.id})
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
    dataForm.value.usageNet = dataForm.value.usage * dataForm.value.concentration
    if (optionType.value === 'add'){
      const res = await axios.post( baseURL + `/esocs/add`, dataForm.value)
      let currPage = Math.trunc((dataPageFrom.value.total + 1) / dataPageFrom.value.pageSize) + 1
      await handleCurrentChange(currPage)
      ElMessage({
        message: res.data.message,
        type: 'success',
        duration: 1000
      })
    }
    else{
      const res = await axios.post( baseURL + `/esocs/update`, dataForm.value)
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
  let url = baseURL + `/esocs/export`
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
  let url = baseURL + `/esocs/query?page=${dataPageFrom.value.currPage}&pageSize=${dataPageFrom.value.pageSize}`
  if (firmName.value){
    url += `&firmName=${firmName.value}`
  }
  if (name.value){
    url += `&name=${name.value}`
  }
  if (cas.value){
    url += `&cas=${cas.value}`
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

async function handleNameChange() {
  if(dataForm.value.name !== ''){
    const baseURL = import.meta.env.VITE_API_BASEURL;
    const url = baseURL + `/csl/query?name=${dataForm.value.name}`
    try{
      const res = await axios.get(url)
      if (res.data.status === 200){
        dataForm.value.cas = res.data.data.cas
        dataForm.value.type = res.data.data.type
      }
      else{
        ElMessage({
          message: res.data.message,
          type: 'info',
          duration: 3000
        })
      }
    }catch(err){
      ElMessage({
        message: err,
        type: 'error',
        duration: 3000
      })
    }
  }
}

async function handleCasChange() {
  if(dataForm.value.cas !== ''){
    const baseURL = import.meta.env.VITE_API_BASEURL;
    const url = baseURL + `/csl/query?cas=${dataForm.value.cas}`
    try{
      const res = await axios.get(url)
      if (res.data.status === 200){
        dataForm.value.name = res.data.data.name
        dataForm.value.type = res.data.data.type
      }
      else{
        ElMessage({
          message: res.data.message,
          type: 'info',
          duration: 3000
        })
      }
    }catch(err){
      ElMessage({
        message: err,
        type: 'error',
        duration: 3000
      })
    }
  }
}

onMounted(() => {
  queryData()
})

</script>

<template>
  <el-form class="scratch" :inline="true">
    <el-form-item label="单位名称 : ">
      <el-input v-model="firmName"></el-input>
    </el-form-item>
    <el-form-item label="化学物质名称 : ">
      <el-input v-model="name"></el-input>
    </el-form-item>
    <el-form-item label="CAS号 : ">
      <el-input v-model="cas"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="queryData">查询</el-button>
      <el-button type="primary" @click="addData">新增</el-button>
      <el-button type="primary" @click="exportData">导出</el-button>
    </el-form-item>
  </el-form>

  <el-table :data="tableData" style="width: 100%" class="table">
    <el-table-column prop="id" label="序号"></el-table-column>
    <el-table-column prop="city" label="设区市"></el-table-column>
    <el-table-column prop="firmName" label="单位名称"></el-table-column>
    <el-table-column prop="productName" label="产品名称"></el-table-column>
    <el-table-column prop="useLink" label="使用环节"></el-table-column>
    <el-table-column prop="name" label="MSDS名称"></el-table-column>
    <el-table-column prop="cas" label="CAS号"></el-table-column>
    <el-table-column prop="concentration" label="浓度"></el-table-column>
    <el-table-column prop="usage" label="使用量"></el-table-column>
    <el-table-column prop="usageNet" label="使用量(折纯)"></el-table-column>
    <el-table-column prop="unit" label="单位"></el-table-column>
    <el-table-column prop="type" label="物质分类"></el-table-column>

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
    <el-form ref="formRef" :model="dataForm" label-width="auto" >
      <el-form-item label="设区市" :label-width="formLabelWidth">
        <el-input v-model="dataForm.city" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单位名称" :label-width="formLabelWidth">
        <el-input v-model="dataForm.firmName" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="产品名称" :label-width="formLabelWidth">
        <el-input v-model="dataForm.productName" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="使用环节" :label-width="formLabelWidth">
        <el-input v-model="dataForm.useLink" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="MSDS名称" :label-width="formLabelWidth" @change="handleNameChange">
        <el-input v-model="dataForm.name" autocomplete="off" placeholder="输入物质名称自动查询CAS号和物质类型"></el-input>
      </el-form-item>
      <el-form-item label="CAS" :label-width="formLabelWidth" @change="handleCasChange">
        <el-input v-model="dataForm.cas" autocomplete="off" placeholder="输入CAS号自动查询物质名称和物质类型"></el-input>
      </el-form-item>
      <el-form-item label="浓度" :label-width="formLabelWidth">
        <el-input v-model="dataForm.concentration" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="使用量" :label-width="formLabelWidth">
        <el-input v-model="dataForm.usage" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单位" :label-width="formLabelWidth">
        <el-select v-model="dataForm.unit" placeholder="选择单位">
          <el-option label="KG" value="KG" />
          <el-option label="L" value="L" />
        </el-select>
      </el-form-item>
      <el-form-item label="物质分类" :label-width="formLabelWidth" prop="type">
        <el-input v-model="dataForm.type" autocomplete="off"></el-input>
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