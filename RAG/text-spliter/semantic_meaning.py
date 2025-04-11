from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

text_splitter = SemanticChunker(
    embeddings,
   breakpoint_threshold_type = "standard_deviation",#used to determine the threshold for splitting. various options include "standard_deviation", "mean", "median", and "max". The default is "standard_deviation".
   breakpoint_threshold_amount=1 #used to determine the threshold for splitting. The default is 1.
)

sample_text ="""
Farmers form the backbone of any nation's economy, especially in agrarian societies like India. Despite their critical role in feeding the population and supporting rural economies, many farmers continue to struggle with issues like unpredictable weather, rising debts, and lack of government support. Their hard work and resilience often go unnoticed amidst the fast-paced modern world. Interestingly, while farmers toil under the sun in the fields, another group of individuals cricketers in the IPL perform under the floodlights, captivating millions across the globe. The Indian Premier League (IPL) is more than just a cricket tournament; it's a cultural phenomenon that unites people across states and languages. It brings glamour, entertainment, and significant economic opportunities, but it also raises questions about priorities when enormous sums are spent on sport while essential sectors like agriculture remain underfunded.

On a more serious note, terrorism continues to be one of the gravest threats to global peace and security. It not only causes tragic loss of life but also creates fear, instability, and long-lasting divisions within societies. The motivations behind terrorism are complex—ranging from ideological extremism to political grievances—and combating it requires international cooperation, intelligence sharing, and addressing the root causes like poverty and radicalization. While the world rallies behind sports and celebrates the common farmer during crises, it must also remain vigilant and united against forces that seek to divide and destroy.
"""

docs = text_splitter.create_documents([sample_text])
print(len(docs))
print(docs[0])
print("******************** ****************")
print(docs[1])
print("******************** ****************")
print(docs[2])

""" 
In the above code, we utilized Google's embedding model in combination with the SemanticChunker class from LangChain's experimental module. Our goal was to split a given block of text based on its semantic meaning, rather than just length or structure.

We provided a sample paragraph and expected it to be broken down into semantically meaningful chunks. However, the output did not meet expectations—it produced three paragraphs, but some parts of the content were merged incorrectly, leading to mismatched meanings. This indicates that the splitting did not fully preserve the intended context of the original text.

It's important to note that the SemanticChunker class is still in the experimental phase and not yet production-ready. As such, occasional inconsistencies in behavior or performance can be expected while using it.
"""