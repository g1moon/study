import React, {useState, useRef, useCallback, useReducer} from 'react';
import TodoTemplate from "./components/TodoTemplate";
import TodoInsert from "./components/TodoInsert";
import TodoList from './components/TodoList';

function createBulkTodos() {
    const arr = [];
    for (let i = 1; i <= 2500; i++) {
        arr.push({
            id: i,
            text: `할 일 ${i}`,
            checked : false,
        });
    }
    return arr;
}

function todoReducer(todos, action) {
    switch (action.type) {
        case 'INSERT':
            return todos.concat(action.todo);

        case "REMOVE":
            return todos.filter(todo =>
                action.id !== todo.id
            );

        case "TOGGLE":
            return todos.map(todo =>
                todo.id === action.id ? {...todo, checked: !todo.checked} : todo
            );
    }
}


const App = () => {
    const [todos, setTodos] = useState(createBulkTodos);
    const nextId = useRef(4);

    const onInsert = useCallback(text => {
        const todo = {
            id : nextId.current,
            text,
            checked: false
        };
        setTodos(todos => todos.concat(todo));
        nextId.current += 1;
    }, []);

    const onRemove = useCallback(id => {
        setTodos(todos => todos.filter(todo => todo.id !== id));
        }
    , []);

    const onToggle = useCallback(id => {
        setTodos(todos => todos.map(todo =>
            todo.id === id ? {...todo, checked: !todo.checked} : todo
        ));
    }, []);



    return (
        <TodoTemplate>
            <TodoInsert onInsert = {onInsert}/>
            {/*todos배열안에들어있는 객체는 id,내용,완료여부*/}
            <TodoList todos = {todos} onRemove={onRemove} onToggle = {onToggle}/>

        </TodoTemplate>
    );
};

export default App;

const todos = [{id: 1, checked: true}];
const nextTodos = [...todos];

//1------------------------------------------------------
nextTodos[0].checked = false;
console.log(todos[0] === nextTodos[0]); //아직 똑같은 객체를 가리키므로 true

//2------------------------------------------------------
nextTodos[0] = {
    ...nextTodos,
    checked: false
};
console.log(todos[0] === nextTodos[0]); //새로운 객체를 할당했기 떄문에 false

