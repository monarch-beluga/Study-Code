const express = require("express");
const cors = require('cors');
const bodyParser = require('body-parser');
const routes = require('./router/index')

const app = express();
app.use(cors())
app.use(bodyParser.json())
routes(app)

app.listen(3000, function(){
    console.log("服务已启动.....")
})



