import os
import sys
import yaml
from models.data_classes import GPT4oCreds, GenPromptConfig
from models.model_classes import GPT4O
from models.llm_json_generators import GPT4oJSONGenerator
from utilities.functions import *
from src.transcriber import WhisperAudioTranscriber


# You can skip the below two lines by directly reading transcription from the text file since running the transcription takes a few minutes

transcriber = WhisperAudioTranscriber()
transcript = transcriber.transcribe("audio/sample_audio.wav", "transcripts/sample_transcript.txt")
# transcript = read_text_file("transcripts/sample_transcript.txt")

# Read GPT4o model credentials
credentials = load_yaml_file("models/credentials/gpt4o.yaml")

# Load GPT4o model and the prompts
gpt4o = GPT4O(GPT4oCreds(**credentials))
prompts = load_prompts_from_dir("prompts/")

# Read task specific prompts from the prompts dictionary
clinical_extraction_prompt = GenPromptConfig(**prompts['clinical_extraction'])
# Added two seperate prompts for SOAP note generation. One generates a JSON output and the other generates a .txt output
soap_note_prompt_text = GenPromptConfig(**prompts['soap_note_generation_text'])
soap_note_prompt_json = GenPromptConfig(**prompts["soap_note_generation"])

# Run clinical and SOAP note extractions
clinical_extraction = GPT4oJSONGenerator(gpt4o, clinical_extraction_prompt, transcript).generate()[0]
soap_note_text = GPT4oJSONGenerator(gpt4o, soap_note_prompt_text, transcript).generate()[1]
soap_note_json = GPT4oJSONGenerator(gpt4o, soap_note_prompt_json, transcript).generate()[0]

# Save clinical extraction to JSON file
write_json_to_file(clinical_extraction, "outputs/clinical_extraction_structured_json.json")

# Write SOAP notes to .txt and JSON files
write_text_to_file(soap_note_text, "outputs/soap_note_text.txt")
write_json_to_file(soap_note_json, "outputs/soap_note_json.json")








