from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
os.environ["HF_HOME"] = "d:/huggingface_model"
llm = HuggingFacePipeline.from_model_id(
   model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.9,
        max_length=100,
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)
