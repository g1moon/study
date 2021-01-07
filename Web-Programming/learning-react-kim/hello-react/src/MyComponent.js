// import React, {Component} from "react";
import React from "react";
import {Component} from "react/cjs/react.production.min";
import PropTypes from 'prop-types';

class MyComponent extends Component {
    render() {
        const {name, favoritNumber, children} = this.props; //비구조화 할당
        return (
            <div>
                이름 : {name} <br />
                child : {children} <br />
                favnum : {favoritNumber}
            </div>
        );
    }
}

MyComponent.defaultProps = {
    name : '기본이름'
}

MyComponent.propTypes = {
    name: PropTypes.string,
    favoritNumber: PropTypes.number.isRequired
};

export default MyComponent;

