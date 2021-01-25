
import React, {useCallback, useState} from 'react';
import NewsList from './components/NewsList';
import Categories from './components/Categories';
import {Route} from 'react-router-dom';
import NewsPage from "./pages/NewsPage";


const App = () => {
    //? 은 optional
    //category URL 파라미터가 없다면 -> 전체 카테고리를 선택(all)
    return <Route path = '/:category?' component={NewsPage}/>
};

export default App;