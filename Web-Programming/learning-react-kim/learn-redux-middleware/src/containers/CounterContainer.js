import React from 'react';
import Counter from "../components/Counter";
import {connect, useSelector} from 'react-redux';
import {decrease, increase} from "../modules/counter";
//state, 액션함수
const CounterContainer = ({number, increase, decrease}) => {
    return (
        <Counter number={number} onIncrease={increase} onDecrease={decrease}/>
    );
};

export default connect(
    state => ({
        number: state.counter
    }),
    {
        increase,
        decrease
    }
)(CounterContainer);