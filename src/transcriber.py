# model = whisper.load_model("turbo")
# result = model.transcribe("audio/sample_audio.wav")

# with open("transcripts/sample_transcript.txt", "w") as file:
#     file.write(result['text'])
import whisper

class WhisperAudioTranscriber:
    def __init__(self, model_name: str = "turbo"):
        """
        Initialize the transcriber with the specified Whisper model.
        """
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str, output_path: str) -> None:
        """
        Transcribe the audio file and save the transcript to a text file.

        Args:
            audio_path (str): Path to the input audio file.
            output_path (str): Path to the output transcript file.
        """
        result = self.model.transcribe(audio_path)
        transcription = result.get('text').strip()
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(transcription)
        return transcription
