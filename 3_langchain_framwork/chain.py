#Create Stuff Documents Chain
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

prompt = ChatPromptTemplate.from_messages(
    [("system", "Burada ismi geçen kişilerin en sevdiği rengi tek tek yaz:\n\n{context}")]
)


docs = [
    Document(page_content="Gamze kırmızıyı sever ama sarıyı sevmez"),
    Document(page_content="Murat yeşili sever ama maviyi sevdiği kadar değil"),
    Document(page_content="Burak'a sorsan favori rengim yok der ama belli ki turuncu rengi seviyor")
]


chain_1 = create_stuff_documents_chain(llm, prompt)

print(chain_1.invoke({"context": docs}))



#Create OpenAI Function Runnable Chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

class Insan(BaseModel):
    """Bir insan hakkında tanımlayıcı bilgiler"""

    isim: str = Field(..., description="Kişinin ismi")
    yas: int = Field(..., description="Kişinin yaşı")
    meslek: Optional[str] = Field(None, description="Kişinin mesleği")


class Sehir(BaseModel):
    """Bir şehir hakında tanımlayıcı bilgiler"""

    isim: str = Field(..., description="Şehrin ismi")
    plaka_no: str = Field(..., description="Şehrin plaka numarası")
    iklim: Optional[str] = Field(None, description="Şehrin iklimi")

llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Sen varlıkları kaydetmek konusunda dünyanın en başarılı algoritmasısın"),
        ("human", "Şu verdiğim girdideki varlıkları kaydetmek için gerekli fonksiyonlara çağrı yap: {input}"),
        ("human", "İpucu: Doğru formatta yanıtladığından emin ol")
    ]
)

chain_2 = create_openai_fn_runnable([Insan, Sehir], llm, prompt)

print(chain_2.invoke({"input": "Aydın 34 yaşında, başarılı bir bilgisayar mühendisiydi"}))
print(chain_2.invoke({"input": "Aydın'da hava her zaman sıcaktır ve bu yüzden 09 plakalı araçlarda klima hep çalışır"}))

