from langchain.memory import ConversationBufferWindowMemory
from drive_thru_bot.agent.llm import MistralAgent
from langchain.agents.agent import AgentExecutor
import chainlit as cl

MODEL_PATH = "./models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"

mistral_agent = MistralAgent(
    model_path=MODEL_PATH,
    temperature=0.1,
    n_ctx=1024,
    n_threads=5,
)


@cl.on_chat_start
async def on_chat_start():
    memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        input_key="input",
        output_key="output",
        return_messages=True,
        k=5,
    )
    cl.user_session.set("memory", memory)
    cl.user_session.set("order", [])

    agent = mistral_agent.load_agent(memory)
    cl.user_session.set("agent", agent)
    await cl.Message("Hi! Welcome to KFC, how can I help you today?").send()


@cl.on_message
async def main(message: cl.Message):
    agent: AgentExecutor = cl.user_session.get("agent")

    answer = await agent.ainvoke({"input": message.content})
    await cl.Message(answer["output"]).send()
