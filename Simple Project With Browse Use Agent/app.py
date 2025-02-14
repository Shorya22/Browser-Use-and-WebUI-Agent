from browser_use import Agent,Browser,BrowserConfig
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os

google_api_key = os.getenv("google_api_key")

async def main():

    browser = Browser(
	config=BrowserConfig(
		chrome_instance_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
		disable_security=True,
	)
)
    
    agent = Agent(browser=browser,
        task= """"What is the current weather in Ahmedabad?""",
        
        llm= ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=google_api_key)
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

