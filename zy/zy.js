//嵌套
// setTimeout(function() {
//     console.log('a');
//     setTimeout(function(){
//       console.log('b');
//         setTimeout(function(){
//            console.log('c')
// },3000);
//
// },3000);
//
//
//
// },3000);

//链式回调
let p = new Promise((resolve, reject) => {
//做一些异步操作
setTimeout(() => {
console.log("a")


 }, 3000);
})
.then(
(data) => {
console.log(data);
return data;})
//此时输出data为resolve传入的参数

