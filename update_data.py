import requests

# 原始链接地址
url = "https://github.com/ignaciocastro/a-dove-is-dumb/blob/main/list.txt"  # 这里替换为实际的 GitHub 链接

# 获取数据
response = requests.get(url)
lines = response.text.splitlines()

# 处理数据
processed_lines = []
for line in lines:
    if line.startswith("#"):
        # 处理注释行
        processed_lines.append(line)
    else:
        # 处理数据行，修改前缀
        processed_lines.append(f"aabb, {line.split(' ')[1]}")

# 保存数据到文件
with open("updated_data.txt", "w") as f:
    for line in processed_lines:
        f.write(line + "\n")
