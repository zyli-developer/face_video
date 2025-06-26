class EmotionClassifier:
    def __init__(self):
        self.emotion_mapping = {
            'happy': 'positive',
            'sad': 'negative',
            'angry': 'negative',
            'surprise': 'neutral',
            'fear': 'negative',
            'disgust': 'negative',
            'neutral': 'neutral'
        }

    def map_emotion_to_sentiment(self, emotion_label):
        return self.emotion_mapping.get(emotion_label, 'neutral')

    def customize_mapping(self, mapping_dict):
        self.emotion_mapping.update(mapping_dict) 