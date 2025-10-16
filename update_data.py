import requests

# 原始链接地址
url = "https://raw.githubusercontent.com/ignaciocastro/a-dove-is-dumb/refs/heads/main/list.txt"  # 请替换成你的原始数据链接

# 获取数据
response = requests.get(url)
lines = response.text.splitlines()

# 处理数据
processed_lines = []
for line in lines:
    # 保留注释
    if line.strip().startswith("#"):
        processed_lines.append(line)
    # 修改以 "0.0.0.0" 开头的数据行
    elif line.strip().startswith("0.0.0.0"):
        parts = line.strip().split()
        # 确保格式正确（有域名部分）
        if len(parts) == 2:
            processed_lines.append(f"DOMAIN,{parts[1]}")
    # 其他行（空行或异常格式）可忽略
    else:
        continue

# 保存处理结果到文件
with open("adobe_crack.list", "w") as f:  # 修改为 adobe_crack.txt
    for line in processed_lines:
        f.write(line + "\n")
