<div align = 'center'>
<h1>自动选课 Automatic Course Selection</h1>
一种易于理解和实现的选课脚本构建方法
</div>

## 简介
生活中我们经常会遇到需要通过在浏览器中与网页交互进行选课、抢票等操作，然而由于网速、手速等原因，结果往往不尽如人意。本项目旨在提供一种非常容易理解和自己构建脚本的思路，由于机器的操作速度往往较手动快，其成功率理论上应比手动操作高。

## 环境配置
**Python** 版本 **3.9** 以上！！请前往 **[Python官网](https://www.python.org/downloads/)** 下载对应版本！

## 构建思路

#### 1. 网页组成

本项目是基于与网页交互来构建脚本的，因此需要对网页的组成有基本认识。
简单而言，我们在浏览器中所看到的网页多以 **html语言** 编写，其传输遵循 **http协议** ，不论多复杂的网页，其 html 文件基本的构建思路都是放入一个个元素来充当网页的内容。
这些放入的元素有以下特点

#### 1.1 每个元素在被放入网页时会按特定类型的方式放入

```html
<div> Hello World!</div>
```
这段html代码代表要向网页中放入文本 'Hello World!' ，而它被放入的方式是 div。除了 div，html 语言还提供了很多种放入方式，如 a/p/span/section/li/ul/nav/h1/img。可以把这些被放入的元素按照放入的方式分为**块级元素**和**行内元素**。

#### 1.2 上述被放入时的方式可以作为索引

如果每个网页都只有1.1中提到的内容，每个网页就会同质化，所有的样式和交互方式都由 html 语言本身确定，而实际上并非如此，那是因为可以在 html 中嵌入 CSS 和 JavaScript 程序分别控制 html 中元素的展示样式和交互函数。
```css
div {
  margin: 20px;
  color: blue;
}
```
这段 CSS 代码表明将 html 中所有以 div 方式放入的元素的外边距 （两个相邻元素的距离） 设为20px，将元素的颜色设置为蓝色。

```javascript
let contents = document.getElementsByTagName('div')
console.log(contents)
```
这段 JavaScript 
