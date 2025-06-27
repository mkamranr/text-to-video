import gradio as gr
from generator import load_pipeline, generate_video

# Load pipeline once
pipe = load_pipeline()

def run_inference(prompt):
    video_path = generate_video(pipe, prompt)
    return video_path

demo = gr.Interface(
    fn=run_inference,
    inputs=gr.Textbox(label="Enter text prompt"),
    outputs=gr.Video(label="Generated Video"),
    title="Text to Video Generator",
    description="Enter a text prompt to generate a video using open-source AI model."
)

if __name__ == "__main__":
    demo.launch()
