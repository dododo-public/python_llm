from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from typing import Callable
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser

class Parser(BaseOutputParser):
    def parse(self, text: str):
        return text

def llm_call(
        system_template,
        human_template, 
        param_provider: Callable[[], dict], 
        parser) -> str:
    try:
        chat_model = ChatOpenAI(model="gpt-4")
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=chat_model,
            prompt=chat_prompt,
            output_parser=parser
        )

        params = param_provider()
        return chain.run(**params)
    except Exception as e:
        raise e

if __name__ == "__main__":
    print("TBD")