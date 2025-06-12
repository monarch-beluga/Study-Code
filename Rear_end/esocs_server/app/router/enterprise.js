const express = require("express")
const router = express.Router()
const {mysqlQuery, mysqlExecute} = require("../config/db")
const ExcelJS = require('exceljs');

router.post("/add", async function (req, res) {
    const {name, city, county, type} = req.body
    let sql = "INSERT INTO `enterprise` (name, city, county, type) VALUES (?, ?, ?, ?)"
    let sql_list = [name, city, county, type]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据添加成功",
    })
})

router.post("/update", async function (req, res) {
    const {name, city, county, type, id} = req.body
    let sql = "UPDATE `enterprise` SET name = ?, city = ?, county = ?, type = ? WHERE id = ?"
    let sql_list = [name, city, county, type, id]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据修改成功",
    })
})

router.post("/delete", async function (req, res) {
    const {id} = req.body
    let sql = "DELETE FROM `enterprise` WHERE id = ?"
    let sql_list = [id]
    const result = await mysqlExecute(sql, sql_list);
    res.send({
        message: "数据删除成功",
    })
})

router.get("/query", async function (req, res) {
    let {page, pageSize, name} = req.query

    let sql = "SELECT * FROM `enterprise`"
    let sql_where = ""
    let sql_count = "SELECT count(*) as count FROM `enterprise`"
    let sql_list = []

    let offset = page * pageSize - pageSize
    if (name){
        name = '%' + name + '%'
        sql_list.push(name)
        sql_where += sql_where?" AND `name` like ?":"`name` like ?"
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
    
    let sql = "SELECT `id` as '序号',`city` as '所在市',`type` as '企业类型',`county` as '所在县、区',`name` as '企业名称' FROM `enterprise`"
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
