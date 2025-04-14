import boto3
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import BedrockChat
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever

# Amazon Bedrock - settings

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

model_id = "deepseek.r1-v1:0"

model_kwargs =  { 
    "max_tokens": 2048,
    "temperature": 0.0,
    "top_k": 250,
    "top_p": 1,
    "stop_sequences": ["\n\nHuman"],
}


template = '''Answer the question based only on the following context:
{context}

Question: {question}'''

prompt = ChatPromptTemplate.from_template(template)

# Amazon Bedrock - KnowledgeBase Retriever 
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="DC4KARLFDD",
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
)

model = BedrockChat(
    client=bedrock_runtime,
    model_id=model_id,
    model_kwargs=model_kwargs,
)

chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    .assign(response = prompt | model | StrOutputParser())
    .pick(["response", "context"])
)