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

