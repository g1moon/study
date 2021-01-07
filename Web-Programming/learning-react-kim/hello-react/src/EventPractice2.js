import React, {useState} from "react";

const EventPractice2 = () => {
    //useState를 이용해 form을{ sername과 msg}를 갖고 있는 객체로 만들어주고, 세터 설정
    const [form, setForm] = useState({
        username: '',
        msg : ''
    });
    const {username, msg} = form;

    //username과 Event가 체인지할때 발생시킬 이벤트 함수
    const onChange = e => {
        const nextForm = {
            ...form, //기존의 form내용을 이 자리에 복사
            [e.target.name]: e.target.value //원하는 값을 덮어 씌우기
        };

        setForm(nextForm); //위에서 바꾼 것들을 업데이트해주기
    };

    const onClick = e => {
        alert(username + ':' + msg);
        setForm({
            username : '',
            msg : ''
        });
    };
    const onKeyPress = e => {
        if (e.key === 'Enter') {
            onClick();
        }
    };

    return (
        <div>
            <h1>이벤트 연습</h1>
            <input
                type='text'
                name='username'
                placeholder='사용자명'
                value={username}
                onChange={onChange}
            />
            <input
                type='text'
                name='msg'
                placeholder='msg 입력'
                value={msg}
                onChange={onChange}
            />
            <button onClick={onClick}>확인</button>
        </div>
    );
};

export default EventPractice2;