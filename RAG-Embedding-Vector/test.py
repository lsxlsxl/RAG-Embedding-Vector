import os
from openai import OpenAI

# 设置环境变量（或者确保系统环境变量中已有）
os.environ["OPENAI_API_KEY"] = "your api key"

client = OpenAI()


models = client.models.list()
print("认证成功，可用模型：")
for model in models.data:
    print(" -", model.id)

