class QuizBrain:
  
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0

  def next_question(self):
    current_q = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_q.question} (True/False)? ")
    self.check_answer(user_answer, current_q.correct_answer)

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("Correct! ✅")
    else:
      print("Wrong Answer! ❌")
    print(f"The correct answer was: {correct_answer}")
    print(f"Your current score is {self.score}/{self.question_number}\n")

  def final_score(self):
    print("-----------------------\nYou've completed the quiz!")
    print(f"Your final score was {self.score}/{self.question_number}\n")