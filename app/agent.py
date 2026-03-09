from app.tools.rag_tools import rag_search
from app.tools.arxiv_tools import search_arxiv
from app.tools.web_search import web_search
from app.tools.calculator import calculator
from app.tools.wikipedia_tool import wikipedia_search
from app.tools.summarizer import summarize_text
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from app.config.llm import get_llm
from app.tools.dummy_tool import get_current_year
from app.prompts.agent_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

def build_agent(memory=None, model: str = "gpt-4o-mini", temperature: float = 0, research_depth: str = "balanced"):

    tools = [get_current_year, web_search, search_arxiv, rag_search, calculator, wikipedia_search, summarize_text]

    # Adjust system prompt based on research depth
    system_prompt = SYSTEM_PROMPT
    if research_depth == "deep":
        system_prompt += "\n\nIMPORTANT: Conduct thorough research. Use multiple tools and cross-reference sources. Provide detailed analysis."
    elif research_depth == "quick":
        system_prompt += "\n\nIMPORTANT: Provide quick, concise answers. Use 1-2 most relevant tools."

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    llm = get_llm(model=model, temperature=temperature)

    agent = create_tool_calling_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        return_intermediate_steps=True,  # ⭐ important
        memory=memory
    )

    return agent_executor
