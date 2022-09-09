const fs = require('fs')
const [x,y,w,h] = fs.readFileSync("input.txt").toString().split(' ')
const {min}=Math

console.log(min(min((w-x),x),min((h-y),y)))
