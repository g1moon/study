const express = require('express');
const app = express();
const config = require('./config/key');
const bodyParser = require('body-parser');
const {User} = require('./models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
//application/x-www-form-urlencoded //application/json
app.use(bodyParser.urlencoded( {extended: true}))
app.use(bodyParser.json());


//mongoose
const mongoose = require('mongoose');
mongoose.connect(config.mongoURI, {
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(() => console.log('MongoDB Connected...'))
    .catch(err => console.log(err))

//root
app.get('/', (req, res) => res.send('Hello World!~~ '));

//register //무조건 send를 해줘야하는든
app.post('/api/users/register', (req, res) => {

    const user = new User(req.body); //json 입력으로 들어감

    //save
    user.save((err, userInfo) => {
        if (err) return res.json({success: false, err});
        return res.json({success: true});
    });
});



//login
app.post('/api/users/login', (req, res) => {
    //요청된 이메일 찾고 ->
    User.findOne({email: req.body.email}, (err, matchedUser) => {
        if (!matchedUser) {
            return res.json({loginSucces : false, message : '등록된 이메일이 아닙니다.'})
        }
        //이메일 맞은 사람이 오는데 -> 비밀번호 맞는지 확인
        matchedUser.checkPassword(req.body.password, (err, isRightPassword) => {
            if (!isRightPassword) {
                res.json({loginSucces: false, message: '비밀번호가 틀렸습니다.'})
            }
            //비밀번호 맞아 그럼 -> 토큰 생성하고 등록해주자
            matchedUser.generateToken((err, matchedUser) => {
                if (err) {
                    return res.status(400).send(err);
                }

                //토큰 줫으니까 토큰 쿠키에 저장해주기
                res.cookie('x_auth', matchedUser.token)
                    .status(200)
                    .json({ loginSucces:true, userId: matchedUser._id}) //성공과 아이디
            });
        });
    });
});

//auth role0 -> user, !0 -> 관리자
// role 1 어드민    role 2 특정 부서 어드민
// role 0 -> 일반유저   role 0이 아니면  관리자
const {auth} = require('./middleware/auth');
app.get('/api/users/auth', auth, (req, res) => {
    //여기 까지 미들웨어를 통과해 왔다는 얘기는  Authentication 이 True 라는 말.
    res.status(200).json({
        _id: req.user._id,
        isAdmin: req.user.role === 0 ? false : true,
        isAuth: true,
        email: req.user.email,
        name: req.user.name,
        lastname: req.user.lastname,
        role: req.user.role,
        image: req.user.image
    })
})

//logout은 -> 그냥 아이디값 찾아서 -> 토큰값을 비워
app.get('/api/users/logout', auth, (req, res) => {

    User.findOneAndUpdate({"_id": req.user._id},
        {token: ''},
        (err, user) => {
            if (err) {
                return res.json({success: false, err});
            } else {
                return res.status(200).json({success: true,});
            }
        });
});

//listener
const port = 5000;
app.listen(port, () => console.log('hello!!!!'));