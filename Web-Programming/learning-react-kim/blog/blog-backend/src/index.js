const Koa = require('koa');
const Router = require('koa-router');
const bodyParser = require('koa-bodyparser');

const api = require('./api'); //적용전

const app = new Koa()
const router = new Router();

router.use('/api', api.routes()); //api 라우트 적용(use)

//라우터 적용 전에 bodyParser
app.use(bodyParser());

//app 인스턴스에 라우터 적용
app.use(router.routes()).use(router.allowedMethods());

app.listen(4000, () => {
    console.log('Listening to port 4000');
});