from TTS.api import TTS

class TTSEngine:
    def __init__(self, model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST"):
        self.tts = TTS(model_name=model_name, progress_bar=False)

    def text_to_speech(self, text, output_path):
        self.tts.tts_to_file(text=text, file_path=output_path) 