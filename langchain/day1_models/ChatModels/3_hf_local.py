from transformers import AutoModelForCausalLM
from langchain_huggingface import (
    HuggingFacePipeline,
    ChatHuggingFace
)

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={
        "device_map": "auto"
    },
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.5
    }
)

response = llm.invoke("what're you upto")
print(response)