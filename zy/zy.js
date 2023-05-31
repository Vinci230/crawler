setTimeout(function() {
    console.log('a');
    setTimeout(function(){
        console.log('b');
        setTimeout(function(){
            console.log('c');
        },3000)
},3000)
}, 3000);
//promise 链式回调
new Promise((resolve,reject)=>{
    setTimeout(() => {
        console.log('a');
        resolve()
    }, 3000)
    
}).then(() =>{   //执行.then的时候，将b生成为一个promise对象
     b();
})
var b = function(){
    return new  Promise((resolve,reject)=>{
        setTimeout(() => {
            console.log('b');
            resolve()
        }, 3000)
     
    }).then(() =>{
         c();
    })
}
var c =  function(){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            console.log('c');
            resolve()
        }, 3000)
       
    })
    
}
//aysnc await异步队列
let a=(time)=>{
    return new Promise((resolve)=>{
        setTimeout(() => {
            resolve();
        }, time);
    });
};
var b=(time)=>{
    return new Promise((resolve)=>{
        setTimeout(() => {
            resolve();
        }, time);
    });
};
var c=(time)=>{
    return new Promise((resolve)=>{
        setTimeout(() => {
            resolve();
        }, time);
    });
};


async function demo()
{
    let word=await a(3000);
    console.log('a');
    let word1=await b(3000);
    console.log('b');
    let word2=await c(3000);
    console.log('c');
}
demo()
