from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

prompt1 = PromptTemplate(
    template="generate one note from given text :: \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="generate 5 mcq for quiz from given text :: \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="merge this note :: \n {note} \n and this quiz :: \n {quiz}  ",
    input_variables=["note","quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "note" : prompt1 | model | parser,
    "quiz" : prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """
A black hole is an astronomical body so compact that its gravity prevents anything, including light, from escaping. Albert Einstein's theory of general relativity, which describes gravitation as the curvature of spacetime, predicts that any sufficiently compact mass will form a black hole.[4] The boundary of no escape is called the event horizon. In general relativity, crossing a black hole's event horizon traps an object inside but produces no locally detectable change. General relativity also predicts that every black hole should have a central singularity, where the curvature of spacetime is infinite.

Objects whose gravitational fields are too strong for light to escape were first considered in the 18th century. In 1916, the first solution of general relativity that would characterise a black hole was found. By the late 1950s, this solution began to be interpreted physically as a region of space from which nothing can escape. Black holes were long considered a mathematical curiosity; it was not until the 1960s that theoretical work showed they were a generic prediction of general relativity. The first widely accepted black hole was Cygnus X-1, identified by several researchers independently in 1971.

Black holes typically form when very massive stars collapse at the end of their life cycle. After a black hole has formed, it can grow by absorbing mass from its surroundings. Supermassive black holes of millions of solar masses may form by absorbing stars and merging with other black holes, or via direct collapse of gas clouds. There is consensus that supermassive black holes exist in the centres of most galaxies.

Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the rate of emission being inversely proportional to the mass. This causes the black hole to lose mass very slowly, provided it is not accreting matter. However, even the smallest class of black holes observed, stellar black holes, are gaining mass from the cosmic microwave background faster than they are losing mass via Hawking radiation.
"""

result = chain.invoke({"text" : text})

print(result)