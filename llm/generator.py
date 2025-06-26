from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

class TextGenerator:
    def __init__(self, model_path_or_name="THUDM/chatglm2-6b"):
        self.model_path_or_name = model_path_or_name
        self.model = None
        self.tokenizer = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self._load_model()

    def _load_model(self):
        try:
            print(f"正在加载大语言模型: {self.model_path_or_name} ...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path_or_name, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_path_or_name, trust_remote_code=True).to(self.device)
            self.model.eval()
            print("大语言模型加载完成！")
        except Exception as e:
            print(f"大语言模型加载失败: {e}")
            print("请确保已下载模型权重，或网络可用。可将模型文件夹放在 models/ 目录下，并在配置中指定本地路径。")
            self.model = None
            self.tokenizer = None

    def generate_text(self, sentiment, prompt_template=None):
        if self.model is None or self.tokenizer is None:
            return f"[大语言模型未加载] 这是为{sentiment}情感生成的占位文本。"
        prompt = prompt_template or f"请为{sentiment}的小朋友生成一段故事或安慰的话。"
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        with torch.no_grad():
            output = self.model.generate(input_ids, max_length=128, do_sample=True, top_p=0.95, temperature=0.8)
        return self.tokenizer.decode(output[0], skip_special_tokens=True) 