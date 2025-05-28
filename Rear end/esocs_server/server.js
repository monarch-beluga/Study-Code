const express = require("express");
const cors = require('cors');
const mysql = require('mysql2/promise');
const bodyParser = require('body-parser');
const ExcelJS = require('exceljs');

const app = express();
app.use(cors())
app.use(bodyParser.json())
const db = {
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: '123456',
    database: 'esocs'
}
const pool = mysql.createPool(db)

app.post("/enterprise/add", async function (req, res) {
    const {name, city, county, type} = req.body
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "INSERT INTO `enterprise` (name, city, county, type) VALUES (?, ?, ?, ?)",
        [name, city, county, type]
    );
    res.send({
        message: "数据添加成功",
    })
    conn.release()
})

app.post("/esocs/add", async function (req, res) {
    const {city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type} = req.body
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "INSERT INTO `esocs` (`city`, `firmName`, `productName`, `useLink`, `name`,`cas`,`concentration`,`usage`,`usageNet`,`unit`,`type`) VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)",
        [city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type]
    );
    res.send({
        message: "数据添加成功",
    })
    conn.release()
})

app.post("/enterprise/update", async function (req, res) {
    const {name, city, county, type, id} = req.body
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "UPDATE `enterprise` SET name = ?, city = ?, county = ?, type = ? WHERE id = ?",
        [name, city, county, type, id]
    );
    res.send({
        message: "数据修改成功",
    })
    conn.release()
})

app.post("/esocs/update", async function (req, res) {
    const {city, firmName, productName, useLink, name,cas,concentration,usage, usageNet,unit,type, id} = req.body
    
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "UPDATE `esocs` SET `city`=?,`firmName`=?,`productName`=?,`useLink`=?,`name`=?,`cas`=?,`concentration`=?,`usage`=?,`usageNet`=?,`unit`=?,`type`=? WHERE id = ?",
        [city, firmName, productName, useLink, name,cas,concentration,usage,usageNet,unit,type,id]
    );
    res.send({
        message: "数据修改成功",
    })
    conn.release()
})

app.post("/enterprise/delete", async function (req, res) {
    const {id} = req.body
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "DELETE FROM `enterprise` WHERE id = ?",
        [id]
    );
    res.send({
        message: "数据删除成功",
    })
    conn.release()
})

app.post("/esocs/delete", async function (req, res) {
    const {id} = req.body
    const conn = await pool.getConnection()
    const [result] = await conn.execute(
        "DELETE FROM `esocs` WHERE id = ?",
        [id]
    );
    res.send({
        message: "数据删除成功",
    })
    conn.release()
})

app.get("/csl/query", async function (req, res) {
    const {name, cas} = req.query
    let sql = "SELECT * FROM `csl` "
    let sql_where = ""
    let sql_list = []
    let message_str = ""

    if (name){
        sql_where = "WHERE `name`=?"
        sql_list.push(name)
        message_str = "未找到该化学物质名称"
    }
    if (cas){
        sql_where = "WHERE `cas`=?"
        sql_list.push(cas)
        message_str = "未找到该化学物质CAS号"
    }
    sql += sql_where
    const conn = await pool.getConnection()
    const [rows] = await conn.query(sql, sql_list)
    conn.release()
    if (rows.length === 0){
        res.send({
            status: 404,
            message: message_str
        })
    }
    else{
        res.send({
            status: 200,
            message: "查找成功",
            data: rows[0]
        })
    }
})

app.get("/enterprise/query", async function (req, res) {
    let {page, pageSize, name} = req.query

    const conn = await pool.getConnection()

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
    const [count] = await conn.query(sql_count, sql_list)
    sql_list.push(offset)
    sql_list.push(parseInt(pageSize))
    const [rows] = await conn.query(sql, sql_list)
    res.send({
        message: "查询成功",
        data: rows,
        total: count[0].count
    })
    conn.release();
})

app.get("/enterprise/export", async function (req, res) {
    
    const conn = await pool.getConnection()
    let sql = "SELECT `id` as '序号',`city` as '所在市',`type` as '企业类型',`county` as '所在县、区',`name` as '企业名称' FROM `enterprise`"
    const [rows] = await conn.query(sql)

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
    conn.release()
    
})

app.get("/esocs/export", async function (req, res) {
    
    const conn = await pool.getConnection()
    let sql = "SELECT `id` as '序号',`city` as '设区市',`firmName` as '单位名称',`productName` as '产品名称',`useLink` as '使用环节',`name` as 'MSDS名称',`cas` as 'CAS',`concentration` as '浓度',`usage` as '使用量',`usageNet` as '使用量(折纯)',`unit` as '单位',`type` as '物质分类' FROM `esocs`"
    const [rows] = await conn.query(sql)

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
    conn.release()
    
})

app.get("/esocs/query", async function (req, res) {
    let {page, pageSize, firmName, name, cas} = req.query

    const conn = await pool.getConnection()

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
    const [count] = await conn.query(sql_count, sql_list)
    sql_list.push(offset)
    sql_list.push(parseInt(pageSize))
    const [rows] = await conn.query(sql, sql_list)
    res.send({
        message: "查询成功",
        data: rows,
        total: count[0].count
    })
    conn.release();
})

app.get("/auth/verify", async function(req, res){

    const auth_token = req.headers.authorization.split(' ')[1]
    const id = auth_token.split('.')[1]
    const token = auth_token.split('.')[0]

    const conn = await pool.getConnection()

    const [user] = conn.query("SELECT * FORM `users` WHERE `id`=?", [id])

    if (user.length === 0){
        res.send({
            status: "403",
            message: "用户错误"
        })
    }else if(user[0].token !== token){
        res.send({
            status: "404",
            message: "登录信息过期"
        })
    }else{
        res.send({
            status: 200,
            message: "验证通过",
            data: user[0].permissions
        })
    }

})

app.post("/auth/login", async function(req, res){

    const data = req.body

    if (!data.name || !data.pwd){
        return res.send({
            status: 402,
            message: "用户账号密码为空"
        })
    }

    const conn = await pool.getConnection()

    const [rows] = await conn.query("SELECT * FROM `users` WHERE `name`=? AND `permissions`=?", [data.name, data.permissions])
    if (rows.length === 0){
       res.send({
            status: 403,
            message: "未找到用户信息"
        })
    }
    else if (data.pwd!==rows[0].pwd){
        res.send({
            status: 404,
            message: "用户密码错误"
        })
    }
    else{
        const [result] = await conn.execute("UPDATE `users` SET `token`=REPLACE(UUID(), '-', '') WHERE `id`=?", [rows[0].id])
        const [token] = await conn.query("SELECT id, token FROM `users` WHERE `id`=?", [rows[0].id])
        res.send({
            status: 200,
            message: "登录成功",
            token: token[0].token + '.' + token[0].id
        })
    }
    conn.release()
})

app.listen(3000, function(){
    console.log("服务已启动.....")
})



