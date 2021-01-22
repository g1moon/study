import produce from 'immer';

const originalState = [
    {
        id: 1,
        todo: '공부하기 1',
        checked: true,
    },

    {
        id: 2,
        todo: '공부하기2',
        chekced: true,
    },

    {
        id: 3,
        todo: '공부하기3',
        chekced: false,
    }
];

const nextState = produce(originalState, draft => {
    //id가 2인 항목의 checked값을 false로 변경----------------------------------
    //id가 2인 항목 찾기
    const todo = draft.find(t => t.id === 2);
    todo.checked = false;

    //배열에 새로운 항목 추가----------------------------------
    draft.push({
        id: 4,
        todo: '추가하는 공부4',
        checked: false,
    });

    //아이디가 1인항목 제거------------------------------
    draft.splice(draft.findIndex(t => t.id ===1), 1)
})