# 说明文档


### Google Cloud Functions 设置
* Python version: 3.8
* requests version:  2.25.1
* Entry point：  triggered_http

### 环境变量 设置
* 飞书 WEBHOOK_URL = "http://xxxx"

### 注意事项 
triggered_http设置Authentication Allow unauthenticated invocations


## 示例 一  通过 GCP Monitoring 创建告警消息到飞书 


### 创建飞书告警机器人

![image](https://user-images.githubusercontent.com/10955940/167241510-c179bb52-201f-4d02-92e6-74d84cdea870.png)

自定义机器人 获取 webhook 地址    

### 使用 Cloud Function 创建一个 Webhook 

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

### 创建 Monitoring 告警
![image](https://user-images.githubusercontent.com/10955940/167338374-3dc5ec84-8b3d-46a0-b0da-938585ced1ec.png)
![image](https://user-images.githubusercontent.com/10955940/167338391-168fc0a6-9280-4c38-8af4-2dc09e6a65cd.png)
![image](https://user-images.githubusercontent.com/10955940/167338409-e6300ed0-14e5-4dbb-b4ab-885edcb457db.png)


## 示例二 Logging alert

##### 设置过滤条件
![image](https://user-images.githubusercontent.com/10955940/167241572-b5166373-0208-415d-9ba3-3aafceacb21c.png)


##### 确认过滤条件
![image](https://user-images.githubusercontent.com/10955940/167241581-a2a7d66a-4460-4a66-a20c-c2d453e39619.png)


##### 设置通知频率和间隔
![image](https://user-images.githubusercontent.com/10955940/167241586-a290e791-f38b-42f0-b5c4-b48479f7b7a4.png)


##### 设置通知通道
<img width="1913" alt="image" src="https://user-images.githubusercontent.com/10955940/167241983-aaf80877-08e4-40be-a0e7-0e9cd6f7a786.png">



### 测试
执行虚机关机操作，告警信息会通知到飞书群

##### 日志数据 json 示例

```json
{
  "incident": {
    "incident_id": "0.opqiw61fsv7p",
    "scoping_project_id": "internal-project",
    "scoping_project_number": 12345,
    "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.lxfiw61fsv7p?project=internal-project",
    "started_at": 1577840461,
    "ended_at": 1577877071,
    "state": "closed",
    "resource_id": "11223344",
    "resource_name": "internal-project gke-cluster-1-default-pool-e2df4cbd-dgp3",
    "resource_display_name": "gke-cluster-1-default-pool-e2df4cbd-dgp3",
    "resource_type_display_name": "VM Instance",
    "resource": {
      "type": "gce_instance",
      "labels": {
        "instance_id": "11223344",
        "project_id": "internal-project",
        "zone": "us-central1-c"
      }
    },
    "metric": {
      "type": "compute.googleapis.com/instance/cpu/utilization",
      "displayName": "CPU utilization",
      "labels": {
        "instance_name": "the name of the VM instance"
      }
    },
    "metadata": {
      "system_labels": { "labelkey": "labelvalue" },
      "user_labels": { "labelkey": "labelvalue" }
    },
    "policy_name": "Monitor-Project-Cluster",
    "policy_user_labels" : {
        "user-label-1" : "important label",
        "user-label-2" : "another label"
    },
    "condition_name": "VM Instance - CPU utilization [MAX]",
    "threshold_value": "0.9",
    "observed_value": "0.835",
    "condition": {
      "name": "projects/internal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789",
      "displayName": "VM Instance - CPU utilization [MAX]",
      "conditionThreshold": {
        "filter": "metric.type=\\"compute.googleapis.com/instance/cpu/utilization\\" resource.type=\\"gce_instance\\" metadata.system_labels.\\"state\\"=\\"ACTIVE\\"",
        "aggregations": [
          {
            "alignmentPeriod": "120s",
            "perSeriesAligner": "ALIGN_MEAN"
          }
        ],
        "comparison": "COMPARISON_GT",
        "thresholdValue": 0.9,
        "duration": "0s",
        "trigger": {
          "count": 1
        }
      }
    },
    "documentation": {
      "content": "TEST ALERT\n\npolicy.name=projects/internal-project/alertPolicies/1234567890123456789\n\npolicy.display_name=Monitored-Project-NO-GROUPBY\n\ncondition.name=projects/nternal-project/alertPolicies/1234567890123456789/conditions/1234567890123456789\n\ncondition.display_name=VM Instance - CPU utilization [MAX]\n\nproject=internal-project\n\nresrouce.project=internal-project \n\nDONE\n",
      "mime_type": "text/markdown"
    },
    "summary": "CPU utilization for internal-project gke-cluster-1-16-default-pool-e2df4cbd-dgp3 with metric labels {instance_name=gke-cluster-1-default-pool-e2df4cbd-dgp3} and system labels {state=ACTIVE} returned to normal with a value of 0.835."
  },
  "version": "1.2"
}
```


### 参考资料


* https://cloud.google.com/monitoring/alerts
* https://cloud.google.com/monitoring/support/notification-options
* https://cloud.google.com/monitoring/support/notification-options#webhooks
