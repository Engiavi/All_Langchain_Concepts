from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langchain.schema.runnable import RunnableParallel # type: ignore

load_dotenv()
parser = StrOutputParser()
model1  = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template ="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"],
)
prompt2 = PromptTemplate(
    template="Generate 5 multiple choice question from given text \n {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template = "Merge the provided notes and mcqs into a single document \n notes ->{notes} \n mcqs->{mcqs}",
    input_variables=["notes", "mcqs"],
)

# we have to first complete the parallel chain
# Thereafter merge the outputs of both the chains
# at last we get final output

# fist task -> complete the parallel chain. it will be done with the help of RunnableParallel

parallel_chain = RunnableParallel(
    {
        "notes": model1 | prompt1 | parser,
        "mcqs": model2 | prompt2 | parser,
    }
)

merge_chain  = prompt3 | model1 | parser

chain =  parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64."""

result = chain.invoke({"text":text})

print(merge_chain)
