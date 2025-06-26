from moviepy.editor import *

class VideoComposer:
    def compose_video(self, audio_path, subtitle, output_path, background_path=None):
        audioclip = AudioFileClip(audio_path)
        txt_clip = TextClip(subtitle, fontsize=70, color='white', size=(1280, 720)).set_duration(audioclip.duration)
        videoclip = CompositeVideoClip([txt_clip])
        videoclip = videoclip.set_audio(audioclip)
        videoclip.write_videofile(output_path, fps=24) 