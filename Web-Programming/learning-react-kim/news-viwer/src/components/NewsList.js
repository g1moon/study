import React, {useState, useEffect} from 'react';
import styled from 'styled-components';
import NewsItem from './NewsItem';
import axios from 'axios';
import usePromise from '../lib/usePromise';

const NewsListBlock = styled.div`
  box-sizing: border-box;
  padding-bottom: 3rem;
  width: 768px;
  margin: 0 auto;
  margin-top: 2rem;
  @media screen and (max-width: 768px) {
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
  }
`;

const NewsList = ({category}) => {
    //export default function usePromise(promiseCreator, deps)
    const [loading, response, error] = usePromise(() => {
        const q = category === 'all' ? '' : `category=${category}`;
        return axios.get(
            'https://newsapi.org/v2/top-headlines?country=kr${query}&apiKey=38d701c9c2844235aa2d63817a2a64a9'
        );
    }, [category]);

    //대기
    if (loading) {
        return <NewsListBlock> 대기중...</NewsListBlock>
    }

    if (!response) {
        return null;
    }

    if (error) {
        return <NewsListBlock>에러발생!</NewsListBlock>
    }

    //response값이 유효
    const {articles} = response.data;
    return (
        <NewsListBLock>
            {articles.map(a => (
                <NewsItem key={a.url} article={a}/>
            ))}
        </NewsListBLock>
    );
};

export default NewsList;