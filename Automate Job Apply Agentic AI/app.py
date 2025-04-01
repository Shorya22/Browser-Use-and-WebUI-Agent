from langgraph import Graph, Node
from browser_use import Agent, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

# Define the LinkedIn login credentials
linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure the browser
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        disable_security=True,
    )
)

# Create an agent with a language model
agent = Agent(
    browser=browser,
    llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=google_api_key)
)

# Define the nodes
class LinkedInLoginNode(Node):
    async def run(self):
        task = f"""
        1. Open LinkedIn login page.
        2. Enter the email: {linkedin_email} and password: {linkedin_password}.
        3. Click on the 'Sign In' button.
        """
        agent.task = task
        await agent.run()

class JobSearchNode(Node):
    async def run(self):
        task = """
        1. Navigate to the LinkedIn job search page.
        2. Search for 'AI Engineer' jobs.
        """
        agent.task = task
        await agent.run()

class JobApplicationNode(Node):
    async def run(self):
        task = """
        1. Click on the first job listing.
        2. Click on the 'Easy Apply' button.
        3. Fill out the required fields in the application form.
        4. Submit the application.
        """
        agent.task = task
        await agent.run()

# Create the graph
graph = Graph()

# Add nodes to the graph
login_node = graph.add_node(LinkedInLoginNode())
search_node = graph.add_node(JobSearchNode())
application_node = graph.add_node(JobApplicationNode())

# Add edges to define the workflow sequence
graph.add_edge(login_node, search_node)
graph.add_edge(search_node, application_node)

# Run the graph
async def main():
    await graph.run()

asyncio.run(main())