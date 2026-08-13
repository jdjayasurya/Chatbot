import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

class chatbot:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
    def initialize_llm(self):
        llm = ChatGroq(model="llama-3.1-8b-instant", api_key=self.api_key)
        return llm
    
    def chain_model(self, llm):
        prompt = PromptTemplate.from_template("You are assitant, and answer for the queries {question} in 2 lines")
        chain = prompt | llm | StrOutputParser()
        return chain
    
if __name__ == "__main__":
    bot = chatbot()
    llm = bot.initialize_llm()
    chain = bot.chain_model(llm)
    while True:
        query = input("Type a query: ")
        if str(query) == "exit":
            break
        else:
           result = chain.invoke(query)
           print(result)

    
