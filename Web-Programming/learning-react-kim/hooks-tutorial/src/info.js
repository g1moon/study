import React, {useReducer} from "react";

function reducer(state, d) {
    //d : <input name = 'name' value = 'sss'?
    //state를 복사하고, state.name : state.value
    //               'name' : 'sss'
    const res = {
        ...state,
        [d.name] : d.value
    };
    //{name: "abcd", nickname: ""}name: "abcd"nickname: ""__proto__: Object
    console.log(res)
    return res;
}

const Info = () => {
    const [state, dispatch] = useReducer(reducer, {
        name : '',
        nickname:''
    });

    const {name, nickname} = state;
    const onChange = e => {
        //바뀐 인풋html에 대한 정보
        console.log(e.target);
        dispatch(e.target);
    };

    return (
        <div>
            <div>
                <input name='name' value={name} onChange={onChange}/>
                <input name='nickname' value={nickname} onChange={onChange}/>
            </div>

            <div>
                <div>
                    <b>이름 : </b> {name}
                </div>
                <div>
                    <b>닉네임 : </b>{nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;