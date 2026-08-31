from langchain_openai import ChatOpenAI
from env import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL

llm = ChatOpenAI(
    model=MODEL,
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    temperature=0,z
)

try:
    response = llm.invoke("请只回复：API 调用成功")
    print("模型回复：")
    print(response.content)
except Exception as e:
    print("调用失败：")
    print(type(e).__name__, e)
