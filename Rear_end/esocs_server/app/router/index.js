const authRoute = require("./auth")
const enterpriseRoute = require('./enterprise')
const esoceRoute = require('./esocs')
const cslRoute = require('./csl')

module.exports = app => {
    app.use('/auth', authRoute)
    app.use("/enterprise", enterpriseRoute)
    app.use("/esocs", esoceRoute)
    app.use("/csl", cslRoute)
}

