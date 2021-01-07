import React, {Component} from "react";

class Counter extends Component {

    // constructor(props) {
    //     super(props);
    //     //컴포넌트의 state의 초깃 값 설정하기(객체형식)
    //     this.state = {
    //         number: 0
    //     };
    // }

    state = {
        number: 0
    };

    render() {
        const {number} = this.state;
        return (
            <div>
                <h1>{number}</h1>
                <button
                    onClick={ () => {
                        this.setState(
                            {
                                number : number + 1
                            },
                            () => {
                                console.log('방금 setState가 호출되었습니다');
                                console.log(this.state);
                            }
                        )
                    }}
                    >
                    +1
                </button>

            </div>
        );
    }
}


export default Counter;