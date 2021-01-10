import React, {useState, useMemo, useCallback, useRef} from "react";

const getAverage = numbers => {
    console.log('------평균 계산중 ---');
    if (numbers.length === 0) {
        return 0;
    }
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
};

const Average = () => {
    const [list, setList] = useState([]);
    const [number, setNumber] = useState('');
    //useRef를 사용해 ref를 설정하면 ->
    //useRef를 통해 만든 객체 안의 current값이 실제 엘리먼트를 가리킴
    const inputEl = useRef(null);

    const onChange = useCallback(e => {
            setNumber(e.target.value);
        }, []
    );

    const onInsert = useCallback(() => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber('');

        inputEl.current.focus();
    }, [list, number]);

    const avg = useMemo(() => getAverage(list), [list]);

    return (
        <div>
            <input value={number} onChange={onChange} ref={inputEl}/>
            <button onClick={onInsert}>등록</button>
            <ul>
                {list.map((val, idx) => (
                    <li key={idx}>{val}</li>
                    ))}
            </ul>
            <div>
            <b>평균값 : </b> {avg}
            </div>
        </div>
    );
};

export default Average;