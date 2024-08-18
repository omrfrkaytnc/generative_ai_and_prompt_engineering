from crewai import Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import crewhelper
import os

os.environ["OPENAI_API_KEY"] = os.getenv("openai_apikey")
os.environ["GOOGLE_API_KEY"] = os.getenv("google_apikey")


llm_gemini = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)
llm_gpt = ChatOpenAI(model="gpt-4-0125-preview", temperature=0)

instructions=f"""Profesyonel hayatta kişilerin karakteristik özelliklerini belirlemekte kullanmak üzere bir kişilik testi geliştir.
Bu testi geliştirirken Big Five, 16 Personalities veya 4 Renk yaklaşımı bilinen ve geniş kabul görmüş yaklaşımlara uyumlu olarak hareket et.
Geliştirdiğin kişilik testi, kişilik tiplerini ve bunların her birinin karakter özelliklerini barındırıyor olmalı.
Her bir kişilik tipini ve karakteri test etmek için sorular yazmalısın. 
Bu soruların yanıtına göre nasıl kullanıcıyı bir tiple ve karakter özellikleriyle bağlantılandıracağına dair bir yönteme karar vermelisin. 
Bu testi yapan kişilere göstermek için her bir kişilik tipinin kısa özet metinleri de olmalı. 
Bu kriterlere uygun olarak kişilik testinin içeriklerini hazırladıktan sonra tüm bu içerikleri içerecek şekilde bir Python Streamlit uygulaması yazmalısın. 
Böylece kullanıcılar bu uygulamayı kullanarak kişilik tiplerini öğrenebilirler. 
Derin bir nefes al ve bu görevleri birer birer yerine getir.
"""

test_expert = crewhelper.test_expert(llm=llm_gpt)
sotware_engineer = crewhelper.software_engineer(llm=llm_gpt)
test_consultant = crewhelper.test_consultant(llm=llm_gpt)

test_development_task = crewhelper.create_test_task(instructions=instructions, agent=test_expert)
code_task = crewhelper.create_code_task(instructions=instructions, agent=sotware_engineer)
test_review_task = crewhelper.create_review_task(instructions=instructions, agent=test_consultant)


crew = Crew(
    agents = [
        test_expert, 
        sotware_engineer,
        test_consultant
        ],
    tasks = [
        test_development_task, 
        test_review_task,
        code_task,
        ],
    verbose = True,
    process=Process.sequential
)

result = crew.kickoff()

print("*"*100)
print("İşte Sonuçlar:")
print("*"*100)
print("*"*100)
print(result)