const CHANGE_INPUT = 'todos/CHANGE_INPUT'; //Input갓 변경
const INSERT = 'todos/INSERT'; //새로운 todo를 등록
const TOGGLE = 'todos/TOGGLE'; //todo를 체크, 체크해제함
const REMOVE = 'todos/REMOVE'; //todo 제거

//액션 생성 함--------------------------------------------
//타입은 위에 정의한 액션 타입이고,
//나중에 action으로 사용될 것들 (input, text, id)
//---------------------------------------------------------------------__
// export const changeInput = createAction(CHANGE_INPUT, input => input);
//
// let id = 3; // insert 가 호출 될 때마다 1씩 더해집니다.
// export const insert = createAction(INSERT, text => ({
//     id: id++,
//     text,
//     done: false,
// }));
//
// export const toggle = createAction(TOGGLE, id => id);
// export const remove = createAction(REMOVE, id => id);
//---------------------------------------------------------------------__
export const changeInput = input => ({
    type: CHANGE_INPUT,
    input
});

let id = 3; //insert가 호출될 때마다 1씩 더해진다.
export const insert = text => ({
    type: INSERT,
    todo: {
        id: id++,
        text,
        done: false
    }
});

export const toggle = id => ({
    type: TOGGLE,
    id
})

export const remove = id => ({
    type: REMOVE,
})
//초기 상태 정의-----------------------------------------------
const initState = {
    input: '',
    todos: [
        {
            id: 1,
            text: 'redux 공부',
            done: true
        },
        {
            id: 2,
            text: '20장까지 보기',
            done: false
        }
    ]
};

//리듀서 함수 만들기 -----------------------------------------------
function todos(state = initState, action) {
    switch (action.type) {
        case CHANGE_INPUT:
            return {
                ...state,
                input: action.input
            };

        case INSERT:
            return {
                ...state,
                todos: state.todos.concat(action.todo)
            };

        case TOGGLE:
            return {
                ...state,
                todos: state.todos.map(todo =>
                    todo.id === action.id ?
                        {...todo, done: !todo.done} : todo
                )
            };

        case REMOVE:
            return {
                ...state,
                todos: {
                    todos.filter(todo =>
                        todo.id !== action.id)
                }
            };

        default:
            return state;
    }
}

export default todos;


const todos = handleActions(
    {
        [CHANGE_INPUT]: (state, action) => ({...state, input: action.payload}),
        [INSERT]: (state, action) => ({
            ...state,
            todos: state.todos.concat(action.payload)
        })
    }
