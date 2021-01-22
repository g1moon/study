import React from 'react';
import qs from 'qs';

const About = ( {location} ) => {
    const q = qs.parse(location.search, {
        ignoreQueryPrefix: true //문자열 맨 앞의 ?를 생략
    });
    const showDetail = q.detail === 'true'; //쿼리의 파싱 결과 값은 문자열

    return (
        <div>
            <h1>소개</h1>
            <p>라우터실습중!</p>
            {showDetail && <p>detail 값이 true 입니다.</p>}
        </div>
    );
};

export default About;