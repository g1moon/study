//이 안에서 인증처리를 진행할 것
const {User} = require('../models/User');
let auth = (req, res, next) => {
    //인증 처리를 하는 곳

    //클라이언트 쿠키에서 토큰을 가져온다(cookie parser)
    let token = req.cookies.x_auth;
    //토큰을 디코드하고 -> 유저를 찾는다(user 모델에서 메서드를 만든다)
    User.findByToken(token, (err, user) => {
        if (err) throw err;
        if (!user) return res.json({isAuth: false, error: ture});

        //app.get에서 사용할 수 있게 -> 라우터까지 갔다면 -> 성공
       req.token = token;
        req.user = user;
        next(); //여기 미들웨어를 탈출시켜주고 -> 라우트 부분으로 감 index의
    });

    //유저가 있으면 인증 0kay
    //유저가 없으면 인증 No

};

module.exports = {auth};
