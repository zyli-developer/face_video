from moviepy.editor import *

class VideoComposer:
    def compose_video(self, audio_path, subtitle, output_path, background_path=None, style_dict=None):
        audioclip = AudioFileClip(audio_path)
        if background_path:
            bg_clip = VideoFileClip(background_path).subclip(0, audioclip.duration)
            txt_clip = TextClip(subtitle, fontsize=style_dict.get('fontsize', 70) if style_dict else 70,
                                color=style_dict.get('color', 'white') if style_dict else 'white',
                                size=bg_clip.size).set_duration(audioclip.duration)
            videoclip = CompositeVideoClip([bg_clip, txt_clip])
        else:
            txt_clip = TextClip(subtitle, fontsize=style_dict.get('fontsize', 70) if style_dict else 70,
                                color=style_dict.get('color', 'white') if style_dict else 'white',
                                size=style_dict.get('size', (1280, 720)) if style_dict else (1280, 720)).set_duration(audioclip.duration)
            videoclip = CompositeVideoClip([txt_clip])
        videoclip = videoclip.set_audio(audioclip)
        videoclip.write_videofile(output_path, fps=24)

    def add_subtitle_to_video(self, video_path, subtitle, style_dict=None):
        video = VideoFileClip(video_path)
        txt_clip = TextClip(subtitle, fontsize=style_dict.get('fontsize', 70) if style_dict else 70,
                            color=style_dict.get('color', 'white') if style_dict else 'white',
                            size=video.size).set_duration(video.duration)
        result = CompositeVideoClip([video, txt_clip])
        output_path = video_path.replace('.mp4', '_subtitled.mp4')
        result.write_videofile(output_path, fps=24)
        return output_path

    def set_video_style(self, style_dict):
        # 可扩展：自定义视频样式参数
        self.style_dict = style_dict

    def create_background(self, size, color="black"):
        # 创建纯色背景clip
        from moviepy.video.VideoClip import ColorClip
        return ColorClip(size, color=color) 