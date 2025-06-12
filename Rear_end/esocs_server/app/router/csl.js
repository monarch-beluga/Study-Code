const express = require("express")
const router = express.Router()
const {mysqlQuery, mysqlExecute} = require("../config/db")

router.get("/query", async function (req, res) {
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
    const rows = await mysqlQuery(sql, sql_list)
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

module.exports = router
