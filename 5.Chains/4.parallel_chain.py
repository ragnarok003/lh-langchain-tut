from typing import final

from langchain_core import runnables
from langchain_ollama import ChatOllama
from rich.markdown import Markdown
from rich.console import Console
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

csl =Console()

model_1 = ChatOllama(model="gemma4:e2b", temperature=0.0)
model_2 = ChatOllama(model="gemma4:e4b", temperature=0.0)

prompt_1 = PromptTemplate(
    template="Generate short and simple note from following topic {topic}",
    input_variables=["topic"],
)
prompt_2 = PromptTemplate(
    template="Generate 5 short  question ans answer from following text {text}",
    input_variables=["text"],
)
prompt_3 = PromptTemplate(
    template="Merge the provided notes and question answers into single document {notes} {qa}",
    input_variables=["notes", "qa"],
)
parser = StrOutputParser()
runnable_chain = RunnableParallel(
    {"notes": prompt_1 | model_1 | parser, "qa": prompt_2 | model_2 | parser}
)

merge_chain = prompt_3 | model_1 | parser

final_chain = runnable_chain | merge_chain

text = """Support vector machines (SVMS) are a set of supervised learning methods used for classification,
regression and outliers detection.
The advantages of support vector machines are:
Effective in high dimensional spaces.
still effective in cases where number of dimensions is greater than the number of samples.
Uses a subset of training points in the decision function (called support vectors), so it is
also memory efficient. I
Versatile: different Kernel functions can be specified for the decision function. Common kernels
are provided, but it is also possible to specify custom kernels.
The disadvantages of support vector machines include:
If the number of features is much greater than the number of samples, avoid over-fitting in
choosing Kernel functions and regularization term is crucial.
SVMS do not directly provide probability estimates, these are calculated using an expensive
five-fold cross-validation (see Scores and probabilities, below).
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to
that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an
SVM to make predictions for sparse data, it must have been fit on such data. For optimal
performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with
dtype=float64."""

result =final_chain.invoke(text)
csl.print(Markdown(result))