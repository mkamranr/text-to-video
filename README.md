# 🧠 Text-to-Video Generator (Open Source)

This tool generates short videos from plain text prompts using the open-source model [`damo/text-to-video-synthesis`](https://www.modelscope.cn/models/damo/text-to-video-synthesis/summary) from ModelScope.

---

## 🚀 Features

- 🎥 Generate video clips from natural language prompts
- 💻 Simple web-based interface using Gradio
- 📦 Based on the `modelscope` framework
- 🪄 Automatically downloads model on first use

---

## 📥 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-to-video-generator.git
cd text-to-video-generator
```

### 2. Create a Virtual Environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Model (Auto or Manual)

The model `damo/text-to-video-synthesis` is downloaded automatically the first time you run the app.

To download it manually:

```python
from modelscope.pipelines import pipeline
pipeline(task='text-to-video-synthesis', model='damo/text-to-video-synthesis', model_revision='v1.1')
```

---

## 🔍 Model Details

- **Model Name**: `damo/text-to-video-synthesis`
- **Provider**: Alibaba DAMO
- **Platform**: [ModelScope](https://www.modelscope.cn)
- **Task**: Text-to-Video Generation
- **Video Resolution**: 576x320
- **Length**: 16 frames (~2 seconds)

> Note: This model generates short videos for research/demo purposes.

---

## 🛠️ System Requirements

- Python 3.8+
- 8GB RAM minimum (16GB+ recommended)
- GPU recommended (CPU works but is slower)
- pip ≥ 20.0

Tested on:
- Ubuntu 22.04 / Windows 10
- Python 3.10
- NVIDIA GPU with CUDA (optional)

---

## ▶️ Run the App

```bash
python app.py
```

Gradio will launch at:

```
http://localhost:7860
```

Enter your text prompt and watch the video generate!

---

## 📂 Output Location

The video file is stored temporarily in the ModelScope cache:

- **Linux/Mac**: `~/.cache/modelscope`
- **Windows**: `%USERPROFILE%\.cache\modelscope`

---

## 🧪 Examples

Try prompts like:

- `A robot dancing in Times Square`
- `A cat floating in space`
- `A waterfall flowing through neon rocks`

---

## 🛠️ Troubleshooting

- **App crashes or hangs?**
  - Ensure you are using Python 3.8 or newer.
  - Try running on a system with a GPU.
  - Make sure you're connected to the internet (for model download).

- **Video doesn't display?**
  - Check console logs for file path or format issues.
  - Try running with a different prompt.

---

## 📜 License

This project is powered by open-source software under the Apache 2.0 License. The underlying model license is owned by ModelScope and Alibaba DAMO Academy. Review their terms here:  
🔗 https://www.modelscope.cn/models/damo/text-to-video-synthesis/summary

---

## 🤝 Contributing

Pull requests, feedback, and issues are welcome! Feel free to fork the repo and submit changes or ideas.

---

## 👨‍💻 Author

Built by Muhammad Kamran Rafi
