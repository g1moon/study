import React, {Component} from 'react';  //책에는 사라져 있음.
import LifeCycleSample from './LifeCycleSample';

function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}
/////////////////
class App extends Component {
    state = {
        color : '#000000'
    }

    handleClick = () =>{
        this.setState({
            color: getRandomColor()
        }
        );
    }

    render() {
        return (
            <div>
                <button onClick = {this.handleClick}>랜덤색상</button>
                <LifeCycleSample color= {this.state.color}/>
            </div>
        );
    }
}

export default App;

// //-----------------------------------------------
// import React from 'react';
// import InputSample from './InputSample';
//
// function App() {
//     return (
//         <InputSample/>
//     );
// }
//
// export default App;