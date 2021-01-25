import React from 'react';
import ColorContext from "./contexts/color";

const ColorBox = () => {
    return (
        <ColorContext.Consumer>
            {value => (
                <div
                    style = {{
                        width: '64px',
                        height: '65px',
                        background: value.color
                    }}
                    />
                )}
        </ColorContext.Consumer>
    )
};