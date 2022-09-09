const fs = require('fs')

let input = fs.readFileSync("/dev/stdin").toString().split('\n')
//\n으로 구분하자. \r은 환경에따라 존재하는데 이거 신경쓰면 백준에서는 오류로뜸

input=input.map(e=>{    
    if(e.slice(0,4)==='push'){
        return e.split(' ')
    }
    else{
        return e.split()
    }});
//push와 숫자를 분리해서 배열화
//나머지 명령어도 배열화함

let stack=[]
let answer=[]
//console.log는 느리기 때문에 답을 배열에 모아 한번에 출력하자.

input.forEach(element=>{

    switch(element[0]){

     case 'push':
        stack.push(Number(element[1]))
        break
     case 'pop':
        stack.length!=0?answer.push(stack.pop()):answer.push(-1)
        break
     case 'size':
        answer.push(stack.length);
        break
     case 'empty':
        stack.length!=0?answer.push(0):answer.push(1)
        break
     case 'top':
        stack.length!=0?answer.push(stack[stack.length-1]):answer.push(-1)
        break
    }
    
});

console.log(answer.join("\n"));