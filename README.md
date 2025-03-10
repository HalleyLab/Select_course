<div align = 'center'>
<h1>自动选课 Automatic Course Selection</h1>
一种易于理解和实现的选课脚本构建方法
</div>

## 简介
生活中我们经常会遇到需要通过在浏览器中与网页交互进行选课、抢票等操作，然而由于网速、手速等原因，结果往往不尽如人意。本项目旨在提供一种非常容易理解和自己构建脚本的思路，由于机器的操作速度往往较手动快，其成功率理论上应比手动操作高。

## 环境配置
**Python** 版本 **3.9** 以上！！请前往 **[Python官网](https://www.python.org/downloads/)** 下载对应版本！并安装Selenium包！

需要下载对应浏览器驱动 ( **[见下文](#download)** )！
```python
  pip install -U selenium
```

## 构建思路

通过开发者工具找到网页中特定元素的参数，再通过selenium库启动网页并模拟鼠标点击行为来进行机械性重复操作。

**<h4> 1. 网页组成</h4>**

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

#### 1.3 可以手动给元素赋予一个class或ID

按 1.2 中的方法只能同时对整个 html 文件中相同 TagName 的元素进行处理，然而在很多情况下我们需要对不同元素设置不同样式。html 语言允许我们在放入元素时设置 class 以及 ID 参数。

```html
<div class = "greeting" id = "hello">Hello World!</div>
```
这段 html 代码表明以 div 方式放入文本 "Hello World!" ，并令其属于 class -- "greeting"，同时为其赋予一个 ID -- "hello"。顾名思义，设置 **class 名称允许重复**，使得我们能对特定一类元素同时操作，而 **ID 名是唯一的**，让我们能快速找到特定元素操作。

**<h4> 2. 开发者工具</h4>**

以Google Chrome浏览器为例，从设置栏的更多工具中找到开发者工具即可打开开发者工具，或通过 **Ctrl + Shift + I** 或 **F12** 等快捷键也可打开。

开发者工具如下图所示。导航栏的第一个选项“元素”中展示了所显示网页对应的html代码。

![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig1.png)

将 html 代码中嵌套的元素不断展开，直到找到我们想要的元素内容，把鼠标放在对应代码上会发现网页中对应内容变为高亮，通过这种方法我们可以得到网页中特定内容的参数。例如从下图中我们可以得到上面的那段话在被放入网页时赋予了参数 **data-sourcepos** 和 **dir** ，值分别为 **"70:1-70:121"** 和 **"auto"**，并且文本以 **p** 的方式放入网页，此时把 **data-sourcepos** 理解为与 **1.3** 中 **ID** 类似的参数即可。

![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig2.png)

**<h4 id = "download"> 3. Selenium库</h4>**

Selenium 库允许我们通过Python打开浏览器访问网站，并模拟鼠标点击网页进行交互。可以在 [Selenium库官网](https://pypi.org/project/selenium/) 找到此库的安装方法和使用示例。 这个网站 ( https://selenium-python.readthedocs.io/ ) 也总结了 Python 的 Selenium 库的使用示例。

需要注意的是 Selenium 库需要驱动来与浏览器进行交互，从以下网站中可以下载对应浏览器的驱动，注意 **需要将驱动安装至与Python相同的路径中** （通常是 /user/bin 或者 /user/local/bin）。

* [Chrome](https://chromedriver.chromium.org/downloads)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

## 实操演示

这里以在Chrome浏览器进行选课操作为例。
### 1#
首先通过驱动打开所需网站。
```python
  driver = webdriver.Chrome()
  driver.get("http://xxx.xxx.edu/") # 填入本学校选课网址
```

### 2#
进入网站后，按照上面描述的方法找到进入按钮对应的元素参数，如下图，ID 为 "ssodl"，由于 ID 唯一，可以直接通过 ID 定位该按钮。

```python
  button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ssodl"))  
  ) # 通过按钮ID定位
  button.click()  # 点击按钮
```
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig3.png)

### 3#
进入登录界面后同理获得用户名、密码输入框以及登录按钮的 ID，输入并点击。 html 中的 button 元素代表的是以按钮方式放入，寻找这个 TagName 也能帮我们更快地在开发者工具中找到对应的按钮， input 代表以输入框的方式放入。
```python
  username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
  )
  password_input = driver.find_element(By.ID, "password")

  username_input.send_keys("username") # 输入用户名
  password_input.send_keys("password") # 输入密码

  login_button = driver.find_element(By.ID, "dl")
  login_button.click()  # 点击登录
```
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig4.png)

### 4#
登录后进入另一个操作页面，需要注意的是，此时 html 文件中出现了以 **iframe** 放入的元素，这代表着在网页内放入的元素是另一个完整的网页，然而我们的 driver 变量还停留在前面的网页中，需要把 driver 移至需要操作的内嵌网页内。
值得注意的是，这里的 **iframe** 没有特定的参数，所以在程序中需要以 **XPATH（自定义路径）** 定位，这个路径实际上是根据 TagName 逐级向下搜，可以在下文看到更具体的应用。
```python
  iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)  # 切换到 iframe
```
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig5.png)

### 5#
**可以在开发者工具中 Ctrl + F 打开查找直接搜索该元素中所含的文字快速寻找**。这里需要先点击选课管理再点击自主选课，由于这两个词在这个网页上基本没有重复，所以可以直接查找来在 html 文件中定位。
```python
  element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
          (By.XPATH, '//ul[@id="myGnmkdmTab"]//a[@data-topgndm="03"]')
        )
    )
  element.click()
```
这里的选课管理没有一个特征参数，所以我们尝试从它的上级开始定位。这段代码表示先找到 ID 为 "myGnmkdmTab" 的 ul 元素，再在这个元素的下级里找到 data-topgndm 参数为 "03" 的 a 元素。
即如下的代码结构。
```html
  <ul id = "myGnmkdmTab">
    ...
      <a data-topgndm = "03" ...>选课管理</a> <!-- 这是需要点击的选课管理元素 -->
    ...
  </ul>
```
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig6.png)

### 6#
定位下一个需要点击的"自主选课"按钮时，采取了另一个办法，因为"自主选课"这个元素除了 class 没有其他参数。
```python
  confirm_button = driver.find_element(By.XPATH, '//div[@id="panel_03"]//label[contains(text(), "自主选课")]')
  confirm_button.click()
```
这段代码表示先定位 id 为 "panel_03" 的 div 元素，再定位下级中含有文本 "自主选课" 的 label 元素。

![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig7.png)

### 7#
进入选课界面。需要注意的是，**如果选课界面是以打开新网页出现的，我们需要再次调整 driver 到新网页才能操作。** 可以通过下述代码实现。
```python
  main_window_handle = driver.current_window_handle # 应在 1# 中打开网站后直接设置主窗口
  WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # 等待窗口数量变为2，如果有更多网页需要通过 driver.window_handles 逐个判断
  for window_handle in driver.window_handles:
    if window_handle != main_window_handle:
      driver.switch_to.window(window_handle)
```

### 8#
现在假设需要选取专业基础课程下的会计学，并选择第一个教学班。这里会出现多个选课按钮，要注意所需教学班的选课按钮的特征参数，也可以用 and 连接所有参数均加入 XPATH。
```python
  general = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
      (By.XPATH, '//li[@kclbmc="专业基础课程"]')
        )
    ) # 定位专业基础课程
  general.click()

  accountancy = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
      (By.ID, 'kcmc_ECON1003F')
        )
    ) # 定位会计学菜单栏
  accountancy.click()

  selection_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
      (By.XPATH, '//button[@data-xkkh="(2024-2025-2)-ECON1003F-0013201-1" and @type="button"]')
        )
    ) # 定位选课按钮，注意确认不同选课按钮的哪一个参数是独特的，这里data-xkkh是特征参数
  selection_button.click()
```
可以发现在定位按钮时用EC.element_to_be_clickable()取代了EC.presence_of_element_located()，这是因为后者只要按钮出现就会进行点击，然而此时按钮可能还不能点击。

此外，元素必须要在视窗内才能点击，可以通过下述代码滑动网页来使其可见。
```python
  driver.execute_script("arguments[0].scrollIntoView(true);", selection_button) #滑动网页至元素可见
```
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig9.png)
![image](https://github.com/HalleyLab/Select_course/blob/main/figures/fig10.png)

### 9#
最后，如果想确认选课结果，可以检测网页弹窗，用上述同样的方法获取弹窗的元素参数，定位后用.text获取元素中文本。
```python
  popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-modal"]//p'))
    )
  if popup.text == '现在不是选课时间！':
    print(popup.text)
    driver.quit()  # 不是选课时间就退出网页
```
