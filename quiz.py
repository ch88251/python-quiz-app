import json
import textwrap

def load_quiz(filename):
    """Load quiz questions from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)["quiz"]

def print_wrapped_text(text, width=80):
    """Prints text wrapped to the specified width while avoiding word breaks."""
    wrapped_text = textwrap.fill(text, width=width)
    print(f"{wrapped_text}\n")

def ask_question(question_data, question_number, total_questions):
    """Ask a question, displaying its number and total count, then get user input."""
    print(f"\nQuestion {question_number} / {total_questions}\n")
    print_wrapped_text(question_data["question"])

    for key, value in question_data["options"].items():
        wrapped_option = textwrap.fill(f"{key}. {value}", width=80, subsequent_indent="   ")
        print(wrapped_option)

    answer = input("Enter your answer: ").strip().upper()
    
    if question_data["type"] == "true_false":
        while answer not in ["TRUE", "FALSE"]:
            answer = input("Invalid input. Enter 'true' or 'false': ").strip().lower()
    else:
        while answer not in question_data["options"].keys():
            answer = input(f"Invalid input. Enter one of {', '.join(question_data['options'].keys())}: ").strip().upper()
    
    return answer

def run_quiz(quiz_data):
    """Run the quiz and track score."""
    score = 0
    total_questions = len(quiz_data)

    for i, question in enumerate(quiz_data, start=1):
        user_answer = ask_question(question, i, total_questions)
        correct_answer = question["correct_answer"]

        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {correct_answer}")

    print(f"\nFinal Score: {score}/{total_questions}")

if __name__ == "__main__":
    quiz_data = load_quiz("quiz.json")
    run_quiz(quiz_data)
