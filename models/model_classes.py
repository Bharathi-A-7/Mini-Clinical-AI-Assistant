import time
from abc import ABC
import requests
from pydantic import BaseModel
from models.data_classes import Payload, GPT4oCreds

class GenerativeModel(ABC):
    """
    Abstract base class for Generative Models.
    Attributes:
       credentials (BaseModel): The credentials required to authenticate
       with the model.
   """
    def __init__(self, credentials: BaseModel):
        """
        Initializes the generative model with the given credentials.
        Arguments:
            credentials (BaseModel): The credentials required to authenticate
            with the model.
        """
        self.credentials = credentials

    def query(self, payload: Payload):
        """
        Abstract method to query the model and get response.
        """

class GPT4O(GenerativeModel):
    """
    Class for interacting with the GPT4O model.
    Attributes:
        credentials (GPT4oCreds): The credentials required to
        authenticate with the GPT4O model.
    """
    def __init__(self, credentials: GPT4oCreds):
        """
        Initializes the GPT4O model with the given credentials.
        Arguments:
            credentials (GPT4oCreds): The credentials required to
            authenticate with the GPT4O model.
        """
        super().__init__(credentials)

    def query(self, payload: Payload):
        """
        Sends a query to the GPT4O model.
        Arguments:
            payload (Payload): The payload to be sent to the model.
        Returns:
            dict: The response from the model.
        """
        headers = {
            "Content-Type": "application/json",
            "api-key": self.credentials.key
        }
        payload_json = payload.dict()
        max_retries = 10
        delay = 5  # Delay in seconds between retries
        retries = 0
        while retries < max_retries:
            try:
                response = requests.post(
                    self.credentials.endpoint,
                    headers=headers,
                    json=payload_json)
                # Will raise an HTTPError if the HTTP request
                # returned an unsuccessful status code
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as exception_message:
                if response.status_code == 429:  # 429 Too Many Requests
                    print(f"Too many requests. Waiting for {delay} \
                          seconds before retrying... \
                          (Retry {retries + 1}/{max_retries})")
                    time.sleep(delay)
                    retries += 1
                else:
                    # Handle other HTTP errors here
                    print(f"HTTP error occurred: {exception_message}")
                    break
            except requests.RequestException as exception_message:
                # Handle non-HTTP errors here
                print(f"Failed to make the request. \
                      Error: {exception_message}")
                break

        print("Maximum retries reached. Could not complete the request.")
        return None
