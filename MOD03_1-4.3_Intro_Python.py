'''
tf_quiz function

tf_quiz() has 2 parameters which are both string arguments

question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "

correct_ans: a string indicating the correct answer, either "T" or "F"

tf_quiz() returns a string: "correct" or "incorrect"
'''

def tf_quiz(question, correct_ans):
    ent_ans = input(question).upper()
    the_ans = ent_ans == correct_ans
    return(the_ans)

quiz_eval = tf_quiz("I love Berkeley ", "T")
print("Your answer is", quiz_eval)
