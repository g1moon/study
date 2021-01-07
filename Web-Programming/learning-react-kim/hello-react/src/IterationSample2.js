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

    //이벤트 함수
    //1.인풋창 변화
    const onChange = e => setInputText(e.target.value);

    //2.추가 버튼 클릭
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

    //3. 데이터 삭제(삭제할 id값을 입력으로 필요)
    const onRemove = id => {
        //
        const nextNames = names.filter(name => name.id !== id);
        setNames(nextNames);
    };

    //return에서 내보내 줄 nameList 작
    //객체 name에서 id를 키로하고 text를 보여준다.
    //더블클릭하면 위에서 만든 삭제 이벤트 발생
    const nameList = names.map(name => (
        <li key={name.id}
            //더블클릭한 것의 id를 삭제할 것으로 넘겨줘
            onDoubleClick={() => onRemove(name.id)}>
            {name.text}
        </li>
    ));

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