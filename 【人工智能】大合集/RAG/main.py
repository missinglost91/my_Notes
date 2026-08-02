# 一个openai示例工程
from openai import OpenAI
import os
# 加载.env文件
from dotenv import load_dotenv
load_dotenv(override=True)
QWEN_URL = os.getenv("QWEN_URL")
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_MODEL = os.getenv("QWEN_MODEL")

# 1. 直接在构造函数中设置中转站 API
client = OpenAI(
    base_url=QWEN_URL,
    api_key=QWEN_API_KEY,
)

completion = client.chat.completions.create(
    model=QWEN_MODEL,                    # 替换为您中转站支持的模型名
    messages=[
        {"role": "user", "content": "你来自哪个国家"}
    ],
    stream=True,
)

for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)