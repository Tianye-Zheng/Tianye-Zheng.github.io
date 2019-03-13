---
layout: post
title:  "JavaScript笔记"
date:   2019-03-13
desc: ""
keywords: ""
categories: [Java]
tags: []
icon: icon-html
---

整理自慕课网 JavaScript 入门篇/进阶篇，上学期记的，从 Ulysses 搬过来，然后准备换用另一个笔记软件 “熊掌记” 了

<br />
# Chap1

`<script type = “text/javascript”> JavaScript代码写在这里 </script>`

`引用JS外部文件： <script src = “script.js”></script>`

`单行注释 //  多行注释  /* */`

`var 变量名 区分大小写，需要先声明`

`判断语句 if () {} else {}`

`function 函数名()
{
	 函数代码;
}`

`<input type = “button” value = “click me“ onclick = “function()” />`

<br />
# Chap2

`document.write(var + “Hello world!” + “<br>”); 输出内容`

`alert(字符串或变量) 警告`

`confirm(str); 包括一个确定按钮和一个取消按钮`
`str:在消息对话框中要显示的文本  返回值：boolean值`

```
prompt(str1, str2);
	参数说明:
	str1: 要显示在消息对话框中的文本，不可修改
	str2: 文本框中的内容，可以修改
	返回值:
	点击确定按钮，文本框中的内容将作为函数返回值
	点击取消按钮，将返回null
```

`window.open([URL],[窗口名称],[参数字符串]);`

`window.close(); // 关闭本窗口`

`<窗口对象>.close(); // 关闭指定的窗口`

<br />
# Chap3

`<a href=“http://www.imooc.com”>JavaScriptDOM</a>`
`元素节点   属性节点  文本节点`

`document.getElementById(“id”);
通过id获得元素对象`

`Object.innerHTML
innerHTML属性用于获取或替换HTML元素的内容`

`Object.style.property = new style;`
`Object是获取的元素对象, eg:`
`mychar.style.color = “red”;`

`Object.style.display = value;`
`“none”  此元素不会被显示`
`“block” 此元素将显示为块级元素（即显示）`

`object.className = classname  为某个元素指定一个css样式来改变外观`

<br />
# Chap4 数组

`创建数组语法 var myarray = new Array();`

`创建时可指定长度，但实际上数组都是变长的`

`第一种方法：
var myarray = new Array(66,80,90,77,59); // 创建数组时同时赋值`

`第二种方法：
var myarray = [66,80,90,77,59]; // 直接输入一个数组（称“字面量数组”）`

`只需使用下一个未用的索引，任何时刻可以不断向数组增加新元素`

`myarray.length; // 获得数组myarray的长度`
`javascript数组的length属性是可变的`

```
二维数组的定义方法一：
var myarr = new Array();
for(var i=0;i<2;i++)
{
	myarr[i] = new Array();
	for(var j=0;j<3;j++)
	{
		myarr[i][j] = ……;
	}
}
二维数组的定义方法二：
var myarr = [[0,1,2],[1,2,3]];
```

<br />
# Chap5 函数

```
function myfunc([参数])
{
	函数代码；
	[return]
}
函数调用 情况一：在<script>标签内调用，调用函数直接写函数名
情况二：在HTML文件中调用，如通过点击按钮后调用定义好的函数
```

<br />
# Chap6 JavaScript内置对象

```
indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置
语法：  stringObject.indexOf(substring, startpos)
substring: 必需，需检索的字符串
startpos: 可选整数参数，开始检索的位置，默认从首字母开始检索
返回第一次出现的位置

split() 方法将字符串分割为字符串数组，并返回此数组
语法：  stringObject.split(separator,limit)

substring() 方法用于提取字符串中介于两个指定下标之间的字符
语法：  stringObject.substring(startPos,stopPos)

substr() 方法从字符串中提取从 startPos位置开始的指定数目的字符串
语法：  stringObject.substr(startPos,length)

ceil() 方法可对一个数进行向上取整
语法:  Math.ceil(x)

floor() 方法可对一个数进行向下取整
语法:  Math.floor(x)

round() 方法可把一个数字四舍五入为最接近的整数
语法:  Math.round(x)

random() 方法可返回介于 0 ~ 1（大于或等于 0 但小于 1 )之间的一个随机数
语法:  Math.random();

join()方法用于把数组中的所有元素放入一个字符串。元素是通过指定的分隔符进行分隔的
语法：  arrayObject.join(分隔符)

slice() 方法可从已有的数组中返回选定的元素
语法：  arrayObject.slice(start,end)

sort()方法使数组中的元素按照一定的顺序排列
语法:   arrayObject.sort(方法函数)
如果不指定<方法函数>，则按unicode码顺序排列
```

<br />
# Chap7 浏览器对象

```
计时器 setInterval()
在执行时，从载入页面后每隔指定的时间执行代码 
语法:
setInterval(代码,交互时间);
参数说明：
1. 代码：要调用的函数或要执行的代码串。
2. 交互时间：周期性执行或调用表达式之间的时间间隔，以毫秒计（1s=1000ms）。
返回值:
一个可以传递给 clearInterval() 从而取消对"代码"的周期性执行的值。
调用函数格式(假设有一个clock()函数):
setInterval("clock()",1000)
或
setInterval(clock,1000)

clearInterval() 方法可取消由 setInterval() 设置的交互时间。
语法：
clearInterval(id_of_setInterval)
参数说明: id_of_setInterval：由 setInterval() 返回的 ID 值。
```