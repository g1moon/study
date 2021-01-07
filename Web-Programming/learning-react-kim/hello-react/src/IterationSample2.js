import React, {useState} from "react";

const IterationSample3 = () => {
    //state초기
    const [names, setNames] = useState([
            {id : 1, text : '눈사람'},
            {id : 2, text : '얼'},
            {id : 3, text : '눈'},
            {id : 4, text : '바'}
            ]);

    const [inputText, setInputText] = useState('');
    const [nextId, setNextid] = useState(5); //새로운 항목 추가할 때 사용할 id

    //key값 할당
    const nameList = names.map(name => <li key={name.id}>{name.text}</li>);

    //이벤트 함수
    const onChange = e => setInputText(e.target.value);

    const onClick = () => {
        //nextNames는 기존의 names에 새로운 객체를 더한 것
        const nextNames = names.concat({
            id: nextId,
            text: inputText
        });
        setNextid(nextId + 1);
        setNames(nextNames);//names는 객체 -> map으로 .id,.text접금
        setInputText('');//비워주기
    }
    //return
    return (
        /*감싸주기*/
        <>
            <input value = {inputText} onChange = {onChange}/> {/*추가 인풋 창*/}
            <button onClick={onClick}>추가</button> {/*추가 버튼*/}
            <ul>{nameList}</ul>
        </>
    );
};

export default IterationSample3;