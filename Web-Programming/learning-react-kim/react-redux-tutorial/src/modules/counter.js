const INCREASE = 'counter/INCREASE';
const DECREASE = 'counter/DECREASE';

export const increase = () => ( {type: INCREASE} );
export const decrease = () => ( {type: DECREASE} );


//초기상태와 리듀서
const initState = {
    number: 0
};

function counter(state = initState, action) {
    switch (action.type) {
        case INCREASE:
            return {number: state.number + 1};

        case DECREASE:
            return {number: state.number - 1};

        default:
            return state;
    }
}

export default counter