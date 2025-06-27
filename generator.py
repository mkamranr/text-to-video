from modelscope.pipelines import pipeline
from modelscope.models import Model
from modelscope.outputs import OutputKeys

# Load pipeline once
def load_pipeline():
    pipe = pipeline(task='text-to-video-synthesis', model='damo/text-to-video-synthesis', model_revision='v1.1')
    return pipe

# Generate video
def generate_video(pipe, prompt):
    result = pipe({'text': prompt})
    return result[OutputKeys.OUTPUT_VIDEO]
