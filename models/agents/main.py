from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    information = """
    
    """
    
    summary_template = """
    given the information {information} about I want you to create:
    1. a summary of the information in 1-2 sentences
    2. two insteresting facts about them 
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": information})
