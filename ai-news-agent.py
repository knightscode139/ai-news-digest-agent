from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from tavily import TavilyClient
from pydantic import BaseModel, Field
from typing import Dict, Any, List

# Load environment variables from .env file
load_dotenv()

# Initialize Tavily client
tavily_client = TavilyClient()


# Define the web search tool
@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for today's most important AI news for an AI Engineer"""

    return tavily_client.search(
        query=query,
        topics='news',
        search_depth='advanced',
        max_results=10,
        time_range='day',
        include_raw_content=True
    )


# Define response schema
class AINews(BaseModel):
    title: str
    url: str
    explanation: str = Field(
        description="A detailed explanation (10 sentences minimum) covering: What happened, Why it's significant, How it impacts AI engineers or the industry"
    ) 

class AINewsDigest(BaseModel):
    news_items: List[AINews]


# Define system prompt
system_prompt = """
You are an AI News Assistant. Your job is to search for and explain the latest AI technology news.

When users ask about AI news:
1. Use the web_search tool to find recent AI news articles from the last 24 hours
2. Choose the 5 most important news items for an AI Engineer
3. Provide a detailed explanation (10 sentences minimum) for each news item that covers:
   - What happened
   - Why it's significant
   - How it impacts AI engineers or the industry
"""


# Create the agent
agent = create_agent(
    model="deepseek-chat",
    tools=[web_search],
    system_prompt=system_prompt,
    response_format=AINewsDigest
)


def get_ai_news(thread_id: str = "0") -> AINewsDigest:
    """Get the latest AI news."""

    response = agent.invoke({"messages": [HumanMessage(content="Is there new exciting news?")]})

    return response['structured_response']


def print_news(news_digest: AINewsDigest) -> None:
    """Print news items in a formatted way."""
    print("\n" + "="*80)
    print("AI NEWS DIGEST")
    print("="*80 + "\n")

    for i, item in enumerate(news_digest.news_items, 1):
        print(f"[{i}] {item.title}")
        print(f"URL: {item.url}")
        print(f"\n{item.explanation}\n")
        print("-" * 80 + "\n")


if __name__ == "__main__":
    # Get the latest AI news
    news = get_ai_news()

    # Print the news
    print_news(news)