from langchain.text_splitter import CharacterTextSplitter

text ="""
**Generative AI (GenAI): A Transformative Force in Technology**

Generative AI (GenAI) refers to a class of artificial intelligence models that can create new content, such as text, images, music, code, and more, based on the data they've been trained on. These models, especially large-scale neural networks like transformers, have evolved rapidly in recent years and are redefining the boundaries of creativity, productivity, and problem-solving across industries.

At the heart of GenAI are deep learning models, particularly large language models (LLMs) like OpenAI's GPT (Generative Pre-trained Transformer), Google's Gemini, and Meta's LLaMA. These models are trained on massive datasets and learn to generate human-like text, carry on conversations, write essays, generate code, and even solve complex analytical tasks. In the visual domain, models such as DALL·E, Midjourney, and Stable Diffusion can generate detailed images from simple text prompts, blending artistic style and imagination.

One of the most compelling aspects of GenAI is its ability to augment human creativity and productivity. In content creation, writers use GenAI for drafting articles, brainstorming ideas, or overcoming writer's block. Designers employ image generation tools to explore visual concepts rapidly. In software development, tools like GitHub Copilot assist programmers by suggesting code snippets and automating routine coding tasks. GenAI also powers personalized education, simulating tutors that adapt to student needs, and enhances customer service through intelligent, conversational AI agents.

"""

spliter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0,separator="")

res = spliter.split_text(text)

print(res)