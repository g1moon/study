import React, {useContext} from 'react';
import ColorContext from "./color";

const ColorBox = () => {
    const {state} = useContext(ColorContext);
    return (
        <div style={{background : state.color }}/>
        <div style={{background : state.subcolor}}/>
    );
};

export default ColorBox;


const store = createSotre(reducer);

