//이 안에서 인증처리를 진행할 것

const {User} = require('../models/User');

let auth = (req, res, next) => {
    //인증처리 -> 클라이언트 쿠키에 저장되어있는 토큰을 가져옴
    let token = req.cookie.x_auth;

    //토큰을 디코드하고 -> 유저 찾음
    User.findUserByToken(token, (err, user) => {
        if (err) {
            throw err;
        }
        if (!user) {
            return res.json({isAuth : false, errror : true})
        }

        // /api/users/auth 에서 req에서 쓰려고
        req.token = token;
        req.user = user;
        next(); //app.get으로 ->
    });
};

module.exports = {auth};