from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import Select
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(10)


# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://one.ahu.edu.cn')
wd.maximize_window()

wd.find_element(By.ID,'un').send_keys('你和学号')

wd.find_element(By.ID,'pd').send_keys('你的密码')

wd.find_element(By.ID,'index_login_btn').click()

time.sleep(5)

wd.find_element(By.XPATH,'//span[@class="fa fa-edit"]').click()
time.sleep(5)
windows = wd.window_handles   # 获取该会话所有的句柄
wd.switch_to.window(windows[-1])

wd.find_element(By.XPATH,'//span[@class="fa fa-edit"]').click()
time.sleep(2)
wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[13]/div/div[1]/div[2]/div[1]/div/div/div/div[4]/div/div[1]/div[3]/p[1]/span').click()
time.sleep(15)
# 定位标签
iframe = wd.find_element(By.ID,'formIframe')
# 切换到标签上
wd.switch_to.frame(iframe)
#辅导员下拉
wd.find_element(By.XPATH,'/html/body/div[1]/div[6]/div[2]/div/button').click()

time.sleep(2)
#选择你的辅导员
wd.find_element(By.XPATH,'辅导员对应的XPATH').click()
time.sleep(1)
#出校
wd.find_element(By.XPATH,'/html/body/div[1]/div[8]/div[2]/div/div/div/div[1]/div/i').click()

#h合肥
wd.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[2]/div/div/div/div/div/i').click()
#事由
wd.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[2]/div/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[2]/div/input').send_keys('你的')
#出行路线
wd.find_element(By.XPATH,'/html/body/div[1]/div[12]/div[2]/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[12]/div[2]/input').send_keys('你的')
#出行方式
wd.find_element(By.XPATH,'/html/body/div[1]/div[13]/div[2]/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[13]/div[2]/input').send_keys('你的')
#导师知情
wd.find_element(By.XPATH,'/html/body/div[1]/div[14]/div[2]/div/div/div/div[1]/div/i').click()
#日期
elmdate=wd.find_element(By.XPATH,'/html/body/div[1]/div[8]/div[4]/input')
js='arguments[0].removeAttribute("readonly");'
wd.execute_script(js, elmdate)
time.sleep(2)
# 今天
today = datetime.date.today()
# 昨天
yesterday = today - datetime.timedelta(days=1)
# 明天
tomorrow = today + datetime.timedelta(days=1)
elmdate.clear()
elmdate.send_keys(str(tomorrow))
#确认申请
wd.find_element(By.XPATH,'/html/body/div[1]/div[16]/div[2]/div/div/div/div/div/i').click()
#上传附件
upload=wd.find_element(By.XPATH,'/html/body/div[1]/div[15]/div[2]/div/span/input')
upload.send_keys(r'文件路径')  
time.sleep(15)  
#切换回窗口
wd.switch_to.parent_frame()
#申请按钮
wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[13]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[3]/div[1]/button').click()
time.sleep(20)
wd.quit()