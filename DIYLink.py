import requests
import json

# API 端点 URL
url = "https://console.diylink.net/api/user/region/list"


# 请求头,填写自己的
headers = {
    "Cookie": "111",
    "Token": '222'
}

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 解析 JSON 响应数据
    data = json.loads(response.text)

    # 访问响应代码和消息
    print(f"Response Code: {data['code']}")
    print(f"Response Message: {data['msg']}")

    # 遍历每个地区的数据
    for region in data['data']:
        print(f"\nRegion: {region['name']}")
        print(f"Icon URL: {region['icon_url']}")
        print(f"VM Count: {region['vm_count']}")
        print(f"App Count: {region['app_count']}")
        print(f"Need to Apply: {region['need_to_apply']}")
        print(f"Cluster Configured: {region['cluster_configured']}")

        # 访问子区域数据
        print("Children:")
        for child in region['children']:
            print(f"  - {child['name']}")
else:
    print(f"Request failed with status code: {response.status_code}")