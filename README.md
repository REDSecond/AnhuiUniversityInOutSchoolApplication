# 傻瓜式出入校申请自动化   
通过selenium实现安徽大学出入校申请，方便走读使用  
## 功能：  
> 自动化每天定时申请出校/入校  
> 自定义日期出行路线等信息
> 自定义申请时间
## 准备工作：  
### 1.python和Chrome    
-[如何安装python](https://blog.csdn.net/hugo233/article/details/122686074)  
-安装Chrome浏览器  
### 2.selenium与ChromeDriver
* [如何安装selenium与ChromeDriver](https://www.cnblogs.com/duoba/p/8968474.html)  
 也可以看这个[视频教程](https://www.bilibili.com/video/BV1Z4411o7TA?p=2&vd_source=3e3da0266630caedc79e101d7aab0742)  
 你可能需要：[python pip教程](https://blog.csdn.net/HHYZBC/article/details/123548294)
### 3.收藏事项
在智慧安大中将在校学生临时初入校园备案表加入收藏，点击该事项右上角的星号。  
#### 确保收藏后这一事项在 点击 办事大厅——服务事项 这一步骤后出现在页面第一个
<img src=https://github.com/REDSecond/AnhuiUniversityInOutSchoolApplication/blob/main/%E5%9B%BE1.png width=70% />  

----
## 操作步骤：
### 两个python文件都要进行以下操作
### 1.下载上面两个python文件  
inschool.py（入校申请）  
outschool.py（出校申请）  
[如何下载github文件](https://blog.csdn.net/qq_41185868/article/details/106156697)  
### 2.更改代码  
#### 2.1输入学号密码 
```python
    wd.find_element(By.ID,'un').send_keys('你的学号')
    wd.find_element(By.ID,'pd').send_keys('你的密码')
```
##### 找到这两个部分，在引号中间输入自己的学号密码
#### 2.2更改辅导员姓名  
一、点击辅导员选项下拉按钮，右键自己辅导员姓名，点击检查  
二、右键右侧高亮区域，右键选中，点击copy->full Xpath
##### 如下图所示  
<img src=https://github.com/REDSecond/AnhuiUniversityInOutSchoolApplication/blob/main/%E5%9B%BE2.png  />  
找到下面这行代码，将刚才copy的内容粘贴到两个引号中  

```python
#选择你的辅导员  
wd.find_element(By.XPATH,'辅导员对应的XPATH').click()
```
#### 2.3输入内容  
在两个引号中输入自己的信息  
```python
wd.find_element(By.XPATH,'/html/body/div[1]/div[10]/div[2]/div/div/div/div/div/i').click()
#事由
wd.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[2]/div/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[11]/div[2]/div/input').send_keys('你的事由')
#出行路线
wd.find_element(By.XPATH,'/html/body/div[1]/div[12]/div[2]/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[12]/div[2]/input').send_keys('你的出行路线')
#出行方式
wd.find_element(By.XPATH,'/html/body/div[1]/div[13]/div[2]/input').clear()
wd.find_element(By.XPATH,'/html/body/div[1]/div[13]/div[2]/input').send_keys('你的出行方式')
```
#### 2.4上传文件  
在下面代码中两个引号之间填入你的附件路径  
```python
#上传附件
upload=wd.find_element(By.XPATH,'/html/body/div[1]/div[15]/div[2]/div/span/input')
upload.send_keys(r'文件路径') 
```
[查找文件路径教程](https://jingyan.baidu.com/article/7e440953c3dc1d6ec1e2ef0e.html)  
此教程复制的文件路径为文件所在文件夹路径，还需要在后面加上自己文件的名称与格式  
例如找到的文件路径为：  
C:\Users\lenovo\desktop，文件名为aaa，格式为jpg  
那么代码中需要填入的路径为：C:\Users\lenovo\desktop\aaa.jpg  
#### 2.5选择日期  
默认填入程序运行时第二天的日期。  
如果需要填入当天的日期，只需要将下面代码中的tomorrow改为today即可。  
```python
elmdate.clear()
elmdate.send_keys(str(tomorrow))
```
#### 2.6程序定时运行
这个很简单，点击下方链接教程即可  
在最后一步中填入inschool和outschool两个文件的路径（查找地路径方法见2.4）  
[如何定时运行程序](http://www.ujiaoshou.com/xtjc/094429980.html)  
建议为inschool和outshool两个文件分别设置任务计划，间隔10分钟以上  
在设定时间电脑保持开机并联网状态即可
