# messingwithtypes.py
# Author: Nur Bujang
# messing with variable types 


# variable names are case sensitive, so Answer is wrong. And dont have variables that are only differentiated by lower and upper cases eh Answer and answer
# Answer=12
# NameError: name 'answer' is not defined
# variable names must not start with an integer, eg 100answers. Must start with small letter
# 100answers=[]
# SyntaxError: invalid syntax
# if the variable name is long, put underscores between them. DO NOT FOLLOW JAVA: AnswerOfQuestion

# answer_of_question="asdf"
# answer=12
# print(f"answer is {answer_of_question}")
# or
# print(f"answer is " + answer_of_question)


# if answer_of_question is an integer, eg:
# answer_of_question=11
# print(f"answer is {answer_of_question}")
# or
# print(f"answer is " + answer_of_question)
# TypeError: can only concatenate str (not "int") to str

# So, you need to so str convert into a string
# answer_of_question=11
# print(f"answer is {answer_of_question}")
# or
# print(f"answer is " + str(answer_of_question))

# if you want to get the type of a variable,
# print(f"type of answer is {type(answer_of_question)}")
# it will print out the type of the variable: type of answer is <class 'int'>

# if answer_of_question is a string
answer_of_question="asdf"
print(f"answer is {answer_of_question}")
# or
print(f"answer is " + str(answer_of_question))
print(f"type of answer is {type(answer_of_question)}")
# it will print out: type of answer is <class 'str'>

# important: Type does not return a string. It actually returns a different variable type
# So what is the type of the type?
print(f"type of type {type(type(answer_of_question))}")
# type of type <class 'type'>, meaning there is a variable type called type. 