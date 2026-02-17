from app.agent import build_agent

agent = build_agent()

while True:
    question = input("\nAsk your agent: ")

    result = agent.invoke({"input": question})

    print("\nFinal Answer:\n", result["output"])
