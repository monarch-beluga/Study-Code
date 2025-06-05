const mysql = require('mysql2/promise');

const db = {
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: '123456',
    database: 'esocs'
}

const pool = mysql.createPool(db)
const mysqlQuery = async function (sql, sql_list){
    const conn = await pool.getConnection()
    const [rows] = await conn.query(sql, sql_list)
    conn.release()
    return rows
}

const mysqlExecute = async function (sql, sql_list) {
    const conn = await pool.getConnection()
    const [result] = await conn.execute(sql, sql_list)
    conn.release()
    return result
}

module.exports = {mysqlQuery, mysqlExecute}
