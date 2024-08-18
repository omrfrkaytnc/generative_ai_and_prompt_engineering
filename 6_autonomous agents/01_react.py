from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = os.getenv("google_apikey")
os.environ["TAVILY_API_KEY"] = os.getenv("tavily_apikey")

llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")
llm_gpt = ChatOpenAI(api_key=my_key_openai, model="gpt-4-0125-preview")

tools = [TavilySearchResults(max_results=1)]

#prompt = hub.pull("emreyz/react-turkce")
prompt = hub.pull("hwchase17/react")

llm = llm_gpt

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input": "Türkiye'de bir sonraki yerel seçimler hangi tarihte gerçekleştirilecek? Cevabı bulduktan sonra yanıtını Türkçe yaz."}, handle_parsing_errors=True)

print("*"*100)
print(f"Sorunuz Şuydu: {result['input']}")
print("*"*100)
print(f"Yanıt şu: {result['output']}")