from TTS.api import TTS

class TTSEngine:
    def __init__(self, model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST"):
        self.model_name = model_name
        self.tts = TTS(model_name=model_name, progress_bar=False)

    def text_to_speech(self, text, output_path):
        self.tts.tts_to_file(text=text, file_path=output_path)

    def set_tts_model(self, model_name):
        self.model_name = model_name
        self.tts = TTS(model_name=model_name, progress_bar=False)

    def adjust_speech_rate(self, rate):
        # Coqui TTS暂不直接支持，需自定义实现
        pass

    def adjust_pitch(self, pitch):
        # Coqui TTS暂不直接支持，需自定义实现
        pass 