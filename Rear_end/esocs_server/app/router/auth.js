const express = require("express")
const router = express.Router()
const {mysqlQuery, mysqlExecute} = require("../config/db")

// 登录
router.post("/login", async function(req, res){

    const data = req.body
    console.log(data)
    let sql = "SELECT * FROM `users` WHERE `name`=? AND `permissions`=?"
    let sql_list = [data.name, data.permissions]
    const rows = await mysqlQuery(sql, sql_list)
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
        // await mysqlExecute("UPDATE `users` SET `token`=REPLACE(UUID(), '-', '') WHERE `id`=?", [rows[0].id])
        const token = await mysqlQuery("SELECT id, token FROM `users` WHERE `id`=?", [rows[0].id])
        res.send({
            status: 200,
            message: "登录成功",
            token: token[0].token + '.' + token[0].id
        })
    }
})

router.get("/verify", async function(req, res){

    const auth_token = req.headers.authorization.split(' ')[1]
    const id = auth_token.split('.')[1]
    const token = auth_token.split('.')[0]

    let sql = "SELECT * FROM `users` WHERE `id`=?"
    let sql_list = [id]
    const user = await mysqlQuery(sql, sql_list)
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
            data: {
                'name': user[0].name,
                "permissions": user[0].permissions
            }
        })
    }
})

module.exports = router

