import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from bs4 import BeautifulSoup as bs


class LLM:
    llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "너는 나의 충실한 조수이다. 그리고 너는 내가 제공하는 문서를 최대 3줄로 요약해 줄 것이다. 너가 요약한 문서는 SEO에 사용될 것이다.",
            ),
            ("human", "{text}"),
        ]
    )
    chain = prompt | llm

    def remove_html_tags(self, text):
        soup = bs(text, "lxml")
        clean_text = soup.text
        return clean_text

    def summarize_text(self, text):
        clean_text = self.remove_html_tags(text)
        return clean_text
