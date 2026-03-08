from agent.langgraph_agent import build_agent


agent = build_agent()


def run_agent(repo):

    result = agent.invoke({
        "repo": repo
    })

    print("\n INVESTIGATION COMPLETE\n")

    print(result["report"])


def chat():

    print("\nAI SRE Agent\n")
    print("Type 'investigate <repo>'")
    print("Example:")
    print("investigate saayam-for-all/webapp\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if user_input.startswith("investigate"):

            repo = user_input.replace("investigate", "").strip()

            print("\nAgent investigating...\n")

            run_agent(repo)

        else:

            print("Unknown command")


if __name__ == "__main__":
    chat()