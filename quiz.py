import psycopg2
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        exit(1)

def fetch_questions():
    """Fetch quiz questions and their options from the database."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT q.id, q.question_text, q.question_type, q.correct_answer, 
               o.option_letter, o.option_text 
        FROM questions q 
        LEFT JOIN options o ON q.id = o.question_id 
        ORDER BY q.id, o.option_letter;
    """)
    
    rows = cursor.fetchall()
    conn.close()

    # Organize data into a structured format
    questions = {}
    for row in rows:
        question_id, question_text, question_type, correct_answer, option_letter, option_text = row
        
        if question_id not in questions:
            questions[question_id] = {
                "question": question_text,
                "type": question_type,
                "options": {},
                "correct_answer": correct_answer
            }
        
        if option_letter:  # Store multiple-choice options
            questions[question_id]["options"][option_letter] = option_text

    return list(questions.values())

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

    answer = input("Enter your answer: ").strip().upper()

    # Validate input
    if question_data["type"] == "true_false":
        while answer not in ["TRUE", "FALSE"]:
            answer = input("Invalid input. Enter 'true' or 'false': ").strip().lower()
    else:
        while answer not in question_data["options"].keys():
            answer = input(f"Invalid input. Enter one of {', '.join(question_data['options'].keys())}: ").strip().upper()

    return answer

def run_quiz():
    """Run the quiz and track score."""
    quiz_data = fetch_questions()
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
    run_quiz()
