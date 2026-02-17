from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.agent import build_agent

class AgentState(TypedDict):
    input: str
    output: str

def build_graph(memory=None, model: str = "gpt-4o-mini", temperature: float = 0, research_depth: str = "balanced"):
    agent = build_agent(memory, model=model, temperature=temperature, research_depth=research_depth)
    
    def run_agent(state: AgentState):
        result = agent.invoke({"input": state["input"]})
        return {"output": result["output"]}
    
    graph = StateGraph(AgentState)

    graph.add_node("researcher", run_agent)
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", END)

    return graph.compile()