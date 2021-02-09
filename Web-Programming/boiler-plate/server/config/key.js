//key.js에서 NODE_ENV에 따라 다르게 exports하게 ->
//index.js -> const config = require('./config/key')
if (process.env.NODE_ENV === 'production') {
    module.exports = require('./prod');
} else {
    module.exports = require('./dev');
}