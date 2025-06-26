# 项目简介

本项目实现了基于摄像头的人脸表情识别、情感分类、调用大语言模型生成文字，并将生成的文字内容自动合成为视频。适用于儿童互动、情感陪伴等场景。

---

# 功能说明

1. **摄像头实时表情识别**：自动检测人脸并识别表情（如开心、难过等）。
2. **情感分类**：将表情结果归类为情感标签。
3. **大语言模型生成文字**：根据情感标签，调用大语言模型（如GPT/LLaMA）生成对应风格的故事或安慰性文字。
4. **文字转视频**：将生成的文字内容通过TTS（文字转语音）和视频合成工具，自动生成带配音和字幕的视频。

---

# 核心技术方案

- **表情识别**：基于OpenCV和深度学习模型（如FER2013、CNN等）实现摄像头实时表情识别。
- **情感分类**：将表情识别结果映射为情感标签。
- **大语言模型**：集成OpenAI GPT、LLaMA等大语言模型API，根据情感生成定制化文本。
- **文字转视频**：使用TTS（如Coqui TTS）将文字转为语音，moviepy/ffmpeg合成视频。

---

# 参考开源项目

- [Emotion-LLaMA](https://github.com/ZebangCheng/Emotion-LLaMA)
- [GPT-FACIAL-EMOTION-RECOGNITION](https://github.com/DaltonPayne/GPT-FACIAL-EMOTION-RECOGNITION)
- [EmoDetect](https://github.com/ch1y1z1/EmoDetect)
- [moviepy](https://github.com/Zulko/moviepy)
- [TTS](https://github.com/coqui-ai/TTS)

---

# 免费开源大模型与工具推荐

## 1. TTS（文字转语音）
- **Coqui TTS**：[GitHub链接](https://github.com/coqui-ai/TTS)
  - 特点：多语言、模型丰富、推理快、完全免费。
  - 示例：
    ```python
    from TTS.api import TTS
    tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False)
    tts.tts_to_file(text="你好，小朋友，今天要开心哦！", file_path="output.wav")
    ```
- **ESPnet-TTS**：[GitHub链接](https://github.com/espnet/espnet)
  - 学术主流，支持多种TTS模型，适合有深度学习基础者。

## 2. ASR（语音转文字）
- **Whisper (OpenAI)**：[GitHub链接](https://github.com/openai/whisper)
  - 多语言，效果优秀，完全免费。
  - 示例：
    ```python
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe("output.wav")
    print(result["text"])
    ```
- **Vosk**：[GitHub链接](https://github.com/alphacep/vosk-api)
  - 轻量级，支持多平台和多语言。

## 3. 视频合成
- **moviepy**：[GitHub链接](https://github.com/Zulko/moviepy)
  - Python库，支持音频、图片、字幕合成视频。
  - 示例：
    ```python
    from moviepy.editor import *
    audioclip = AudioFileClip("output.wav")
    txt_clip = TextClip("你好，小朋友，今天要开心哦！", fontsize=70, color='white', size=(1280, 720)).set_duration(audioclip.duration)
    videoclip = CompositeVideoClip([txt_clip])
    videoclip = videoclip.set_audio(audioclip)
    videoclip.write_videofile("final_video.mp4", fps=24)
    ```
- **ffmpeg**：[官网](https://ffmpeg.org/)
  - 命令行工具，功能强大，完全免费。

## 4. 免费大语言模型（文本生成）
- **ChatGLM**：[GitHub链接](https://github.com/THUDM/ChatGLM2-6B)
  - 免费、开源、支持本地部署，适合中文。
- **LLaMA2/3**：[GitHub链接](https://github.com/facebookresearch/llama)
  - 需申请权重，社区有多种推理框架。
- **Qwen**：[GitHub链接](https://github.com/QwenLM/Qwen-7B)
  - 阿里开源，支持中文。

---

# 推荐组合与集成流程

- TTS：Coqui TTS
- ASR：Whisper
- 视频合成：moviepy
- 大语言模型：ChatGLM、Qwen、LLaMA2/3（本地推理）

## 典型流程与细节说明

### 1. 文字生成（本地大模型生成文本）
- **输入**：情感标签（如"开心"、"难过"）
- **处理**：根据情感标签，设计Prompt，调用本地大语言模型生成故事或安慰性文字。
- **输出**：生成的文本内容
- **示例代码**（以ChatGLM为例，伪代码）：
  ```python
  prompt = f"请为{emotion}的小朋友生成一段故事或安慰的话。"
  response = glm_model.chat(prompt)
  print(response)
  ```
- **注意事项**：
  - 本地大模型需提前下载权重并配置好推理环境。
  - 可根据不同情感设计不同的Prompt模板。

### 2. TTS（文字转语音）
- **输入**：上一步生成的文本内容
- **处理**：调用Coqui TTS，将文本转为语音文件（如output.wav）
- **输出**：语音音频文件（wav/mp3等）
- **示例代码**：
  ```python
  from TTS.api import TTS
  tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False)
  tts.tts_to_file(text=response, file_path="output.wav")
  ```
- **注意事项**：
  - 选择合适的中文TTS模型。
  - 可根据需求选择不同的发音人或风格。

### 3. ASR（如需，语音转文字）
- **输入**：语音音频文件
- **处理**：调用Whisper等ASR模型，将语音转为文字
- **输出**：识别出的文本内容
- **示例代码**：
  ```python
  import whisper
  model = whisper.load_model("base")
  result = model.transcribe("output.wav")
  print(result["text"])
  ```
- **注意事项**：
  - 若仅需TTS和视频合成，可跳过此步。
  - Whisper支持多种模型大小，权衡速度与精度。

### 4. 视频合成（moviepy）
- **输入**：语音音频文件、文本内容（用于字幕）、可选的背景图片/视频
- **处理**：用moviepy将音频、字幕、背景合成为视频
- **输出**：最终视频文件（如final_video.mp4）
- **示例代码**：
  ```python
  from moviepy.editor import *
  audioclip = AudioFileClip("output.wav")
  txt_clip = TextClip(response, fontsize=70, color='white', size=(1280, 720)).set_duration(audioclip.duration)
  videoclip = CompositeVideoClip([txt_clip])
  videoclip = videoclip.set_audio(audioclip)
  videoclip.write_videofile("final_video.mp4", fps=24)
  ```
- **注意事项**：
  - 可自定义背景图片、字体、字幕样式等。
  - 视频分辨率、帧率可根据需求调整。
  - 如需更丰富的画面，可叠加动画、图片等元素。

---

如需进一步细化某一环节的实现或遇到具体技术问题，欢迎随时咨询！

---

# 快速开始

## 1. 环境准备

- Python 3.7+
- 建议使用虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Windows下为 venv\Scripts\activate
```

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

## 3. 运行项目

```bash
python main.py
```

## 4. 配置大语言模型API

- 需在环境变量中设置API Key（如OpenAI GPT等）。

## 5. 体验流程

- 启动后，摄像头自动检测人脸表情。
- 根据表情分类，自动生成故事或安慰性文字。
- 自动合成视频并保存/展示。

---

# 备注

如需自定义模型或功能，可参考上述开源项目进行二次开发。

---

# 大语言模型下载与集成说明

## 推荐模型
- **ChatGLM2-6B**（推荐，支持中文，开源免费）

## 下载方式

### 方式一：自动下载
- 只需在 `llm/generator.py` 中指定模型名（如 "THUDM/chatglm2-6b"），首次运行会自动下载到 `~/.cache/huggingface/hub` 目录。

### 方式二：手动下载
1. 访问 [ChatGLM2-6B HuggingFace页面](https://huggingface.co/THUDM/chatglm2-6b)
2. 登录后点击"Download"下载全部模型文件
3. 将下载的文件夹（如 `chatglm2-6b`）放到本地项目的 `models/` 目录下

## 配置与集成
- 在 `config.yaml` 或 `.env` 文件中增加模型路径配置：
  ```yaml
  llm_model: "models/chatglm2-6b"  # 或 "THUDM/chatglm2-6b"
  ```
- 主流程初始化时读取配置：
  ```python
  import yaml
  with open("config.yaml", "r", encoding="utf-8") as f:
      config = yaml.safe_load(f)
  generator = TextGenerator(model_path_or_name=config["llm_model"])
  ```
- 代码已支持本地路径和 HuggingFace Hub 名称两种加载方式。

## 依赖安装
- 请确保已安装 `transformers`、`torch` 等依赖。
- 推荐使用 GPU 环境，内存建议 16GB 以上。

## 常见问题
- 首次加载慢，需耐心等待。
- 无外网时请提前手动下载模型。
- 加载失败时会有友好提示。 