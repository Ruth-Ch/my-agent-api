import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

@tool
def get_trending_topics() -> str:
    """Returns current trending YouTube topics."""
    return (
        "Trending YouTube topics right now include fitness challenges, "
        "morning routines, AI tools, productivity content, day-in-the-life vlogs, "
        "healthy meal ideas, and personal growth videos."
    )

@tool
def get_content_ideas(niche: str) -> str:
    """Get content format ideas for a given niche or topic.
    Use this when the user asks for content ideas, formats, or creative suggestions."""
    return (
        f"Content ideas for {niche}: "
        "1) Carousel post — break down a common myth in your niche into 5 slides. "
        "2) Reel — show a before and after transformation in 30 seconds. "
        "3) Story series — share 3 quick tips over 3 consecutive days. "
        "4) Long-form video — do a full tutorial or deep dive on a topic your audience keeps asking about."
    )

tools = [get_trending_topics, get_content_ideas]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

system_prompt = """
You are AlgoRhythm, a helpful assistant for content strategy.

Use:
- get_trending_topics when the user asks what is trending on YouTube right now
- get_content_ideas when the user asks for content formats or creative suggestions for a niche

Always use the appropriate tool when relevant.
"""

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=system_prompt
)