const Router = require('koa-router');
const posts = require('./posts');

const api = new Router();

//api라우터에 posts라우터 연결
api.use('/posts', posts.routes());

//라우터 내보내기
module.exports = api;
