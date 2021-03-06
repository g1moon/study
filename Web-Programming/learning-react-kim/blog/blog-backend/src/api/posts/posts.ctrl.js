let postId = 1;

//posts 배열 초기 데이터
const posts = [
    {
        id: 1,
        title: '제목',
        body: '내용',
    },
];

/*포스트 작성
POST /api/posts
{title, boy}
* */

exports.write = ctx => {
    //REST API의 Request Body는 ctx.request.body에서 조회
    const {title, body}  = ctx.request.body;
    postId += 1;
    const post = {id: postId, title, body};
    posts.push(post);
    ctx.body = post;
};

/*포스트 목록 조회
* GET /api/posts
* */
exports.list = ctx => {
    ctx.body = posts;
};

/*
* 특정포스트 조회
* GET /api/posts/:id*/
exports.read = ctx => {
    const {id} = ctx.params;
    //주어진 id 값으로 포스트를 찾는다
    //파라미터로 받아 온 값은 문자열 형식이므로 -> 파라미터를 숫자로 변환
    //p.id 값을 문자열로 변경
    const post = posts.find(p => p.id.toString() === id);
    if (!post) {
        ctx.status = 404;
        ctx.body = {
            message: '포스트가 존재하지 않습니다.'
        };
        return;
    }
    ctx.body = post;
};

/*특정 포스트 제거
DELETE /api/posts/:id*/
exports.remove = ctx => {
    const { id } = ctx.params;
    //해당 id를 가진 Post가 몇번쨰인지
    const index = posts.findIndex(p => p.id.toString() === id);
    //포스트가 없으면 오
    if (index === -1) {
        ctx.status = 404;
        ctx.body = {
            message: '포스트가 존재하지 않습니다'
        };
        return;
    }
};

/*포스트 수정(교체)
* PUT /api/posts/:id
* {title, body} */
exports.replace = ctx => {
    //put 메서드는 전체 포스트 정보를 입력해서 -> 데이터를 통째로 교체
    const {id} = ctx.params;
    //해당 id를 가진 post가 몇번쨰인지
    const index = posts.findIndex(p => p.id.toString() === id);
    if (index === -1) {
        ctx.status = 404;
        ctx.body ={
            message : '포스트가 존재하지 않습니다'
        }
        return;
    }
    //전체 객체를 덮어 씌운다
    //따라서 id를 제외한 기존 정보를 날리고, 객체를 새로 만든다
    posts[index] = {
        id,
        ...ctx.request.body //const {title, body}  = ctx.request.body;
    };
    ctx.body = posts[index];
};

/*포스트 수정(특정 필드 변경
* PATCH /api/posts/:id
* {title, boy}*/

exports.update = ctx => {
    const {id} = ctx.params;
    const index = posts.findIndex(p => p.id.toString() === id);
    if (index === -1) {
        ctx.status = 404;
        ctx.body = {
            message:'포스트가 존재하지 않습니'
        }
        return;
    }

    //기존 값에 정보를 덮어 씌운다
    posts[index] = {
        ...posts[index], //id해서 id빼고 다 날림
        ...ctx.request.body,
    }
    ctx.body = posts[index];
};