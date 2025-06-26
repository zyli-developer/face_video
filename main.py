from camera.detector import EmotionDetector
from emotion.classifier import EmotionClassifier
from llm.generator import TextGenerator
from tts.tts_engine import TTSEngine
from video.composer import VideoComposer
import time


def main():
    detector = EmotionDetector()
    classifier = EmotionClassifier()
    generator = TextGenerator()
    tts_engine = TTSEngine()
    composer = VideoComposer()

    print("打开摄像头...")
    if not detector.open_camera():
        print("摄像头打开失败！")
        return

    print("开始采集表情...")
    # 这里只采集一帧做演示，后续可扩展为循环实时采集
    frame, emotions = detector.process_frame()
    if not emotions:
        print("未检测到人脸或表情！")
        return
    print(f"检测到表情: {emotions}")

    sentiment = classifier.map_emotion_to_sentiment(emotions[0])
    print(f"情感分类: {sentiment}")

    text = generator.generate_text(sentiment)
    print(f"生成文本: {text}")

    tts_engine.text_to_speech(text, "output.wav")
    print("已生成语音文件 output.wav")

    composer.compose_video("output.wav", text, "final_video.mp4")
    print("已合成视频 final_video.mp4")

    print("流程结束。")

if __name__ == "__main__":
    main() 