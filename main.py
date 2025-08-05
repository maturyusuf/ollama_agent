from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from vector import retriever

# Initialize the Ollama LLM 
llm = OllamaLLM(model="llama3.2", temperature=0.7)

template = """
You are a helpful assistant. Answer the following question based on the context provided.
Here's the context: {context}
Here's the question: {question}
Please provide a concise answer.
"""

prompt = ChatPromptTemplate.from_template(template)

chain: RunnableSequence = prompt | llm

while True:
    # Get user input
    user_input = input("Enter your question (or 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break
    
    # Use the retriever to get context and then invoke the chain with the context and question
    context = retriever.invoke(user_input)
    result = chain.invoke({"context": context, "question": user_input})
    
    # Print the result
    print(result)
    
    

    
    
    
