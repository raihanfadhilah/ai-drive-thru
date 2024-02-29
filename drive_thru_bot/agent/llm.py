from langchain.agents.agent import AgentExecutor
from langchain.agents.initialize import initialize_agent
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models.ollama import ChatOllama
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.llms import LlamaCpp
from drive_thru_bot.agent.prompts import SYS_MSG, HUMAN_MSG   # type: ignore
from drive_thru_bot.agent.tools import take_order, confirm_order # type: ignore

class MistralAgent:
    """
    Represents a Mistral Agent that interacts with the ChatOllama model.

    Args:
        model_path (str): The path to the ChatOllama model.
        temperature (float): The temperature parameter for generating responses.
        n_ctx (int): The number of context tokens.
        n_threads (int): The number of threads to use.

    Attributes:
        model_path (str): The path to the ChatOllama model.
        temperature (float): The temperature parameter for generating responses.
        n_ctx (int): The number of context tokens.
        n_threads (int): The number of threads to use.
        model (ChatOllama): The ChatOllama model instance.
        agent (AgentExecutor): The Mistral Agent executor.

    Methods:
        load_agent: Loads the Mistral Agent with the specified memory.

    """

    def __init__(self, model_path: str, temperature: float, n_ctx: int, n_threads: int):
        self.model_path = model_path
        self.temperature = temperature
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        self.model = ChatOllama(
            model="openhermes:7b-mistral-v2.5-q4_K_M",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            temperature=self.temperature,
            num_ctx=self.n_ctx,
            num_thread=self.n_threads,
        )

    def load_agent(
        self, memory: ConversationBufferWindowMemory, **kwargs
    ) -> AgentExecutor:
        """
        Loads the Mistral Agent with the specified memory.

        Args:
            memory (ConversationBufferWindowMemory): The memory for the agent.
            **kwargs: Additional keyword arguments.

        Returns:
            AgentExecutor: The loaded Mistral Agent executor.

        """
        self.agent = initialize_agent(
            llm=self.model,
            tools=[take_order, confirm_order],
            memory=memory,
            agent="chat-conversational-react-description",
            verbose=True,
            # handle_parsing_errors=True,
            # return_intermediate_steps=True,
            **kwargs
        )

        ## Set the system and human messages
        self.agent.agent.llm_chain.prompt.messages[0].prompt.template = SYS_MSG
        self.agent.agent.llm_chain.prompt.messages[2].prompt.template = HUMAN_MSG

        return self.agent
