# 傻瓜式出入校申请自动化，走读用，傻瓜式讲解
通过selenium实现安徽大学出入校申请，方便走读使用  
功能：自动化定时申请出校/入校
## 准备工作：  
### 1.python  
* [安装python](https://blog.csdn.net/hugo233/article/details/122686074)
### 2.selenium与ChromeDriver
* [安装selenium与ChromeDriver](https://www.cnblogs.com/duoba/p/8968474.html)  
 也可以看这个视频教程  
>   > [视频教程](https://www.bilibili.com/video/BV1Z4411o7TA?p=2&vd_source=3e3da0266630caedc79e101d7aab0742)  
### 3.收藏事项
在智慧安大中将在校学生临时初入校园备案表加入收藏，点击该事项右上角的信号。  
> 确保收藏后这一事项在 点击 办事大厅——服务事项 这一步骤后出现在页面第一个
> 
---
## 操作步骤：  
### 1.下载上面两个python文件  
[下载github文件](https://blog.csdn.net/qq_41185868/article/details/106156697)  
### 2.更改代码  
#### 2.1更改学号密码  
    wd.find_element(By.ID,'un').send_keys('你和学号')
    wd.find_element(By.ID,'pd').send_keys('你的密码')
找到这两个部分，在引号中间输入自己的学号密码
#### 2.2
