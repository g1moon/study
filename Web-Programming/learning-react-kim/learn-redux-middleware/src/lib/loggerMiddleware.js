

const loggerMiddleware = store => next => action =>{
    //액션 타입으로 log를 그룹화함
    console.group(action && action.type);
    //Prev
    console.log('Prev: ', store.getState());
    //Action
    console.log('Action: ', action);
    //다음 미들웨어 or 리듀서로 전달(next)
    next(action);
    //After
    console.log('After: ', store.getState());
    //그룹 끝
    console.group();
}

export default loggerMiddleware;