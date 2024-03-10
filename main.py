from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits.python.base import create_python_agent
from langchain_experimental.agents import create_csv_agent
from langchain_experimental.tools.python.tool import PythonREPLTool

# initializes an agent with prefix to run python code
# spawns new process and runs python code in it
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
import qrcode

load_dotenv()


def main():
    print("Hello Langchain!")
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        tool=PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # python_agent_executor.run(
    #     """Generate and save in the current working directory 15 QRCodes
    #                           that point to https://www.linkedin.com/in/anair99/, you have qrcode package installed already"""
    # )
    csv_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        path=r"episode_info.csv",
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    # csv_agent.run("""How many columns are there in the file episode_info.csv?""")
    # csv_agent.run("""From the file episode_info.csv print seasons in the ascending order of the number of episodes they have""")

    routing_agent = initialize_agent(
        tools=[
            Tool(
                name="PythonAgent",
                func=python_agent_executor.run,
                description="""Useful when you need to transform natural language and write from it python and execute the python code
                returning the results of the code execution, 
                DO NOT SEND PYTHON CODE TO THIS TOOL""",
            ),
            Tool(
                name="CSVAgent",
                func=csv_agent.run,
                description="""Useful when you need to answer question over the episode_info.csv file
                 takes the entire question as an input and returns the answer after running the pandas calculations""",
            ),
        ],
        llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"),
        agent_type=AgentType.OPENAI_FUNCTIONS,  # wrapper to implement function calling so openai will select which tool to use
        verbose=True,
    )  # routing_agent is a simple router agent that routes the input to the correct agent based on the input

    routing_agent.run(
        """From the file episode_info.csv print seasons in the ascending order of the number of episodes they have"""
    )
if __name__ == "__main__":
    main()
