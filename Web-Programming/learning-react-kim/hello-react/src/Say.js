import React, {useState} from "react";

const Say = () => {
    //useState 함수의 인자에 초깃값을 넣어준다.(클래스형 컴포넌트와 달리 자유 타입)
    const [msg, setMessage] = useState('');
    const onClickEnter = () => setMessage('안녕하세요');
    const onClickLeave = () => setMessage('안녕히가세요');

    return (
        <div>
            <button onClick={onClickEnter}>입장</button>
            <button onClick={onClickLeave}> 퇴장</button>
            <h1>{msg}</h1>
        </div>
    );
};

export default Say;