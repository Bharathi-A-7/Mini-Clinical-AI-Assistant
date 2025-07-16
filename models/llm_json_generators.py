import json
import logging
import re
from abc import ABC, abstractmethod
import traceback
import base64
from typing import Dict, Tuple, Union
from models.data_classes import Payload, GenPromptConfig, Message
from models.model_classes import GPT4O

class LLMJSONGenerator(ABC):
    """
    Abstract base class for LLMs with JSON Output Generators.
    """
    def __init__(self) -> None:
        """
        Initializes the LLMJSONGenerator.
        """

    @abstractmethod
    def generate(self) -> dict:
        """
        Abstract method to generate a response.
        Returns:
            dict: The extracted JSON from the model response.
        """

    @abstractmethod
    def _get_payload(self) -> Payload:
        """
        Abstract method to get the payload for the request.
        Returns:
            Payload: The defined payload for a request with the
            model parameters.
        """

    def _get_json(self, response) -> Union[Tuple[Dict, str], str]:
        """
        Extracts JSON from the response.
        Arguments:
            response (dict): The response from the model.
        Returns:
            dict: Extracted JSON and the text content.
        """
        json_dict = [{}]
        try:
            text = response["choices"][0]["message"]["content"]
        except Exception:
            return traceback.format_exc()

        # Use regular expression to find the text between two strings
        match = re.search(r'```json\n(.*?)```', text, re.DOTALL)
        if match:
            json_str = match.group(0)
            json_str = json_str.replace("```", "")
            json_str = json_str.replace("json\n", "")
            logging.info("JSON found")
        else:
            json_str = "[{}]"
        try:
            json_dict = json.loads(json_str)
        except Exception:
            json_dict = [{}]
        return json_dict, text
    
class GPT4oJSONGenerator(LLMJSONGenerator):
    """
    JSON Generator class for GPT-4o model.
    Attributes:
        model (GPT4O): The GPT-4o model instance.
        prompt_config (PromptConfig): The configuration for the prompt.
        encoded_images (list): List of base64 encoded images.
    """
    def __init__(self, model: GPT4O,
                 prompt_config: GenPromptConfig,
                 text_input) -> None:
        self.model = model
        self.prompt_config = prompt_config
        self.input = text_input

    def _get_payload(self) -> Payload:
        """
        Constructs the payload for the GPT-4o model request.
        Returns:
                Payload: The defined payload for a request with the
                model parameters.
        """

        prompt = self.prompt_config.generation_prompt
        parameters = self.prompt_config.parameters
        payload = Payload(
            messages=[
                Message(
                    role="system",
                    content=[
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                ),
                Message(
                    role="user",
                    content=[
                        {
                            "type": "text",
                            "text": self.input
                        }
                    ]
                )
            ],
            temperature=parameters.temperature,
            top_p=parameters.top_p,
            max_tokens=parameters.max_tokens
        )
        return payload

    def generate(self) -> dict:
        """
        Generates a JSON response from the GPT-4o model.
        Returns:
                dict: The extracted JSON from the model response.
        """
        payload = self._get_payload()
        response = self.model.query(payload)
        return self._get_json(response)

