'use strict'

class Counter{
    constructor(runEvryFiveTime){
        this.counter = 0;
        this.callback = runEvryFiveTime;
    }

    increase() {
        this.counter++;
        console.log(this.counter);
        if (this.counter % 5 === 0){
            // if (this.callback){
            //     this.callback(this.counter);
            // } --> 간단하게
            this.callback && this.callback(this.counter); //simple ver
        }
    }
}

//----------------------------------
function printSomething(num){
    console.log(`wow! ${num}`);
}

function alertNum(num){
    alert(`alert! ${num}`);
}

const coolCounter = new Counter(printSomething);
const alertCounter = new Counter(alertNum);
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
coolCounter.increase();
