from question import Question
from data import question_data
from quize_brain import Quize_brain_class



question_bank=[]


for data in question_data:
    q=data["text"]
    A=data["answer"]
    next_que=Question(q,A)
    question_bank.append(next_que)


quize=Quize_brain_class(question_bank)

# print(question_bank)
while(quize.still_que()):
    quize.next_question()
