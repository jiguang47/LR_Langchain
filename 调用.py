import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("未找到系统环境变量 OPENAI_API_KEY")

if not OPENAI_BASE_URL:
    raise RuntimeError("未找到系统环境变量 OPENAI_BASE_URL")