import React from 'react';

function Wrapper({children}) {
    const style = {
        border: '2px solid black',
        padding: '16px',
    };
    return (
        <div style={style}>
            {children}
        </div>
    )
}

export default Wrapper;


//App.js
// //-----------------------------------------------
// // import React from 'react';
// // import Hello from './Hello';
// // import Wrapper from './Wrapper';
// //
// // function App() {
// //     return (
// //         <Wrapper>
// //             <Hello color="red" name="react" />
// //             <Hello color="pink"/>
// //         </Wrapper>
// //     );
// // }
// //
// // export default App;

//Hello.js
// import React from 'react';
//
// function Hello({color, name}) {
//     return <div style = {{color}}> 안녕하세요 {name}</div>
// }
//
// Hello.defaultProps = {
//     name: '이름없음'
// }
//
// export default Hello;