# Mini-Clinical-AI-Assistant
This repository contains the source code for a mini clinical AI assistant that transcribes clinical audio and performs various information extraction on it. 

### Features

1. Audio Transcription using OpenAI Whisper
2. Clinical Information Extraction (age, sex, complaint, diagnosis, plan)
3. SOAP Note Generation
4. Powered by GPT-4o


### Project Structure 

```
clinical_ai_assistant/
│
├── audio/                            # Input - Sample audio file
│   └── sample_audio.wav
│
├── models/                           # Model-related classes and credentials
│   ├── credentials/
│   │   └── gpt4o.yaml                # YAML file with GPT-4o credentials
│   ├── data_classes.py              # Pydantic dataclasses for LLMs
│   ├── model_classes.py             # GPT4O model wrapper
│   └── llm_json_generators.py       # Structured LLM prompt-based extractors
│
├── outputs/                          # Generated outputs
│   ├── clinical_extraction_structured_json.json
│   ├── soap_note_text.txt
│   └── soap_note_json.json
│
├── prompts/                          # Prompt templates for LLM
│   ├── clinical_extraction.json
│   ├── soap_note_generation.json
│   └── soap_note_generation_text.json
│
├── src/                              # Source scripts
│   ├── main.py                       # Main pipeline to run everything
│   ├── test.ipynb                    # Jupyter notebook for experimentation
│   ├── generate_sample_audio.py     # Script to generate a sample audio from text using gTTS (Not a module)
│   └── transcriber.py               # Whisper transcription wrapper
│
├── transcripts/                      # Generated text transcripts
│   ├── sample_transcript.txt
│   └── sample_transcript_2.txt
│
├── utilities/                        # Utility functions
│   └── functions.py
│   
├── clinical_ai_assistant_documentation.pdf        # Documentation of the approach

```

### Outputs

1. ```outputs/clinical_extraction_structured_json.json```: Structured clinical fields like Age, sex, diagnosis, etc
2. ```outputs/soap_note_text.txt``` : AI generated SOAP note in plain text
3. ```outputs/soap_note_json.json``` : AI generated SOAP note in JSON format
