import requests
import json

# 設定目標URL
url = 'https://search.opentix.life/search'

# 設定請求頭和請求體
headers = {
    'Content-Type': 'application/json'
}

# 這是一個範例請求體，根據實際需求進行修改
payload = {
    # "categoryFilter": ["音樂-管絃樂團"],
    # "cityFilter": ["臺北"],
    "language":"zh-CHT",
    # "sortBy":"ABOUT_TO_BEGIN"
}

# 發送POST請求
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 檢查回應狀態碼
if response.status_code == 200:
    # 解析回應數據
    data = response.json()
    # 處理並打印所需的數據
    print(data)
    # for event in data['hits']['hits']:
    #     print(f"Title: {event['_source']['title']}, Date: {event['_source']['date']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
