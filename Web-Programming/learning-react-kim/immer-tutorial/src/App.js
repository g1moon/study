import React, {useRef, useCallback, useState} from 'react';
import produce from 'immer';

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
            setForm(
                produce(form, draft => {
                    draft[name] = value;
                })
            );
        },
        [form]
    );

    //form 등록(form에서 name과 username을 받아와)
    const onSubmit = useCallback(
        e => {
            e.preventDefault();
            const info = {
                id: nextId.current,
                name: form.name,
                username: form.username
            };

            //새항목 등록 -> 이후에 초기화 필요
            setData(
                produce(data, draft => {
                    draft.array.push(info);
                })
            );

            //등록후 초기화
            setForm({
                name: '',
                username: ''
            });
            nextId.current += 1;
        },
        [data, form.name, form.username]
    );

    //항목을 삭제하는 함수
    const onRemove = useCallback(
        id => {
            produce(data, draft => {
                draft.array.splice(draft.array.findIndex(info => info.id === id), 1);
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

export default App;