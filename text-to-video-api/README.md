# 📽️ Text-to-Video Generation API (FastAPI)

Generate short videos using text prompts with Alibaba's open-source `damo/text-to-video-synthesis` model on [ModelScope](https://www.modelscope.cn).

---

## 🚀 Features

- REST API powered by FastAPI
- Accepts text prompts and returns path to generated video
- Automatically downloads model on first run

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-to-video-api.git
cd text-to-video-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

```
http://localhost:8000
```

---

## 📡 API Usage

### `POST /generate`

**Request Body**:
```json
{
  "prompt": "A panda riding a bicycle"
}
```

**Response**:
```json
{
  "video_path": "/root/.cache/modelscope/.../output.mp4"
}
```

---

## 🧪 Example (Python Client)

```python
import requests

resp = requests.post("http://localhost:8000/generate", json={"prompt": "A cat flying through clouds"})
print(resp.json())
```

---

## 📂 Output Files

Videos are cached under:
- Linux/macOS: `~/.cache/modelscope`
- Windows: `%USERPROFILE%\.cache\modelscope`

---

## ⚠️ Notes

- Requires internet on first run (to download the model)
- GPU recommended, CPU fallback available

---

## 🧑‍💻 Author

Created by Muhammad Kamran Rafi