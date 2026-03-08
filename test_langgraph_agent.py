from agent.langgraph_agent import build_agent

agent = build_agent()

result = agent.invoke({
    "repo": "saayam-for-all/webapp"
})

print("\nFINAL RESULT:\n")
print(result)