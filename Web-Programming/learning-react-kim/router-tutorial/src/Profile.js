import React from 'react';

const data = {
    velopert: {
        name: '김민준',
        desc: '리액트 좋아하는 개발자'
    },
    gildong: {
        name: '홍길동',
        desc: '소설 주인'
    }
};

const Profile = ({match}) => {
    const {username} = match.params;
    const profile = data[username];

    if (!profile) {
        return <div>존재하지 않는 사용자 입니다.</div>
    }

    return (
        <div>
            <h3>
                {username}({profile.name})
            </h3>
            <p>{profile.desc}</p>
        </div>
    );

};

export default Profile;