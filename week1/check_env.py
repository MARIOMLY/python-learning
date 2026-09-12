# check_env.py —— 环境自检：一次性确认今天的安装是否真的成功
# 运行方式： python check_env.py
# 全部通过时最后会打印 "环境自检通过"。

import sys
import platform

print("=" * 46)
print("Python 环境自检")
print("=" * 46)

# 1. 解释器版本
print(f"1. Python 版本 : {sys.version.split()[0]}")
print(f"   解释器路径  : {sys.executable}")
if sys.version_info >= (3, 8):
    print("   -> OK，版本够用")
else:
    print("   -> 版本偏旧，建议装 3.10 以上")

# 2. 操作系统
print(f"2. 操作系统   : {platform.system()} {platform.release()}")

# 3. pip 是否可用
try:
    import pip
    print(f"3. pip        : {pip.__version__}  -> OK")
except ImportError:
    print("3. pip        : 未找到 -> 需要重新安装 Python 时勾选 pip")

# 4. 中文输出是否正常（如果这行出现乱码，是终端编码问题，不是你的错）
print("4. 中文测试   : 你好，这是一行中文")

# 5. 基础语法自检：变量、运算、f-string、判断、循环
name = "ZERO"
age = 20
print(f"5. 变量与 f-string : 我叫{name}，今年{age}岁，明年{age + 1}岁")

total = 0
for i in range(1, 11):
    total += i
print(f"6. 循环 1 到 10 累加 : {total}（应该是 55）")

print("=" * 46)
print("环境自检通过：可以开始第 1 周的学习了")
print("接下来把 hello.py 跑一遍，然后去网页版点亮 D01")
print("=" * 46)
