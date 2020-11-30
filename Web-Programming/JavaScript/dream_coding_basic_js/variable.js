
'use strict';
//--------------------------------------------------
let lst = [12,32,44,45,52,61];

//1 
for (let i =0; i < lst.length; i ++){
    console.log(lst[i]);
}

//2
for (let item of lst){
    console.log(item);
}

//3
lst.forEach( function (item, idx, arr){
    console.log(`${idx} : ${item}`);
});

//----------------------------------------------------
class Student{
    constructor(name, age, enrolled, score){
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}



const objs = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88)
]

//----------------------------------------------
objs.forEach( function (item, idx) {
    console.log(item, idx);
});

//
objs.forEach( (item, idx, array) => console.log(item));

//
for(let i = 0; i < objs.length; i++){
    console.log(objs[i]);
}

//
for(let item of objs){
    console.log(item);
}
//-------------------------------------------------------
console.clear(); //clear

//q5. find a student with the score 90
//결과가 하나만 나옴... 돌다가 만족하면 바로 꺼버리는듯?
const res1 = objs.find( function (item, idx, arr){
    return item.score === 90;
});
console.log(res1);

//90하나짜리
const res2 = objs.find( (item, idx, arr) => item.score === 90);
console.log(res2);

//0번 인덱스 아이템
const res3 = objs.find( (item, idx, arr) => idx === 0);
console.log(res3)

//----------------------------------------------------
//q6. make an array of enrolled students
console.clear()
const res4 = objs.filter( (item) => item.enrolled );
console.log(res4);

//-----------------------------
//q7. make an array containing only the students's scores 
//result should be 
let arr = [];
objs.forEach( (item) => arr.push(item.score));
console.log(arr);
console.log(arr.slice(0,2));
let popped = arr.pop();
console.log(popped);

//popped item -> **2 
console.clear();
const res5 = objs.map( (item) => (item.score) ** 2);
console.log(res5);

//-----------------------------------
//q8. check if there is a student with the score lower than 50
const res6 = objs.filter( (item) => item.score < 50);
if (res6.length != 0){
    console.log(true); 
}else{
    console.log(false);
}
//result:  true

//some을 이용하면 -> 하나라도 맞으면 true리턴 
const res7 = objs.some( (item) => (item.score < 50));
console.log(res7); //true

//everys는 모두 충족해야함

//-------------------------------------
//q9. compute students avg score 
console.clear();
let score_lst = [];
objs.forEach( (item) => score_lst.push(item.score));
let sum_num = 0;
for ( let score of score_lst){
    sum_num += score;
}
console.log(sum_num / score_lst.length)

//reduce는 모든 걸 더해서 리턴한다, 이전값과 -> 다음값 -> 초기값은 0
const res8 = objs.reduce( (prev, curr) => prev + curr.score, 0);
console.log(res8 / objs.length);

//------------------
//q10. make a string containing all the scores
// result should be : '45,` 80, 90, 66, 88'
let sc_lst = [];
objs.forEach( (item) => sc_lst.push(item.score) )
let res9 = sc_lst.join(",");
console.log(res9);

//map을 이용해서 
console.clear();
const res10 = objs
    .map( (item) => item.score)
    .filter( (item) => item >= 50) // score
    .join();
console.log(res10);