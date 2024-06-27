import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
)

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

print(
    chain.invoke(
        {
            "text": """대한민국 육군 제12보병사단. 일명 을지부대. 사단본부 비석에는 상승을지부대로 표시되어 있다. 표어는 <을지부대는 오직 전진할 뿐이다>를 사용한다. 경례구호는 '충성'. 1970년대와 1980년대 초에는 당백(일당백), 1997년 여름까지는 '단결'이었다. 다른 사단과 달리 병사를 병사가 아닌 '용사'라고 부른다.

사단본부는 <인제 가면 언제 오나, 원통해서 못 살겠네>에서 그 원통에 자리잡고 있다. 정확한 지명은 강원특별자치도 인제군 북면 원통리이며 북면사무소 소재지다. 물론 위 주소는 사단본부 소재지이며, 예하부대는 인제군 및 양구군, 고성군에 나뉘어 주둔하면서 <조국의 창끝, 산악의 방패>로서 그 사명을 충실히 완수하고 있다.

그러나 연이은 논란들과 하나 같이 가혹한 사단내 군기 혹은 괴롭힘 사건등으로 최악의 사단이란 이미지가 잡혀있다.
입대를 압둔 20대 남성은 12사단 신병교육대만큼은 제발 피하기를 바라는 분위기가 형성 될 정도이며 12사단으로 배정 받았다는 말만 꺼내도 뉴스 기사들을 보여주며 걱정의 눈초리를 받게 된다."""
        }
    ).to_json
)
