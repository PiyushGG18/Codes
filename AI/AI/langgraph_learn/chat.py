from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gemini-3.1-flash-lite-preview",
    model_provider="google_genai",
)

class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

def samplenode(state: State):
    print("\n\nInside samplenode node ", state)
    return {"messages": ["Sample message appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, My name is Piyush"]}))
print("\n\nUpdated state ", updated_state)