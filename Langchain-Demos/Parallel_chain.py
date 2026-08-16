from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template="""
    Write a beginner friendly article on {topic}
    """,
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="""
    Generate a professional Linkedin post with a strong hook on below mentioned topic: \n topic: {topic}
    """,
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="""
    Merge the provided article and LinkedIn post into a single document \n {article} and LinkedIn post {post}
    """,
    input_variables=["article", "post"]
)

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

parellel_chain = RunnableParallel(
    {
        'article': prompt1 | model | StrOutputParser(),
        'post': prompt2 | model | StrOutputParser()
    }
)

document_chain = prompt3 | model | StrOutputParser()

chain = parellel_chain | document_chain

print(chain.invoke({'topic': 'AI disruption in IT'}))