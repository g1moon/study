import React, {useState} from 'react';

const EventPractice = () => {
    const [username, setUsername] = useState('');
    const [msg, setMsg] = useState('');

    //-----------------이벤트 처리 할 함수 4개-----------------
    const onChangeUsername = e => setUsername(e.target.value);
    const onChangeMsg = e => setMsg(e.target.value);

    const onClick = () => {
        alert(username + ':' + msg);
        setUsername('');
        setMsg('');
    };
    //엔터치면 -> onClick과 같은 효과 (엔터하니면 그냥 흘러감)
    const onKeyPress = e => {
        if (e.key === 'Enter') {
            onClick();
        }
    };
    //------------------------------------------------------
    return (
        <div>
            <h1>이벤트 연습</h1>
            <input
                type='text'
                name='username'
                placeholder='사용자명'
                value={username}
                onChange={onChangeUsername}
            />
            <input
                type='text'
                name='msg'
                placeholder='msg: 아무거나 입력하세요'
                value={msg}
                onChange={onChangeMsg}
                onKeyPress={onKeyPress}
            />

            <button onClick = {onClick}>확인</button>
        </div>
    );
};
export default EventPractice;