const express = require("express")
const router = express.Router()
const {mysqlQuery, mysqlExecute} = require("../config/db")
const ExcelJS = require('exceljs');

router.post("/add", async function (req, res) {
    const {city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type} = req.body
    let sql = "INSERT INTO `esocs` (`city`, `firmName`, `productName`, `useLink`, `name`,`cas`,`concentration`,`usage`,`usageNet`,`unit`,`type`) VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)"
    let sql_list = [city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据添加成功",
    })
})



router.post("/update", async function (req, res) {
    const {city, firmName, productName, useLink, name,cas,concentration,usage, usageNet,unit,type, id} = req.body
    
    let sql = "UPDATE `esocs` SET `city`=?,`firmName`=?,`productName`=?,`useLink`=?,`name`=?,`cas`=?,`concentration`=?,`usage`=?,`usageNet`=?,`unit`=?,`type`=? WHERE id = ?"
    let sql_list = [city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type,id]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据修改成功",
    })
})



router.post("/delete", async function (req, res) {
    const {id} = req.body
    let sql = "DELETE FROM `esocs` WHERE id = ?"
    let sql_list = [id]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据删除成功",
    })
})

router.get("/query", async function (req, res) {
    let {page, pageSize, firmName, name, cas} = req.query

    let sql = "SELECT * FROM `esocs`"
    let sql_where = ""
    let sql_count = "SELECT count(*) as count FROM `esocs`"
    let sql_list = []

    let offset = page * pageSize - pageSize
    if (firmName){
        firmName = '%' + firmName + '%'
        sql_list.push(firmName)
        sql_where += sql_where?" AND `firmName` like ?":"`firmName` like ?"
    }
    if (name){
        name = '%' + name + '%'
        sql_list.push(name)
        sql_where += sql_where?" AND `name` like ?":"`name` like ?"
    }
    if (cas){
        cas = '%' + cas + '%'
        sql_list.push(cas)
        sql_where += sql_where?" AND `cas` like ?":"`cas` like ?"
    }
    sql += sql_where?"WHERE "+sql_where+" LIMIT ?,?":" LIMIT ?,?"
    sql_count += sql_where?"WHERE "+sql_where:""
    const count = await mysqlQuery(sql_count, sql_list)
    sql_list.push(offset)
    sql_list.push(parseInt(pageSize))
    const rows = await mysqlQuery(sql, sql_list)
    res.send({
        message: "查询成功",
        data: rows,
        total: count[0].count
    })
})

router.get("/export", async function (req, res) {
    
    let sql = "SELECT `id` as '序号',`city` as '设区市',`firmName` as '单位名称',`productName` as '产品名称',`useLink` as '使用环节',`name` as 'MSDS名称',`cas` as 'CAS',`concentration` as '浓度',`usage` as '使用量',`usageNet` as '使用量(折纯)',`unit` as '单位',`type` as '物质分类' FROM `esocs`"
    const rows = await mysqlQuery(sql, [])

    // 创建Excel工作簿
    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet('Data');
    
    // 添加表头
    if (rows.length > 0) {
      const headers = Object.keys(rows[0]);
      worksheet.addRow(headers);
      
      // 添加数据行
      rows.forEach(row => {
        worksheet.addRow(Object.values(row));
      });
    }
    
    // 设置响应头
    res.setHeader(
      'Content-Type',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    );
    res.setHeader(
      'Content-Disposition',
      'attachment; filename="exported_data.xlsx"'
    );
    
    // 发送Excel文件
    await workbook.xlsx.write(res);
    res.end();
    
})

module.exports = router
