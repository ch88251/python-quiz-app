import sys
import json
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QRadioButton, 
                             QCheckBox, QButtonGroup, QMessageBox, QProgressBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quiz_data = []
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.init_ui()
        self.load_quiz()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Python Quiz App")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Title label
        self.title_label = QLabel("Python Quiz App")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.title_label)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)
        
        # Question number label
        self.question_number_label = QLabel("")
        question_num_font = QFont()
        question_num_font.setPointSize(12)
        question_num_font.setBold(True)
        self.question_number_label.setFont(question_num_font)
        main_layout.addWidget(self.question_number_label)
        
        # Question label
        self.question_label = QLabel("")
        question_font = QFont()
        question_font.setPointSize(14)
        self.question_label.setFont(question_font)
        self.question_label.setWordWrap(True)
        self.question_label.setMinimumHeight(100)
        main_layout.addWidget(self.question_label)
        
        # Instruction label (for multi-select questions)
        self.instruction_label = QLabel("")
        instruction_font = QFont()
        instruction_font.setPointSize(10)
        instruction_font.setItalic(True)
        self.instruction_label.setFont(instruction_font)
        self.instruction_label.setStyleSheet("color: #666;")
        main_layout.addWidget(self.instruction_label)
        
        # Options container
        self.options_widget = QWidget()
        self.options_layout = QVBoxLayout(self.options_widget)
        self.options_layout.setSpacing(10)
        main_layout.addWidget(self.options_widget)
        
        # Button group for radio buttons (single choice)
        self.radio_group = QButtonGroup()
        
        # List to store checkboxes (multi choice)
        self.checkboxes = []
        
        # Spacer to push buttons to bottom
        main_layout.addStretch()
        
        # Navigation buttons
        button_layout = QHBoxLayout()
        
        self.prev_button = QPushButton("← Previous")
        self.prev_button.setMinimumHeight(40)
        self.prev_button.clicked.connect(self.previous_question)
        self.prev_button.setEnabled(False)
        button_layout.addWidget(self.prev_button)
        
        self.next_button = QPushButton("Next →")
        self.next_button.setMinimumHeight(40)
        self.next_button.clicked.connect(self.next_question)
        button_layout.addWidget(self.next_button)
        
        self.submit_button = QPushButton("Submit Quiz")
        self.submit_button.setMinimumHeight(40)
        self.submit_button.clicked.connect(self.submit_quiz)
        self.submit_button.setVisible(False)
        button_layout.addWidget(self.submit_button)
        
        main_layout.addLayout(button_layout)
        
        # Apply some styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QRadioButton, QCheckBox {
                font-size: 13px;
                padding: 8px;
            }
            QRadioButton::indicator, QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """)
        
    def load_quiz(self):
        """Load quiz questions from JSON file and shuffle them."""
        try:
            with open("quiz.json", "r") as file:
                quiz_json = json.load(file)
                self.quiz_data = quiz_json["quiz"]
            
            # Shuffle questions
            random.shuffle(self.quiz_data)
            
            # Initialize user_answers list
            self.user_answers = [None] * len(self.quiz_data)
            
            # Set progress bar maximum
            self.progress_bar.setMaximum(len(self.quiz_data))
            
            # Display first question
            self.display_question()
            
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "quiz.json file not found!")
            sys.exit(1)
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Invalid JSON format in quiz.json!")
            sys.exit(1)
    
    def display_question(self):
        """Display the current question and its options."""
        if self.current_question >= len(self.quiz_data):
            return
        
        question_data = self.quiz_data[self.current_question]
        
        # Update question number
        self.question_number_label.setText(
            f"Question {self.current_question + 1} of {len(self.quiz_data)}"
        )
        
        # Update progress bar
        self.progress_bar.setValue(self.current_question)
        
        # Update question text
        self.question_label.setText(question_data["question"])
        
        # Clear previous options
        self.clear_options()
        
        # Determine if multi-select question
        correct_answer = question_data["correct_answer"]
        is_multi_select = isinstance(correct_answer, list) and len(correct_answer) > 1
        
        # Update instruction label
        if is_multi_select:
            self.instruction_label.setText("Select all that apply:")
        else:
            self.instruction_label.setText("Select one answer:")
        
        # Create options
        options = question_data["options"]
        
        if is_multi_select:
            # Create checkboxes for multi-select
            self.checkboxes = []
            for key in sorted(options.keys()):
                checkbox = QCheckBox(f"{key}. {options[key]}")
                self.checkboxes.append((key, checkbox))
                self.options_layout.addWidget(checkbox)
                
                # Restore previous answer if any
                if self.user_answers[self.current_question]:
                    if key in self.user_answers[self.current_question]:
                        checkbox.setChecked(True)
        else:
            # Create radio buttons for single-select
            for key in sorted(options.keys()):
                radio = QRadioButton(f"{key}. {options[key]}")
                self.radio_group.addButton(radio)
                self.options_layout.addWidget(radio)
                
                # Restore previous answer if any
                if self.user_answers[self.current_question]:
                    if key in self.user_answers[self.current_question]:
                        radio.setChecked(True)
        
        # Update navigation buttons
        self.prev_button.setEnabled(self.current_question > 0)
        
        # Show submit button on last question
        if self.current_question == len(self.quiz_data) - 1:
            self.next_button.setVisible(False)
            self.submit_button.setVisible(True)
        else:
            self.next_button.setVisible(True)
            self.submit_button.setVisible(False)
    
    def clear_options(self):
        """Clear all option widgets."""
        # Remove all radio buttons from group
        for button in self.radio_group.buttons():
            self.radio_group.removeButton(button)
            button.deleteLater()
        
        # Clear checkboxes list
        self.checkboxes = []
        
        # Clear all widgets from options layout
        while self.options_layout.count():
            item = self.options_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def get_current_answer(self):
        """Get the user's answer for the current question."""
        question_data = self.quiz_data[self.current_question]
        correct_answer = question_data["correct_answer"]
        is_multi_select = isinstance(correct_answer, list) and len(correct_answer) > 1
        
        if is_multi_select:
            # Get selected checkboxes
            selected = []
            for key, checkbox in self.checkboxes:
                if checkbox.isChecked():
                    selected.append(key)
            return sorted(selected) if selected else None
        else:
            # Get selected radio button
            for button in self.radio_group.buttons():
                if button.isChecked():
                    # Extract the key (first character before the dot)
                    text = button.text()
                    key = text.split('.')[0].strip()
                    return [key]
            return None
    
    def save_current_answer(self):
        """Save the current answer before navigating."""
        answer = self.get_current_answer()
        self.user_answers[self.current_question] = answer
    
    def next_question(self):
        """Move to the next question."""
        self.save_current_answer()
        
        if self.current_question < len(self.quiz_data) - 1:
            self.current_question += 1
            self.display_question()
    
    def previous_question(self):
        """Move to the previous question."""
        self.save_current_answer()
        
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question()
    
    def submit_quiz(self):
        """Submit the quiz and calculate the score."""
        self.save_current_answer()
        
        # Check if all questions are answered
        unanswered = []
        for i, answer in enumerate(self.user_answers):
            if answer is None:
                unanswered.append(i + 1)
        
        if unanswered:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Unanswered Questions")
            msg.setText(f"You have {len(unanswered)} unanswered question(s).")
            msg.setInformativeText(f"Questions: {', '.join(map(str, unanswered))}\n\nDo you want to submit anyway?")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setDefaultButton(QMessageBox.StandardButton.No)
            
            if msg.exec() == QMessageBox.StandardButton.No:
                return
        
        # Calculate score
        self.score = 0
        for i, question in enumerate(self.quiz_data):
            correct_answer = sorted(set(question["correct_answer"]))
            user_answer = self.user_answers[i] if self.user_answers[i] else []
            
            if sorted(set(user_answer)) == correct_answer:
                self.score += 1
        
        # Show results
        self.show_results()
    
    def show_results(self):
        """Display the quiz results."""
        percentage = (self.score / len(self.quiz_data)) * 100
        
        # Create results message
        result_text = f"Quiz Complete!\n\n"
        result_text += f"Final Score: {self.score} / {len(self.quiz_data)}\n"
        result_text += f"Percentage: {percentage:.1f}%\n\n"
        
        # Add performance rating
        if percentage >= 90:
            result_text += "Excellent work! 🌟"
        elif percentage >= 70:
            result_text += "Good job! 👍"
        elif percentage >= 50:
            result_text += "Not bad! Keep practicing! 📚"
        else:
            result_text += "Keep studying! You can do better! 💪"
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Quiz Results")
        msg.setText(result_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if msg.exec() == QMessageBox.StandardButton.Ok:
            # Ask if user wants to review answers or restart
            review_msg = QMessageBox()
            review_msg.setIcon(QMessageBox.Icon.Question)
            review_msg.setWindowTitle("What's Next?")
            review_msg.setText("Would you like to review your answers or take the quiz again?")
            review_msg.addButton("Review Answers", QMessageBox.ButtonRole.YesRole)
            review_msg.addButton("Restart Quiz", QMessageBox.ButtonRole.NoRole)
            review_msg.addButton("Exit", QMessageBox.ButtonRole.RejectRole)
            
            result = review_msg.exec()
            
            if result == 0:  # Review Answers
                self.review_answers()
            elif result == 1:  # Restart Quiz
                self.restart_quiz()
            else:  # Exit
                self.close()
    
    def review_answers(self):
        """Show a detailed review of all answers."""
        self.current_question = 0
        self.display_question_review()
    
    def display_question_review(self):
        """Display question in review mode showing correct/incorrect answers."""
        if self.current_question >= len(self.quiz_data):
            return
        
        question_data = self.quiz_data[self.current_question]
        user_answer = self.user_answers[self.current_question] if self.user_answers[self.current_question] else []
        correct_answer = sorted(set(question_data["correct_answer"]))
        is_correct = sorted(set(user_answer)) == correct_answer
        
        # Update question number with result indicator
        result_emoji = "✅" if is_correct else "❌"
        self.question_number_label.setText(
            f"{result_emoji} Question {self.current_question + 1} of {len(self.quiz_data)}"
        )
        
        # Update question text
        self.question_label.setText(question_data["question"])
        
        # Show answer info
        if is_correct:
            self.instruction_label.setText("✅ Correct!")
            self.instruction_label.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.instruction_label.setText(
                f"❌ Incorrect! Correct answer(s): {', '.join(correct_answer)}"
            )
            self.instruction_label.setStyleSheet("color: red; font-weight: bold;")
        
        # Clear and display options (disabled)
        self.clear_options()
        
        options = question_data["options"]
        is_multi_select = isinstance(question_data["correct_answer"], list) and len(question_data["correct_answer"]) > 1
        
        if is_multi_select:
            self.checkboxes = []
            for key in sorted(options.keys()):
                checkbox = QCheckBox(f"{key}. {options[key]}")
                checkbox.setEnabled(False)
                
                if key in user_answer:
                    checkbox.setChecked(True)
                
                # Highlight correct answers
                if key in correct_answer:
                    checkbox.setStyleSheet("color: green; font-weight: bold;")
                elif key in user_answer:
                    checkbox.setStyleSheet("color: red;")
                
                self.checkboxes.append((key, checkbox))
                self.options_layout.addWidget(checkbox)
        else:
            for key in sorted(options.keys()):
                radio = QRadioButton(f"{key}. {options[key]}")
                radio.setEnabled(False)
                self.radio_group.addButton(radio)
                
                if key in user_answer:
                    radio.setChecked(True)
                
                # Highlight correct answer
                if key in correct_answer:
                    radio.setStyleSheet("color: green; font-weight: bold;")
                elif key in user_answer:
                    radio.setStyleSheet("color: red;")
                
                self.options_layout.addWidget(radio)
        
        # Update navigation buttons for review mode
        self.prev_button.setEnabled(self.current_question > 0)
        self.next_button.setVisible(True)
        self.submit_button.setVisible(False)
        
        if self.current_question == len(self.quiz_data) - 1:
            self.next_button.setText("Finish Review")
            self.next_button.disconnect()
            self.next_button.clicked.connect(self.finish_review)
        else:
            self.next_button.setText("Next →")
            try:
                self.next_button.disconnect()
            except:
                pass
            self.next_button.clicked.connect(self.next_review_question)
        
        if self.current_question > 0:
            try:
                self.prev_button.disconnect()
            except:
                pass
            self.prev_button.clicked.connect(self.prev_review_question)
    
    def next_review_question(self):
        """Move to next question in review mode."""
        if self.current_question < len(self.quiz_data) - 1:
            self.current_question += 1
            self.display_question_review()
    
    def prev_review_question(self):
        """Move to previous question in review mode."""
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question_review()
    
    def finish_review(self):
        """Finish review and ask what to do next."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Review Complete")
        msg.setText("Review complete! What would you like to do?")
        msg.addButton("Restart Quiz", QMessageBox.ButtonRole.YesRole)
        msg.addButton("Exit", QMessageBox.ButtonRole.NoRole)
        
        result = msg.exec()
        
        if result == 0:  # Restart
            self.restart_quiz()
        else:  # Exit
            self.close()
    
    def restart_quiz(self):
        """Restart the quiz with shuffled questions."""
        self.current_question = 0
        self.score = 0
        
        # Shuffle questions again
        random.shuffle(self.quiz_data)
        
        # Reset answers
        self.user_answers = [None] * len(self.quiz_data)
        
        # Reset instruction label style
        instruction_font = QFont()
        instruction_font.setPointSize(10)
        instruction_font.setItalic(True)
        self.instruction_label.setFont(instruction_font)
        self.instruction_label.setStyleSheet("color: #666;")
        
        # Reconnect buttons to normal mode
        try:
            self.next_button.disconnect()
            self.prev_button.disconnect()
        except:
            pass
        
        self.next_button.clicked.connect(self.next_question)
        self.prev_button.clicked.connect(self.previous_question)
        
        # Display first question
        self.display_question()


def main():
    app = QApplication(sys.argv)
    
    # Set application-wide font
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(10)
    app.setFont(font)
    
    quiz_window = QuizApp()
    quiz_window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
