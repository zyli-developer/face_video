import cv2
import numpy as np
from tensorflow.keras.models import load_model

class EmotionDetector:
    def __init__(self, model_path: str = "models/emotion_model.h5", cascade_path: str = None):
        """初始化表情识别器"""
        self.face_cascade = cv2.CascadeClassifier(
            cascade_path or cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        # 加载表情识别模型
        try:
            self.model = load_model(model_path)
            print(f"表情识别模型加载成功: {model_path}")
        except Exception as e:
            print(f"表情识别模型加载失败: {e}")
            self.model = None
        self.cap = None
        self.emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

    def open_camera(self, camera_id: int = 0):
        self.cap = cv2.VideoCapture(camera_id)
        return self.cap.isOpened()

    def get_frame(self):
        if self.cap is None:
            return None
        ret, frame = self.cap.read()
        return frame if ret else None

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def predict_emotion(self, face_img):
        if self.model is None:
            return "happy"  # 占位返回
        # 预处理
        face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        face_resized = cv2.resize(face_gray, (48, 48))
        face_input = face_resized[np.newaxis, ..., np.newaxis] / 255.0
        preds = self.model.predict(face_input)
        idx = np.argmax(preds)
        return self.emotion_labels[idx]

    def process_frame(self):
        frame = self.get_frame()
        if frame is None:
            return None, []
        faces = self.detect_faces(frame)
        emotions = []
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            emotion = self.predict_emotion(face_img)
            emotions.append(emotion)
        return frame, emotions 