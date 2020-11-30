'use strict'

//js is synchronous
//execute the code block by orger after hoisting
//hoisiting : var, function, decalration이 위에서 먼저

console.log('1'); 
// setTimeout( function () {
//     console.log('2');
// })
setTimeout( () => console.log('2'), 1000);
console.log('3');

//Synchronous callback -- hoisting
function printImmediately(print){
    print();
} // -> hoisting
printImmediately( () => console.log('hello'));

//Asynchronous callback
function printWithDelay(print, timeout){
    setTimeout(print, timeout);
} // -> hoisting
printWithDelay( () => console.log('async callback'), 2000);


//Callback Hell example 
class UserStorage{
    loginUser(id, password, onSuccess, onError){
        setTimeout( () => {
            if (
                (id == 'ellie' && password == 'dream') ||
                (id == 'coder' && password == 'academy')
            ){
                onSuccess(id);
            } else{
                onError(new Error('not found'));
            }
        }, 2000);
    }

    getRoles(user, onSuccess, onError) {
        setTimeout(() => {
        if (user == 'ellie') {
            onSuccess( { name : 'ellie', role: 'admin'});
        } else{
            onError(new Error('no access'));
        }
    }, 1000);
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');

userStorage.loginUser(
    id,
    password,
    user => {
        userStorage.getRoles(
            user,
            userWithRole =>{
                alert(`hello ${userWithRole.name}, you have a ${userWithRole.role} role`);
            },
            eroor =>{
                console.log(error);
            }
        );
    },
    error => {
        console.log(error);
    }
);