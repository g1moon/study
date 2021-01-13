// eslint-disable-next-line no-unused-vars
import React, {Component} from 'react';

class LifeCycleSample extends Component {
    state = {
        number: 0,
        color: null,
    }

    //
    myRef = null; //ref를 설정할 부분

    //
    constructor(props) {
        super(props);
        console.log('constructor');
    }

    //부모에서 받은 color값을 state에 동기화(props에 있는 값을 state에 넣을 때 )
    static getDeriveStateFromPops(nextProps, prevState) {
        console.log('getDeriveStateFromPops');
        if (nextProps.color !== prevState.color) { //다르면??
            return {color: nextProps.color}
        }
        return null;
    }

    //
    componentDidMount() {
        console.log('componentDidMount');
    }

    //
    shouldComponentUpdate(nextProps, nextState) {
        console.log('shouldComponentUpdate', nextProps, nextState);
        //숫자의 마지막 자리가 4면 리렌더링하지 않는다
        return nextState.number % 10 !==4;
    }

    componentWillUnmount() {
        console.log('componentWillUnmount')
    }

    handleClick = () =>{
        console.log('this: ', this); //확인
        this.setState({
            number: this.state.number + 1 //현재 값에 1더하기
        });
    }

    //DOM에 변화가 일어나기 직전의 색상 속성을 snapshot값으로 반환해 ->
    //이것을 componentDidUpdate에서 조회 가능
   getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log('componentWillUnmount');
        if (prevProps.color !== this.props.color) {
            return this.myRef.style.color;
        }
        return null;
    }

    //smap샷이 있으면(변화가 일어났으면) -> 업데이트 되기 전을 확
    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log('componentDidUpdate', prevProps, prevState);
        if (snapshot) {
            console.log('업데이트되기 전 : ', snapshot);
        }
    }

    render() {
        console.log('render');

        const style = {
            color: this.props.color
        };

        return (
            <div>
                <h1 stype={style} ref={(ref) => this.myRef = ref}>
                    {this.state.number}
                </h1>
                <p>color: {this.props.color}</p>
                <button onClick = {this.handleClick}>
                    더하기
                </button>
            </div>
        );
    }

}

export default LifeCycleSample;