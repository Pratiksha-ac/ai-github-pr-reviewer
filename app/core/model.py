from autogen_ext.models.openai import OpenAIChatCompletionClient
from app.config.settings import GEMINI_API_KEY, MODEL_NAME

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)