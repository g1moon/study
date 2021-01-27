import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {createStore} from 'redux';
import rootReducer from "./modules";
import {Provider} from 'react-redux';
//ReduxDevTools 적용
import {composeWithDevTools} from "redux-devtools-extension";

//스토어 만들기, ReduxDevTools 적용
const store = createStore(rootReducer, composeWithDevTools());

ReactDOM.render(
    <Provider store={store}>
        <App/>
    </Provider>,
    document.getElementById('root'));


