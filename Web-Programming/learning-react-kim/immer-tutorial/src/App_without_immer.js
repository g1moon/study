import React, {useRef, useCallback, useState} from 'react';

const App = () => {
    const nextId = useRef(1);
    const [form, setForm] = useState({name: '', username: ''});
    const [data, setData] = useState({
        array: [],
        uselessValue: null
    });

    //input 수정을 위한 함수
    const onChange = useCallback(
        e => {
            const {name, value} = e.target;
            setForm({
                ...form,
                [name]: [value]
            });
        },
        [form]
    );

    //form 등록을 위한 함수
    const onSubmit = useCallback(
        e => {
            e.preventDefault(); //새로고침 막기
            //data.array에 추가 할 info data
            const info = {
                id: nextId.current,
                name: form.name,
                username: form.username
            };

            //array에 새 항목 등록
            setData({
                ...data,
                array: data.array.concat(info)
            });
            nextId.current += 1;
        },
        [data, form.name, form.username]
    );

    // 항목을 삭제하는 함수(data.array만 업데이트시키면 된다)
    const onRemove = useCallback(
        id => {
            setData({
                ...data,
                array: data.array.filter(info => info.id !== id)
            });
        },
        [data]
    );

    return (
        <div>
            {/*     form -> {username: '', name: ''}      */}
            <form onSubmit={onSubmit}>
                <input
                    name='username'
                    placeholder='id'
                    value={form.username}
                    onChange={onChange}
                />
                <input
                    name='name'
                    placeholder='name'
                    value={form.name}
                    onChange={onChange}
                />
                <button type = 'submit'>등록</button>
            </form>
            <div>
                <ul>
                    {data.array.map(info =>(
                        <li key = {info.id} onClick = { () => onSubmit(info.id)}>
                            {info.username} ({info.name})
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};
//
// export default App;


