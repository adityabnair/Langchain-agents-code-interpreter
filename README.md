# LangChain agent-based code interpreter
As the name suggests, this project aims to demonstrate the usage of tools, ReAct agents and how thier implementation can be used to effectively function as a functional code interpreter capable of analyzing and 
executing tasks after it has been given a user-defined prompt. 

Two types of Tools have been used here, the first being a python executor agent and the second; a CSV analyzing agent. The python executor is responsible for creating, running and executing python code after the
user provides a prompt for it. The sample prompt used in the project was to generate QRCodes pointing to my LinkedIn profile. 
The CSV analyzing agent on the other hand, reads a CSV file and responds to queries (by resorting to loading the CSV on a Pandas dataframe followed by the necessary operations) in order to calculate the correct 
results. The sample CSV file used here was the episode information list of the popular televsion series Seinfeld. 
Both these agents were created using the Langchain library containing pre-defined functions. 
A customized routing agent was created to switch between these two Tools accompanied by descriptions to help the openai function wrapper to switch between them as per the nature of the prompt. 
While not entirely perfect and still flaky in some aspects, the two Tools using these agents seem to perform fairly well to process simple queries occassionally giving incorrect answers and sometimes being unable
to decide on the right course of action. GPT 3.5 has been used here but according to relevant experimentation GPT 4 can also be used for more accurate ReAct observation, thoughts, results and final answers.

## Screenshots
![qrcode_screenshot_2](https://github.com/adityabnair/Langchain-agents-code-interpreter/assets/64246274/427a6f5f-9832-4be3-8e82-48ece145036c)
![qrcode_screenshot](https://github.com/adityabnair/Langchain-agents-code-interpreter/assets/64246274/190f7b2f-e4f6-4aa2-a9bd-8c4821262f22)
![image](https://github.com/adityabnair/Langchain-agents-code-interpreter/assets/64246274/bb1f34e4-492b-4030-94d4-be463d496523)



## Main Prerequisites

1. At least Python 3.10
2. Access to OpenAI's API credits for usage of gpt-3.5

### Running

1. Use pipenv to install python libraries from requirements.txt (a virtual environemnt is always recommended)
2. Add environment variable in a .env file to hold OpenAI's API key
3. Run main.py file 
4. Can re-run main.py file with other queries pertaining to python programming and CSV querying


## Acknowledgments

Thanks to @emarco177 for the langchain development course
