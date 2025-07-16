from typing import List
from pydantic import BaseModel, Field

class Message(BaseModel):
    """
    Represents a message with a role and content for an LLM.
    Attributes:
        role (str): The role of the message sender (e.g., 'system', 'user').
        content (List[dict]): The content of the message as a list
        of dictionaries.
    """
    role: str
    content: List[dict]

class Payload(BaseModel):
    """
    Represents the payload for a request.
    Attributes:
        messages (List[Message]): A list of Message objects.
        temperature (float): The temperature setting for the model.
        top_p (float): The top_p setting for the model.
        max_tokens (int): The maximum number of tokens to generate.
    """
    messages: List[Message]
    temperature: float
    top_p: float
    max_tokens: int

class GPT4oCreds(BaseModel):
    """
    Represents the credentials for GPT-4o.
    Attributes:
        endpoint (str): The endpoint URL.
        key (str): The API key.
    """
    endpoint: str
    key: str

class Parameter(BaseModel):
    """
    Represents the parameters for a request.
    Attributes:
        temperature (float): The temperature setting for the model.
        top_p (float): The top_p setting for the model.
        max_tokens (int): The maximum number of tokens to generate.
    """
    temperature: float = Field(default=0.5)
    top_p: float = Field(default=0.95)
    max_tokens: int = Field(default=8000)


class GenPromptConfig(BaseModel):
    """
    Represents the configuration for a generation prompt.
    Attributes:
        generation_prompt (str): The generation prompt text.
        parameters (Paramter): The parameters for the generation.
    """
    generation_prompt: str = ''
    parameters: Parameter