import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {Provider} from "react-redux";
import {applyMiddleware, createStore} from "redux";
import rootReducer from "./modules";
import loggerMiddleware from "./lib/loggerMiddleware";
import {createLogger} from 'redux-logger';


const loger = createLogger();
//스토어 만들고 , Provider로 감싸주고 , 스토어 넣어주기
const store = createStore(rootReducer, applyMiddleware(looger()));


ReactDOM.render(
    <Provider store={store}>
        <App/>
    </Provider>,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

const loading = handleAction({
        [START_LOADING]: (state, action) => ({
            ...state,
            [action.payload]: true
        }),

        [FINISH_LOADING]: (state, action) => ({
            ...state,
            [action.payload]: false
        })
    }
)

