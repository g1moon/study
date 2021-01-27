// @flow
import React from 'react';
import {useSelector} from 'react-redux';
import {changeInput, toggle} from '../modules/todos';

const TodoContainer = () => {
    const {input, todos} = useSelector(({todos}) => ({
        input: todos.input,
        todos.: todos.todos
    }));

    const dispatch = useDispatch();
    const onChangeInput = useCallback(input => dispatch(changeInput(input)), [dispatch])
    const onToggle  = useCallback(id => dispatch(toggle))
};

