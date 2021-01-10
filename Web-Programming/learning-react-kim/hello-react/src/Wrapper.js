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
// import React from 'react';
// import Hello from './Hello';
// import Wrapper from './Wrapper';
//
// function App() {
//     return (
//         <Wrapper>
//             <Hello color="red" name="react" />
//             <Hello color="pink"/>
//         </Wrapper>
//     );
// }
//
// export default App;