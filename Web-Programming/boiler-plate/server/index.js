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
    //디비에서 요청한 Email 찾고
    //console.log(req.body); //{ email: 'goo@naver.com', password: '12345667' }

    //디비에서 요청한 이메일이 있다면 -> 비밀번호 같은지
    let login = false;
    User.findOne({email: req.body.email}, function (err, matchedItem) {
        if (matchedItem) {
            // console.log('matchedItem.password: ',  (matchedItem.password)); //$2b$10$fmkK/a8/wL12ywC1rcmApOWfIiJCEumj8Ex2jK3HW7DDO/q26seS6
            // console.log('req.body.password: ',  (req.body.password)); //pooky12345
            bcrypt.compare(req.body.password, matchedItem.password, function (err, isMatch) {
                if (!isMatch) {
                    return res.json({loginSuccess: false, message: '비밀번호가 틀렸습니다'}); //
                }
            });
        } else {
            return res.json({loginSuccess: false, message: '이메일이 존재하지 않습니다'})
        }

        //여기까지 오면 성공 -> 토큰 생성하고 토큰 저장
        //user._id + '' = token
        // console.log((req.body)); //{ email: 'pooky@naver.com', password: 'pooky12345' }
        const token = jwt.sign(matchedItem._id.toHexString(), 'secretToken'); //토큰만들고
        matchedItem.token = token; //토큰 저장해주고
        matchedItem.save((err, saveResult) => {
            console.log('save');
            if (err) {
                return res.status(400).send(err);
            }
            //토큰을 저장하는데 쿠키에
            res.cookie('x_auth', user.token)
                .status(200)
                .json({loginSucces : true, userId: matchedItem._id})

        });
        return res.json({loginSuccess : true, message: '성공 2!!'})

    });
    //같다면 token생성
});



//listener
const port = 5000;
app.listen(port, () => console.log('hello!!!!'));