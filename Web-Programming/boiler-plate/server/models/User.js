const mongoose = require('mongoose');
const userSchema = mongoose.Schema({
    name: {
        type: String,
        maxlength: 50
    },
    email: {
        type: String,
        trim: true,
        unique: 1
    },
    password: {
        type: String,
        minlength: 5
    },
    lastname: {
        type: String,
        maxlength: 50
    },
    role: {
        type: Number,
        default: 0
    },
    image: String,
    token: {
        type: String
    },
    tokenExp: {
        type: Number
    }
});

//저장하기 전 암호화한다
const bcrypt = require('bcrypt');
const saltRounds = 10;

userSchema.pre('save', function (next) {
    var user = this;
    if (user.isModified('password')) {
        //비밀번호를 암호화 시킨다.
        bcrypt.genSalt(saltRounds, function (err, salt) {
            if (err) return next(err)

            bcrypt.hash(user.password, salt, function (err, hash) {
                if (err) return next(err)
                user.password = hash
                next()
            })
        })
    } else {
        next()
    }
})

//checkPasswor(req.body.password, (err, isRightPassword) =>
userSchema.methods.checkPassword = function (plainPassword, cb) {
    //plainPassword(입력한 거) this.password(저장되어있는 거)
    bcrypt.compare(plainPassword, this.password, function (err, isRightPassword) {
        if (err) {
            console.log(err);
            return cb(err);
        } else {
            // console.log('isRightPassword:', isRightPassword);  //true
            return cb(null, isRightPassword);
        }
    });
};

//generateToken( (err, matchedUser) => )
const jwt = require('jsonwebtoken');

userSchema.methods.generateToken = function (cb) {
    console.log(this); //this = {role :0, _id:, name, email, password .....
    let matchedUser = this;
    //토큰을 생성하고(matchedUser._id + 'secretToken' = token
    const token = jwt.sign(matchedUser._id.toHexString(), 'secretToken');
    matchedUser.token = token;
    matchedUser.save(function (err, matchedUser) {
        if (err) {
            return cb(err);
        } else {
            console.log('===================')
            console.log(matchedUser);
            cb(null, matchedUser);
        }
    });
};

//User.findByToken(token, (err, user) => {
userSchema.statics.findUserByToken = function (token, cb) {
    // console.log(this); /this = {role :0, _id:, name, email, password .....
    let user = this;
    //._id + 'secretToken' = token -> token과 secretToekn으로 id 찾기
    //토큰을 디코드
    jwt.verify(token, 'scretToken', function (err, decodedId) {
        //유저 아이디를 이용해 유저를 찾고 -> 클라이언트에서 가져온 토큰과 DB토큰이 일치하는지 확인
        //토큰을 이용해 -> 디코드하고 -> 디코드한 값으로 아이디를 찾아서 -> 그 유저 보냄(있으면 isAuth)
        user.findOne({"_id": decodedId}, function (err, user) {
            if(err) return cb(err);
            cb(null, user);
        });
    });
};

//User가 모델이 된다.
const User = mongoose.model('User', userSchema);
//
module.exports = {User};

