// var dayjs= require('dayjs')
// dayjs().format()

// // console.log(dayjs.unix(1648049128).format('YYYY-MM-DD HH:mm:ss'))
// // console.log(dayjs().unix())
// console.log(dayjs().daysInMonth)






function randomNum(minNum,maxNum){ 
    switch(arguments.length){ 
        case 1: 
            return parseInt(Math.random()*minNum+1,10); 
        break; 
        case 2: 
            return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
        break; 
            default: 
                return 0; 
            break; 
    } 
} 


console.log(randomNum(0,4294967295))