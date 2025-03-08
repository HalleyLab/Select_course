from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # 确保chromedriver在系统路径中
driver.get("http://xxx.xxx.edu/")  # 目标网页
main_window_handle = driver.current_window_handle

# 显式等待按钮加载（最多等10秒）
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ssodl"))  # 通过按钮ID定位
)
button.click()

try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_input = driver.find_element(By.ID, "password")

    # 填写用户名和密码
    username_input.send_keys("username") # 改为登录所用的用户名
    password_input.send_keys("password")  # 改为登录所用的密码

    # 点击登录
    login_button = driver.find_element(By.ID, "dl")
    login_button.click()

    iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)  # 切换到 iframe

    # 选课管理
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//ul[@id="myGnmkdmTab"]//a[@data-topgndm="03"]')
        )
    )
    element.click()

    # 自主选课
    confirm_button = driver.find_element(By.XPATH, '//div[@id="panel_03"]//label[contains(text(), "自主选课")]')
    confirm_button.click()
    
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # 等待窗口数量变为2
    for window_handle in driver.window_handles:
        if window_handle != main_window_handle:
            driver.switch_to.window(window_handle)

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
      (By.XPATH, '//button[@data-xkkh="(2024-2025-2)-ECON1003F-0013201-1"]')
        )
    ) # 定位选课按钮，注意不同选课按钮的哪一个参数是独特的，这里data-xkkh是特征参数
    # driver.execute_script("arguments[0].scrollIntoView(true);", selection_button) #滑动网页至元素可见
    selection_button.click()

    popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-modal"]//p'))
    )
    if popup.text == '现在不是选课时间！':
        print(popup.text)
        driver.quit()
finally:
    driver.quit()
    pass