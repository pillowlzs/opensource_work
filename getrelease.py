import requests
import csv

# 定义获取所有 Releases 数据的函数
def get_all_releases(owner, repo, token=None):
    releases = []
    url = f'https://api.github.com/repos/{owner}/{repo}/releases'
    
    # 添加认证信息，如果提供了 token
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'

    while url:
        # 发送请求
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 将当前页的 Release 数据添加到 releases 列表中
            data = response.json()
            releases.extend(data)
            
            # 检查是否有下一页数据
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                break  # 没有下一页数据，退出循环
        else:
            print(f"Error {response.status_code}: {response.text}")
            break
    
    return releases

# 获取所有 Release 数据
owner = 'plotly'  # 仓库的拥有者
repo = 'plotly.py'  # 仓库名
token = 'your_token'  # 替换为你自己的 Token##################################替换token

# 调用函数获取 Release 数据
releases = get_all_releases(owner, repo, token)

# 将所有 Release 信息保存到一个文本文件
with open('releases_info.txt', 'w', encoding='utf-8') as file:
    for release in releases:
        file.write(f"Release Name: {release['name']}\n")
        file.write(f"Tag Name: {release['tag_name']}\n")
        file.write(f"Published at: {release['published_at']}\n")
        file.write(f"Body: {release['body']}\n")
        file.write('-' * 50 + '\n')

print("Data saved to releases_info.txt")

# 将所有 Release 信息保存到一个 CSV 文件
with open('releases_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Release Name', 'Tag Name', 'Published at', 'Body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()
    
    # 写入每个 Release 的数据
    for release in releases:
        writer.writerow({
            'Release Name': release['name'],
            'Tag Name': release['tag_name'],
            'Published at': release['published_at'],
            'Body': release['body']
        })

print("Data saved to releases_info.csv")
