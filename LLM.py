from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    openai_api_key="",
)

prompt = ChatPromptTemplate.from_messages(
    [("system", "최대 3문장으로 요약해줘"), ("user", {question})]
)

chain = prompt | llm

question = "진희는 강아지를 기르고있습니다. 진희가 기르는 동물은?"
