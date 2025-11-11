from crewai.tools import tool

@tool
def count_letters(sentence:str):
 """
 This function counts the amount of letters in a sentence.
 This input is a 'sentence' string, the output is an integer.
 """ #crewai가 이 docstring을 보고 schema를 생성(함수에 대한 설명). 중요!
 print(f"tool called with input : ", sentence)
 return len(sentence)