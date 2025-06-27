from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

# Load the pipeline globally (once)
pipe = pipeline(task='text-to-video-synthesis', model='damo/text-to-video-synthesis', model_revision='v1.1')

def generate_video(prompt: str) -> str:
    result = pipe({'text': prompt})
    return result[OutputKeys.OUTPUT_VIDEO]
