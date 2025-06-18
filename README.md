🎨🗣️ Multi-Modal AI Generator

📌 **Overview**

This project demonstrates a simple **multi-modal AI system** that:
- ✅ Generates text using a Large Language Model (`Mistral-7B`)
- ✅ Generates images using Stable Diffusion
- ✅ Generates audio speech from text using `TTS`
- ✅ Provides a web UI with **Gradio**

Just enter a **single prompt** and get:
- 📜 AI-generated text
- 🖼️ A matching image
- 🔊 Spoken audio of the text

---

⚡ **Tech Stack**

- **Hugging Face Transformers** — for LLM text generation  
- **Diffusers** — for text-to-image generation (Stable Diffusion)  
- **TTS** — for text-to-speech  
- **Gradio** — for an easy-to-use web interface  
- **Torch** — as the backend for all models

---

## 🚀 **Quickstart**

### 1️⃣ **Clone the repo (optional)**

bash
git clone https://github.com/your-username/multimodal-ai-generator.git
cd multimodal-ai-generator

2️⃣ Install dependencies
pip install -r requirements.txt
OR manually:
pip install transformers torch diffusers accelerate openai-whisper TTS gradio

3️⃣ Authenticate with Hugging Face
from huggingface_hub import notebook_login
notebook_login()
You’ll be prompted to paste your Hugging Face token.

4️⃣ Run the app
Create a Python script (app.py) with your code or run the notebook. Then launch:
python app.py
OR if you use a notebook, just run the cells.

⚙️ Usage
Open the Gradio link (localhost or shareable link).
Type your prompt — click Generate — get:

📜 Text

🖼️ Image (384x384)

🔊 Audio file (generated_audio.wav)

🎯 Features
✅ Uses Mistral-7B LLM for rich text generation
✅ Uses Stable Diffusion for detailed images
✅ Uses TTS for natural speech
✅ Runs on GPU if available (torch.float16)
✅ Easy Gradio interface for anyone to try

📝 License
This project is open-source, under the MIT License.

⭐ If you like it:
Please star ⭐ the repo and share your ideas! 🚀

