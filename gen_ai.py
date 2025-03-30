# -*- coding: utf-8 -*-
"""Gen AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EjUsoCCvs5RuhWul1oX9ulkUYJPHzzsz
"""

!pip install transformers torch diffusers accelerate openai-whisper
!pip install accelerate
!pip install gradio

!pip install TTS

from huggingface_hub import notebook_login

notebook_login()

from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from diffusers import AutoPipelineForText2Image, StableVideoDiffusionPipeline, StableDiffusionPipeline, AnimateDiffPipeline
import torch

llm_model_name = "mistralai/Mistral-7B-v0.1"
llm_model = AutoModelForCausalLM.from_pretrained(llm_model_name, torch_dtype=torch.float16, device_map="auto")
llm_tokenizer = AutoTokenizer.from_pretrained(llm_model_name)

def generate_text(prompt):
    inputs = llm_tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    streamer = TextStreamer(llm_tokenizer)
    outputs = llm_model.generate(**inputs, streamer=streamer, max_length=100)
    return llm_tokenizer.decode(outputs[0], skip_special_tokens=True)

img_model_id = "runwayml/stable-diffusion-v1-5"
pipe_img = StableDiffusionPipeline.from_pretrained(img_model_id, torch_dtype=torch.float16)

def generate_image(prompt):
    return pipe_img(prompt, width=384, height=384).images[0]

import torch
from TTS.api import TTS
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
def generate_audio(text):
    tts.tts_to_file(text=text, file_path="generated_audio.wav")

def generate_all(prompt):
    text = generate_text(prompt)
    image = generate_image(prompt)
    generate_audio(text)
    return text, image, "generated_audio.wav"

import gradio as gr
def generate_all(prompt):
    text = generate_text(prompt)
    image = generate_image(prompt)
    generate_audio(text)
    return text, image, "generated_audio.wav"

gr.Interface(
    fn=generate_all,
    inputs="text",
    outputs=["text", "image", "file"],
    title="Multi-Modal AI Generator",
    description="Enter a prompt to generate text, images, and audio."
).launch()

