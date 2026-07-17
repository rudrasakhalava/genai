from langchain_core.prompts import PromptTemplate

template = PromptTemplate(template="""please summarize the topic titled :: {paper_input} with following specification,Explanation length : {length_input} and Explanation style : {style_input}. here Explanation length short means in 3-4 lines.""",
                            input_variables=["paper_input","length_input","style_input"],
                            validate_template=True
                          )

template.save("template.json")