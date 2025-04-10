import json
import textwrap
import random

def load_quiz(filename):
    """Load quiz questions from a JSON file and shuffle them."""
    with open(filename, "r") as file:
        quiz_data = json.load(file)["quiz"]
    
    random.shuffle(quiz_data)  # Shuffle questions each time the quiz starts
    return quiz_data

def print_wrapped_text(text, width=80):
    """Prints text wrapped to the specified width while avoiding word breaks."""
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)

def ask_question(question_data, question_number, total_questions):
    """Ask a question, displaying its number and total count, then get user input."""
    print(f"\nQuestion {question_number} / {total_questions}")
    print_wrapped_text(question_data["question"])  # Wrap the question text

    for key, value in question_data["options"].items():
        wrapped_option = textwrap.fill(f"{key}. {value}", width=80, subsequent_indent="   ")
        print(wrapped_option)
    
    # Detect if it's a "select all that apply" question
    multi_answer = isinstance(question_data["correct_answer"], list) and len(question_data["correct_answer"]) > 1

    if multi_answer:
      prompt = "Enter all correct answers (comma-separated, e.g., A,C): "
    else:
      prompt = "Enter your answer: "

    valid_keys = set(question_data["options"].keys())

    while True:
      user_input = input(prompt).strip().upper().replace(" ", "")
      user_answers = user_input.split(",")
      if all(answer in valid_keys for answer in user_answers):
        break
      print(f"Invalid input. Please enter valid option letters from {', '.join(valid_keys)}.")
    
    return sorted(set(user_answers))

def run_quiz(quiz_data):
    """Run the quiz and track score."""
    score = 0
    total_questions = len(quiz_data)

    for i, question in enumerate(quiz_data, start=1):
        user_answers = ask_question(question, i, total_questions)
        correct_answers = sorted(set(question["correct_answer"]))

        if user_answers == correct_answers:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer(s): {', '.join(correct_answers)}")

    print(f"\nFinal Score: {score}/{total_questions}")

if __name__ == "__main__":
    quiz_data = load_quiz("quiz.json")  # Load and shuffle the quiz data
    run_quiz(quiz_data)  # Start the quiz
