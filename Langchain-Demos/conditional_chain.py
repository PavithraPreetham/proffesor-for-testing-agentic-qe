from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal
import os

load_dotenv()

class Feedback(BaseModel):
    customer_name: str =Field(description="Name of the customer")
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")


pyparser = PydanticOutputParser(pydantic_object=Feedback)

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

prompt1 = PromptTemplate(template="""
Analyze the sentiment of the following feedback and classify it into positive or negative \n {feedback} \n {format_instructions}
""", input_variables=["feedback"], validate_template=True, partial_variables={'format_instructions': pyparser.get_format_instructions()})

chain1 = prompt1 | model | pyparser

positive_email_prompt = PromptTemplate(
    template="""
    Write a thank you email to the customer for giving a positive feedback about his recent purchase of IPhone 16.
    \n {feedback}
    """,
    input_variables=["feedback"]
)


negative_email_prompt = PromptTemplate(
    template="""
    Write an apology email to the customer for giving a negative feedback about his recent purchase of IPhone 16.
    \n {feedback}
    """,
    input_variables=["feedback"]
)

# Writing the conditional chain
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_email_prompt | model | StrOutputParser()),
    (lambda x:x.sentiment == 'negative', negative_email_prompt | model | StrOutputParser()),
    (lambda x: "Not able to analyze the feedback")
)

chain = chain1 | branch_chain

# print(chain.get_graph().draw_ascii())

print(chain.invoke({'feedback': 'The phone is really good and it is meeting my expectations. I am really happy. Name - Dhiraj'}))
