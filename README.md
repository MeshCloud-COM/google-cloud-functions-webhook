# google-cloud-functions-webhook

### 创建飞书告警机器人

![image](https://user-images.githubusercontent.com/10955940/167241510-c179bb52-201f-4d02-92e6-74d84cdea870.png)

自定义机器人 获取 webhook 地址    

### 创建一个 Webhook 使用 Cloud Function 

##### 配置
![image](https://user-images.githubusercontent.com/10955940/167241523-38d7fa28-1cf0-4dea-876c-8a810e8be34b.png)

* 设置Function名字 google-cloud-functions-feishu
* 设置Authentication  Allow unauthenticated invocations

##### 编码
![image](https://user-images.githubusercontent.com/10955940/167241527-461f3373-d5c6-41d0-a194-35c133921bed.png)

* 设置 Runtime   Python 3.8
* 设置 Entry point  feishu_alert
* 设置 FEISHU_WEBHOOK_URL 为创建的 feishuwebhook 地址
![image](https://user-images.githubusercontent.com/10955940/167241539-8bb20c73-15ae-4dc1-aa51-fd618a6cbfc5.png)


设置 requirements.txt  中添加依赖 requests==2.25.1
![image](https://user-images.githubusercontent.com/10955940/167241546-d79ecea8-72a8-4d8b-83a8-09526a587757.png)


获取 Google Cloud Functions 的地址 https://us-central1-spoton-project.cloudfunctions.net/xxxxxx

### 创建 Monitoring 通知通道  

![image](https://user-images.githubusercontent.com/10955940/167241559-ed03ae37-1f66-4dfb-9a4a-73d0f76f6411.png)
关联 Google Cloud Functions 的地址
![image](https://user-images.githubusercontent.com/10955940/167241564-9c3e15e1-2aad-4c08-8d60-6cd259560d16.png)


### 创建 Logging alert

##### 设置过滤条件
![image](https://user-images.githubusercontent.com/10955940/167241572-b5166373-0208-415d-9ba3-3aafceacb21c.png)


##### 确认过滤条件
![image](https://user-images.githubusercontent.com/10955940/167241581-a2a7d66a-4460-4a66-a20c-c2d453e39619.png)


##### 设置通知频率和间隔
![image](https://user-images.githubusercontent.com/10955940/167241586-a290e791-f38b-42f0-b5c4-b48479f7b7a4.png)


##### 设置通知通道
<img width="1913" alt="image" src="https://user-images.githubusercontent.com/10955940/167241983-aaf80877-08e4-40be-a0e7-0e9cd6f7a786.png">

### 参考资料
* https://cloud.google.com/monitoring/alerts
* https://cloud.google.com/monitoring/support/notification-options
