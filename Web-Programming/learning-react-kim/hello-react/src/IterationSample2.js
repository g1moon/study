import React, {Component} from "react";

const IterationSample2 = () => {
    const names = ['a', 'b', 'c', 'd']
    const nameList = names.map(
        (name, index) => <li key={index}>{name}</li>);

    return <ul>{nameList}</ul>;
    };

export default IterationSample2;