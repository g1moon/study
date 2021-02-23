import React from 'react';
import {useDispatch} from "react-redux";
import {useState} from "react/cjs/react.production.min";
import { registerUser } from '../../../_actions/user_action';

function RegisterPage() {
    const dispatch = useDispatch();

    const [Email, setEmail] = useState('');
    const [Password, setPassword] = useState('');
    const [Name, setName] = useState('');
    const [ConfirmPassword, setConfirmPassword] = useState('');


/// input event handler
    function onEmailHandler(e) {
        setEmail(e.target.value);
    }

    function onNameHandler(e) {
        setEmail(e.target.value);
    }

    function onPasswordHandler(e) {
        setEmail(e.target.value);
    }

    function onConfirmPasswordHandler(e) {
        setEmail(e.target.value);
    }

// submit event handler
    //submit을 하면 비밀번호 채크하고 -> body에 넣어
    function onSubmitHandler(e) {
        e.preventDefault();

        if (Password !== ConfirmPassword) {
            return alert('check your password')
        }

        let body = {
            email : Email,
            name : Name,
            password : Password
        }

        dispatch(registerUser(body));


    }

    return (
        <div style={{
            display: 'flex', justifyContent: 'center', alignItems: 'center'
            , width: '100%', height: '100vh'
        }}>
            <form style={{ display: 'flex', flexDirection: 'column' }}
                  onSubmit={onSubmitHandler}
            >
                <label>Email</label>
                <input type="email" value={Email} onChange={onEmailHandler} />

                <label>Name</label>
                <input type="text" value={Name} onChange={onNameHandler} />

                <label>Password</label>
                <input type="password" value={Password} onChange={onPasswordHandler} />

                <label>Confirm Password</label>
                <input type="password" value={ConfirmPassword} onChange={onConfirmPasswordHandler} />

                <br />
                <button type="submit">
                    회원 가입
                </button>
            </form>
        </div>
    )
}

export default RegisterPage;