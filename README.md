<div align = 'center'>
<h1>自动选课 Automatic Course Selection</h1>
一种易于理解和实现的选课脚本构建方法
</div>

## 简介
生活中我们经常会遇到需要通过在浏览器中与网页交互进行选课、抢票等操作，然而由于网速、手速等原因，结果往往不尽如人意。本项目旨在提供一种非常容易理解和自己构建脚本的思路，由于机器的操作速度往往较手动快，其成功率理论上应比手动操作高。

## 环境配置
**Python** 版本 **3.9** 以上！！请前往 **[Python官网](https://www.python.org/downloads/)** 下载对应版本！并安装Selenium包！
```python
  pip install selenium
```

## 构建思路

#### 1. 网页组成

本项目是基于与网页交互来构建脚本的，因此需要对网页的组成有基本认识。
简单而言，我们在浏览器中所看到的网页多以 **html语言** 编写，其传输遵循 **http协议** ，不论多复杂的网页，其 html 文件基本的构建思路都是放入一个个元素来充当网页的内容。
这些放入的元素有以下特点

#### 1.1 每个元素在被放入网页时会按特定类型的方式放入

```html
<div> Hello World!</div>
```
这段 html 代码代表要向网页中放入文本 "Hello World!" ，而它被放入的方式是 div。除了 div，html 语言还提供了很多种放入方式，如 a/p/span/section/li/ul/nav/h1/img。可以把这些被放入的元素按照放入的方式分为**块级元素**和**行内元素**。

**这种放入是可以叠加的**。
```html
<div>
  <a>
    Hello World!
  </a>
</div>
```
这段代码相当于先以 div 的方式放入了一个容器，再在这个容器中以 a 的方式放入文本 "Hello World!"。

#### 1.2 上述被放入时的方式可以作为索引

如果每个网页都只有 1.1 中提到的内容，每个网页就会同质化，所有的样式和交互方式都由 html 语言本身确定，而实际上并非如此，那是因为可以在 html 中嵌入 CSS 和 JavaScript 程序分别控制 html 中元素的展示样式和交互函数。
```css
div {
  margin: 20px;
  color: blue;
}
```
这段 CSS 代码表明将对应 html 文件中所有以 div 方式放入的元素的外边距 （两个相邻元素的距离） 设为 20px，将元素的颜色设置为蓝色。

```javascript
let contents = document.getElementsByTagName('div')
console.log(contents)
```
这段 JavaScript 代码表明获取对应 html 文件中所有以 div 方式放入网页的元素，并将其中的内容存入变量 contents，然后在控制台输出该变量。从该代码中可以直观发现，div 等类别在 JavaScript 中被称为 TagName。

#### 1.3 可以认为给元素赋予一个class或ID

按 1.2 中的方法只能同时对整个 html 文件中相同 TagName 的元素进行处理，然而在很多情况下我们需要对不同元素设置不同样式。html 语言允许我们在放入元素时设置 class 以及 ID 参数。

```html
<div class = "greeting" id = "hello">Hello World!</div>
```
这段 html 代码表明以 div 方式放入文本 "Hello World!" ，并令其属于 class -- "greeting"，同时为其赋予一个 ID -- "hello"。顾名思义，设置 **class 名称允许重复**，使得我们能对特定一类元素同时操作，而 **ID 名是唯一的**，让我们能快速找到特定元素操作。

#### 2. 开发者工具

以Google Chrome浏览器为例，从设置栏的更多工具中找到开发者工具即可打开开发者工具，或通过 **Ctrl + Shift + I** 或 **F12** 等快捷键也可打开。

开发者工具如下图所示。导航栏的第一个选项“元素”中展示了所显示网页对应的html代码。

![image](https://github.com/user-attachments/assets/c47a9968-65e6-48fa-975f-522eaac67bf8)

将 html 代码中嵌套的元素不断展开，直到找到我们想要的元素内容，把鼠标放在对应代码上会发现网页中对应内容变为高亮，通过这种方法我们可以得到网页中特定内容的参数。

![image](https://github.com/user-attachments/assets/fa36d674-b035-4a6a-82df-eec8d343f131)



