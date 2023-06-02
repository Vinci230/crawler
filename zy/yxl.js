function  A(a,b){
    this.a=a,
        this.b=b
}//函数里的参数与this调用的参数名字要保持一致
A.prototype.sum=function ()//prototype.加名字可以增加属性（函数，地址等）
{
    return this.a+this.b
}
let object = new A(2,3);//new一个对象实例
 // object = {
 // "a" : 2,
 // "b" : 3
 //
 // }
console.log(object.sum())//调用构造函数里面需要的属性求值
function B(a,b){
    this.a=a,
        this.b=b
}
// B.prototype.sum=function ()
// {
//     return this.a+this.b
// }
let obj=new B (3,4);
console.log( object.sum.apply(obj))//apply和call都可以让一个新的构造函数B使用其他的构造函数如A的包括的属性的函数来求值
console.log(object.sum.call(obj))
console.log(object.sum.bind(obj))//需要函数，bound，该函数接收一个要进行绑定的值、下限和上限