import React, {useRef, useState, useCallback, useReducer} from 'react';
import TodoTemplate from './components/TodoTemplate';
import TodoInsert from "./components/TodoInsert";
import TodoList from './components/TodoList';

function createBulkTodos() {
    const array = [];
    for (let i = 1; i <= 2500; i++) {
        array.push({
            id: i,
            text: `할일 ${i}`,
            checked: false,
        });
    }
    return array;
}

//reducer----------
function todoReducer(todos, action) {
    switch (action.type) {
        case 'INSERT':
            return todos.concat(action.todo);

        case 'REMOVE':
            return todos.filter(todo => todo.id !== action.id);

        case 'TOGGLE':
            return todos.map(todo =>
                todo.id === action.id
                    ? {...todo, checked: !todo.chekced}
                    : todo);

        default:
            return todos;
    }
}
const App = () => {
    // const [todos, setTodos] = useState(createBulkTodos);
    const [todos, dispatch] = useReducer(todoReducer,undefined, createBulkTodos)

//--------------------------------------------------------_
    const nextId = useRef(2501);

    const onInsert = useCallback((text) => {
        const todo = {
            id: nextId.current,
            text: text,
            checked: false,
        };
        // setTodos(todos.concat(todo));
        // setTodos(todos => todos.concat(todo));
        dispatch({type: 'INSERT', todo})
        nextId.current += 1;
        console.log(todos);
    }, []);

//--------------------------------------------------------
    const onRemove = useCallback(id => {
        // setTodos(todos => todos.filter(todo => todo.id !== id));
        dispatch({type: 'REMOVE', id});
    }, []);


//--------------------------------------------------------
    const onToggle = useCallback(id => {
        dispatch({type: 'TOGGLE', id});
    }, []);
    //     setTodos(todos =>
    //         todos.map(todo =>
    //             todo.id === id
    //                 ? {
    //                     ...todo,
    //                     checked: !todo.checked
    //                 }
    //                 : todo));
    //
    // });
//--------------------------------------------------------
    return (
        <TodoTemplate>
            <TodoInsert onInsert={onInsert}/>
            <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle}/>
        </TodoTemplate>
    );
};

export default App;