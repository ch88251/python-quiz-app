import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QRadioButton, 
                             QCheckBox, QButtonGroup, QMessageBox, QProgressBar,
                             QMenuBar, QComboBox, QDialog, QTableWidget, 
                             QTableWidgetItem, QLineEdit, QTextEdit, QDialogButtonBox,
                             QFormLayout, QHeaderView, QAbstractItemView)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction
from quiz_db import QuizDatabase


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quiz_data = []
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.db = QuizDatabase()
        self.subjects = []
        self.current_subject = None
        self.init_ui()
        self.load_subjects()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Quiz Application")
        self.setGeometry(100, 100, 1200, 800)
        self.setFixedSize(1200, 800)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Subject selection dropdown
        subject_layout = QHBoxLayout()
        subject_label = QLabel("Select Subject:")
        subject_label.setFont(QFont("Arial", 12))
        subject_layout.addWidget(subject_label)
        
        self.subject_combo = QComboBox()
        self.subject_combo.setMinimumHeight(35)
        self.subject_combo.currentIndexChanged.connect(self.on_subject_changed)
        subject_layout.addWidget(self.subject_combo)
        subject_layout.addStretch()
        
        main_layout.addLayout(subject_layout)
        
        # Title label
        self.title_label = QLabel("Quiz Application")
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
        instruction_font.setPointSize(12)
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
        
        self.prev_button = QPushButton("Previous")
        self.prev_button.setMinimumHeight(40)
        self.prev_button.setMaximumWidth(120)
        self.prev_button.clicked.connect(self.previous_question)
        self.prev_button.setEnabled(False)
        button_layout.addWidget(self.prev_button)
        
        self.next_button = QPushButton("Next")
        self.next_button.setMinimumHeight(40)
        self.next_button.setMaximumWidth(120)
        self.next_button.clicked.connect(self.next_question)
        button_layout.addWidget(self.next_button)
        
        self.submit_button = QPushButton("Submit Quiz")
        self.submit_button.setMinimumHeight(40)
        self.submit_button.setMaximumWidth(120)
        self.submit_button.clicked.connect(self.submit_quiz)
        self.submit_button.setVisible(False)
        button_layout.addWidget(self.submit_button)
        
        main_layout.addLayout(button_layout)
        
        # Apply some styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QMenuBar {
                background-color: lightgray;
                font-size: 16px;
            }
            QComboBox {
                background-color: white;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
                color: black;
            }
            QComboBox:hover {
                border: 2px solid #45a049;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                selection-background-color: #4CAF50;
                selection-color: white;
                border: 1px solid #4CAF50;
                padding: 5px;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px;
                min-height: 25px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #45a049;
                color: white;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QRadioButton, QCheckBox {
                font-size: 16px;
                padding: 8px;
            }
            QRadioButton::indicator, QCheckBox::indicator {
                width: 24px;
                height: 24px;
            }
        """)
    
    def create_menu_bar(self):
        """Create the menu bar with App and Help menus."""
        menubar = self.menuBar()
        
        # App menu (left side)
        app_menu = menubar.addMenu("App")
        
        # Exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        app_menu.addAction(exit_action)
        
        # Create a separate menu bar for the Admin and Help menus on the right
        # Using setCornerWidget to position Admin and Help menus on the right
        right_menubar = QMenuBar(menubar)
        
        # Admin menu
        admin_menu = right_menubar.addMenu("Admin")
        
        # Subject Management action
        subject_mgmt_action = QAction("Subject Management", self)
        subject_mgmt_action.triggered.connect(self.show_subject_management)
        admin_menu.addAction(subject_mgmt_action)
        
        # Question Management action
        question_mgmt_action = QAction("Question Management", self)
        question_mgmt_action.triggered.connect(self.show_question_management)
        admin_menu.addAction(question_mgmt_action)
        
        # Help menu
        help_menu = right_menubar.addMenu("Help")
        
        # About action
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        
        # Set the right menubar as a corner widget
        menubar.setCornerWidget(right_menubar, Qt.Corner.TopRightCorner)
    
    def show_about_dialog(self):
        """Display the About dialog."""
        about_text = """
        <h2>Quiz Application</h2>
        <p><b>Version:</b> 1.0.0</p>
        <p><b>Created by:</b> Charles Hayes</p>
        """
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("About Quiz Application")
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setText(about_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
    
    def show_subject_management(self):
        """Display the Subject Management dialog."""
        dialog = SubjectManagementDialog(self.db, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_subjects()
    
    def show_question_management(self):
        """Display the Question Management dialog."""
        dialog = QuestionManagementDialog(self.db, self)
        dialog.exec()
        
    def load_subjects(self):
        """Load available subjects from the database."""
        try:
            # Connect to database
            if not self.db.connect():
                QMessageBox.critical(
                    self, 
                    "Database Error", 
                    "Could not connect to PostgreSQL database.\n\n"
                    "Please ensure:\n"
                    "1. Docker container is running (cd db && docker-compose up -d)\n"
                    "2. Database has been migrated (python migrate_to_postgres.py)"
                )
                sys.exit(1)
            
            # Load subjects from database
            self.subjects = self.db.get_all_subjects()
            
            if not self.subjects:
                QMessageBox.critical(
                    self,
                    "No Data",
                    "No subjects found in the database.\n\n"
                    "You must reseed the database with initial data.\n"
                )
                sys.exit(1)
            
            # Populate subject combo box
            self.subject_combo.blockSignals(True)
            for subject in self.subjects:
                self.subject_combo.addItem(subject['name'], subject['id'])
            self.subject_combo.blockSignals(False)
            
            # Automatically select first subject
            if self.subjects:
                self.on_subject_changed(0)
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Error", 
                f"Failed to load subjects:\n{str(e)}"
            )
            sys.exit(1)
    
    def on_subject_changed(self, index):
        """Handle subject selection change."""
        if index < 0:
            return
        
        subject_id = self.subject_combo.currentData()
        subject_name = self.subject_combo.currentText()
        
        # Update title label
        self.title_label.setText(f"{subject_name} Quiz")
        
        # Store current subject
        self.current_subject = subject_id
        
        # Load questions for this subject
        self.load_quiz()
    
    def load_quiz(self):
        """Load quiz questions for the current subject from PostgreSQL database."""
        if self.current_subject is None:
            return
        
        try:
            # Load questions from database for current subject
            self.quiz_data = self.db.get_questions_by_subject(self.current_subject, shuffle=True)
            
            if not self.quiz_data:
                QMessageBox.warning(
                    self,
                    "No Questions",
                    "No questions found for this subject.\n\n"
                    "Please add questions to the database."
                )
                return
            
            # Initialize user_answers list
            self.user_answers = [None] * len(self.quiz_data)
            
            # Set progress bar maximum
            self.progress_bar.setMaximum(len(self.quiz_data))
            
            # Display first question
            self.display_question()
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Error", 
                f"Failed to load quiz questions:\n{str(e)}"
            )
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
            review_button = review_msg.addButton("Review Answers", QMessageBox.ButtonRole.YesRole)
            restart_button = review_msg.addButton("Restart Quiz", QMessageBox.ButtonRole.NoRole)
            exit_button = review_msg.addButton("Exit", QMessageBox.ButtonRole.RejectRole)
            
            review_msg.exec()
            clicked_button = review_msg.clickedButton()
            
            if clicked_button == review_button:
                self.review_answers()
            elif clicked_button == restart_button:
                self.restart_quiz()
            else:  # Exit button
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
            # Disconnect any existing connections before reconnecting
            # PyQt6's disconnect() raises TypeError if no connections exist
            try:
                self.next_button.disconnect()
            except TypeError:
                # No existing connections, which is fine
                pass
            self.next_button.clicked.connect(self.next_review_question)
        
        if self.current_question > 0:
            # Disconnect any existing connections before reconnecting
            # PyQt6's disconnect() raises TypeError if no connections exist
            try:
                self.prev_button.disconnect()
            except TypeError:
                # No existing connections, which is fine
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
        restart_button = msg.addButton("Restart Quiz", QMessageBox.ButtonRole.YesRole)
        exit_button = msg.addButton("Exit", QMessageBox.ButtonRole.NoRole)
        
        msg.exec()
        clicked_button = msg.clickedButton()
        
        if clicked_button == restart_button:
            self.restart_quiz()
        else:  # Exit
            self.close()
    
    def restart_quiz(self):
        """Restart the quiz with shuffled questions."""
        self.current_question = 0
        self.score = 0
        
        # Reload questions for current subject (shuffled)
        if self.current_subject:
            self.quiz_data = self.db.get_questions_by_subject(self.current_subject, shuffle=True)
        
        # Reset answers
        self.user_answers = [None] * len(self.quiz_data)
        
        # Reset instruction label style
        instruction_font = QFont()
        instruction_font.setPointSize(10)
        instruction_font.setItalic(True)
        self.instruction_label.setFont(instruction_font)
        self.instruction_label.setStyleSheet("color: #666;")
        
        # Reconnect buttons to normal mode
        # Disconnect any existing connections before reconnecting
        # PyQt6's disconnect() raises TypeError if no connections exist
        try:
            self.next_button.disconnect()
            self.prev_button.disconnect()
        except TypeError:
            # No existing connections, which is fine
            pass
        
        self.next_button.clicked.connect(self.next_question)
        self.prev_button.clicked.connect(self.previous_question)
        
        # Display first question
        self.display_question()
    
    def closeEvent(self, event):
        """Clean up database connection when closing the application."""
        if hasattr(self, 'db') and self.db:
            self.db.close()
        event.accept()


class SubjectManagementDialog(QDialog):
    """Dialog for managing subjects/categories."""
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.init_ui()
        
    def init_ui(self):
        """Initialize the subject management UI."""
        self.setWindowTitle("Subject Management")
        self.setGeometry(200, 200, 900, 600)
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Subject Management")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Subject management view
        subjects_widget = CategoriesView(self.db, self)
        layout.addWidget(subjects_widget)
        
        # Close button
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        button_box.rejected.connect(self.accept)
        layout.addWidget(button_box)


class QuestionManagementDialog(QDialog):
    """Dialog for managing questions."""
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.init_ui()
        
    def init_ui(self):
        """Initialize the question management UI."""
        self.setWindowTitle("Question Management")
        self.setGeometry(200, 200, 900, 600)
        
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("Question Management")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Question management view
        questions_widget = QuestionsView(self.db, self)
        layout.addWidget(questions_widget)
        
        # Close button
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        button_box.rejected.connect(self.accept)
        layout.addWidget(button_box)


class CategoriesView(QWidget):
    """Widget for managing categories/subjects."""
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_dialog = parent
        self.init_ui()
        self.load_categories()
        
    def init_ui(self):
        """Initialize the categories view UI."""
        layout = QVBoxLayout(self)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        add_button = QPushButton("Add Subject")
        add_button.clicked.connect(self.add_subject)
        button_layout.addWidget(add_button)
        
        edit_button = QPushButton("Edit Subject")
        edit_button.clicked.connect(self.edit_subject)
        button_layout.addWidget(edit_button)
        
        delete_button = QPushButton("Delete Subject")
        delete_button.clicked.connect(self.delete_subject)
        button_layout.addWidget(delete_button)
        
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        # Subjects table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Description"])
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        
        layout.addWidget(self.table)
        
    def load_categories(self):
        """Load categories from the database."""
        categories = self.db.get_all_subjects()
        
        self.table.setRowCount(0)
        for subject in categories:
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            self.table.setItem(row, 0, QTableWidgetItem(str(subject['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(subject['name']))
            self.table.setItem(row, 2, QTableWidgetItem(subject.get('description', '')))
            
    def add_subject(self):
        """Add a new subject."""
        dialog = SubjectDialog(self.db, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_categories()
            
    def edit_subject(self):
        """Edit the selected subject."""
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select a subject to edit.")
            return
            
        row = selected_rows[0].row()
        subject_id = int(self.table.item(row, 0).text())
        subject_name = self.table.item(row, 1).text()
        subject_desc = self.table.item(row, 2).text()
        
        dialog = SubjectDialog(self.db, self, subject_id, subject_name, subject_desc)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_categories()
            
    def delete_subject(self):
        """Delete the selected subject."""
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select a subject to delete.")
            return
            
        row = selected_rows[0].row()
        subject_id = int(self.table.item(row, 0).text())
        subject_name = self.table.item(row, 1).text()
        
        # Confirm deletion
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Confirm Deletion")
        msg.setText(f"Are you sure you want to delete the subject '{subject_name}'?")
        msg.setInformativeText("This will also delete all associated questions and answers!")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            if self.db.delete_subject(subject_id):
                QMessageBox.information(self, "Success", "Subject deleted successfully.")
                self.load_categories()
            else:
                QMessageBox.critical(self, "Error", "Failed to delete subject.")

class SubjectDialog(QDialog):
    """Dialog for adding or editing a subject."""
    
    def __init__(self, db, parent=None, subject_id=None, name="", description=""):
        super().__init__(parent)
        self.db = db
        self.subject_id = subject_id
        self.is_edit = subject_id is not None
        self.init_ui(name, description)
        
    def init_ui(self, name, description):
        """Initialize the subject dialog UI."""
        self.setWindowTitle("Edit Subject" if self.is_edit else "Add Subject")
        self.setGeometry(300, 300, 400, 200)
        
        layout = QFormLayout(self)
        
        # Name field
        self.name_edit = QLineEdit(name)
        layout.addRow("Name:", self.name_edit)
        
        # Description field
        self.description_edit = QTextEdit(description)
        self.description_edit.setMaximumHeight(100)
        layout.addRow("Description:", self.description_edit)
        
        # Buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.save_subject)
        button_box.rejected.connect(self.reject)
        layout.addRow(button_box)
        
    def save_subject(self):
        """Save the subject to the database."""
        name = self.name_edit.text().strip()
        description = self.description_edit.toPlainText().strip()
        
        if not name:
            QMessageBox.warning(self, "Validation Error", "Subject name is required.")
            return
            
        if self.is_edit:
            # Update existing subject
            if self.db.update_subject(self.subject_id, name, description):
                QMessageBox.information(self, "Success", "Subject updated successfully.")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Failed to update subject.")
        else:
            # Add new subject
            if self.db.add_subject(name, description):
                QMessageBox.information(self, "Success", "Subject added successfully.")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Failed to add subject.")


class QuestionsView(QWidget):
    """Widget for managing questions."""
    
    # Constants for question text display
    MAX_QUESTION_LENGTH = 100
    TRUNCATE_LENGTH = 97
    
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.parent_dialog = parent
        self.init_ui()
        self.load_questions()
        
    def init_ui(self):
        """Initialize the questions view UI."""
        layout = QVBoxLayout(self)
        
        # Filter by subject
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Filter by Subject:")
        filter_layout.addWidget(filter_label)
        
        self.subject_filter = QComboBox()
        self.subject_filter.addItem("All Subjects", None)
        
        # Load subjects
        subjects = self.db.get_all_subjects()
        for subject in subjects:
            self.subject_filter.addItem(subject['name'], subject['id'])
        
        self.subject_filter.currentIndexChanged.connect(self.load_questions)
        filter_layout.addWidget(self.subject_filter)
        filter_layout.addStretch()
        
        layout.addLayout(filter_layout)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        add_button = QPushButton("Add Question")
        add_button.clicked.connect(self.add_question)
        button_layout.addWidget(add_button)
        
        edit_button = QPushButton("Edit Question")
        edit_button.clicked.connect(self.edit_question)
        button_layout.addWidget(edit_button)
        
        delete_button = QPushButton("Delete Question")
        delete_button.clicked.connect(self.delete_question)
        button_layout.addWidget(delete_button)
        
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        # Questions table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Subject", "Question", "Type"])
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        
        layout.addWidget(self.table)
        
    def load_questions(self):
        """Load questions from the database."""
        questions = self.db.get_all_questions()
        
        # Filter by selected subject
        selected_subject_id = self.subject_filter.currentData()
        if selected_subject_id is not None:
            questions = [q for q in questions if q['subject_id'] == selected_subject_id]
        
        self.table.setRowCount(0)
        for question in questions:
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            self.table.setItem(row, 0, QTableWidgetItem(str(question['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(question['subject_name']))
            
            # Truncate question text if too long
            question_text = question['question_text']
            if len(question_text) > self.MAX_QUESTION_LENGTH:
                question_text = question_text[:self.TRUNCATE_LENGTH] + "..."
            self.table.setItem(row, 2, QTableWidgetItem(question_text))
            
            self.table.setItem(row, 3, QTableWidgetItem(question['question_type']))
            
    def add_question(self):
        """Add a new question."""
        dialog = QuestionDialog(self.db, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_questions()
            
    def edit_question(self):
        """Edit the selected question."""
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select a question to edit.")
            return
            
        row = selected_rows[0].row()
        question_id = int(self.table.item(row, 0).text())
        
        dialog = QuestionDialog(self.db, self, question_id)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_questions()
            
    def delete_question(self):
        """Delete the selected question."""
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select a question to delete.")
            return
            
        row = selected_rows[0].row()
        question_id = int(self.table.item(row, 0).text())
        question_text = self.table.item(row, 2).text()
        
        # Confirm deletion
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Confirm Deletion")
        msg.setText("Are you sure you want to delete this question?")
        msg.setInformativeText(f"Question: {question_text}")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            if self.db.delete_question(question_id):
                QMessageBox.information(self, "Success", "Question deleted successfully.")
                self.load_questions()
            else:
                QMessageBox.critical(self, "Error", "Failed to delete question.")


class QuestionDialog(QDialog):
    """Dialog for adding or editing a question."""
    
    def __init__(self, db, parent=None, question_id=None):
        super().__init__(parent)
        self.db = db
        self.question_id = question_id
        self.is_edit = question_id is not None
        self.option_inputs = {}
        self.correct_answer_checks = {}
        self.init_ui()
        
        if self.is_edit:
            self.load_question()
        
    def init_ui(self):
        """Initialize the question dialog UI."""
        self.setWindowTitle("Edit Question" if self.is_edit else "Add Question")
        self.setGeometry(250, 250, 600, 500)
        
        layout = QVBoxLayout(self)
        
        # Subject selection
        subject_layout = QHBoxLayout()
        subject_layout.addWidget(QLabel("Subject:"))
        self.subject_combo = QComboBox()
        
        subjects = self.db.get_all_subjects()
        for subject in subjects:
            self.subject_combo.addItem(subject['name'], subject['id'])
        
        subject_layout.addWidget(self.subject_combo)
        subject_layout.addStretch()
        layout.addLayout(subject_layout)
        
        # Question text
        layout.addWidget(QLabel("Question:"))
        self.question_edit = QTextEdit()
        self.question_edit.setMaximumHeight(100)
        layout.addWidget(self.question_edit)
        
        # Question type
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        self.type_combo = QComboBox()
        self.type_combo.addItem("Multiple Choice (Single Answer)", "multiple_choice")
        self.type_combo.addItem("Multi-Select (Multiple Answers)", "multi_select")
        type_layout.addWidget(self.type_combo)
        type_layout.addStretch()
        layout.addLayout(type_layout)
        
        # Options section
        layout.addWidget(QLabel("Options (mark correct answers):"))
        
        options_widget = QWidget()
        options_layout = QVBoxLayout(options_widget)
        
        for key in ['A', 'B', 'C', 'D', 'E', 'F']:
            option_layout = QHBoxLayout()
            
            correct_check = QCheckBox(f"{key}:")
            self.correct_answer_checks[key] = correct_check
            option_layout.addWidget(correct_check)
            
            option_input = QLineEdit()
            self.option_inputs[key] = option_input
            option_layout.addWidget(option_input)
            
            options_layout.addLayout(option_layout)
        
        layout.addWidget(options_widget)
        
        # Buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.save_question)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
    def load_question(self):
        """Load question data for editing."""
        question_data = self.db.get_question_by_id(self.question_id)
        
        if not question_data:
            QMessageBox.critical(self, "Error", "Failed to load question data.")
            self.reject()
            return
        
        # Set subject
        for i in range(self.subject_combo.count()):
            if self.subject_combo.itemData(i) == question_data['subject_id']:
                self.subject_combo.setCurrentIndex(i)
                break
        
        # Set question text
        self.question_edit.setPlainText(question_data['question_text'])
        
        # Set question type
        for i in range(self.type_combo.count()):
            if self.type_combo.itemData(i) == question_data['question_type']:
                self.type_combo.setCurrentIndex(i)
                break
        
        # Set options
        for key, text in question_data['options'].items():
            if key in self.option_inputs:
                self.option_inputs[key].setText(text)
        
        # Set correct answers
        for key in question_data['correct_answers']:
            if key in self.correct_answer_checks:
                self.correct_answer_checks[key].setChecked(True)
        
    def save_question(self):
        """Save the question to the database."""
        subject_id = self.subject_combo.currentData()
        question_text = self.question_edit.toPlainText().strip()
        question_type = self.type_combo.currentData()
        
        if not question_text:
            QMessageBox.warning(self, "Validation Error", "Question text is required.")
            return
        
        # Collect options
        options = {}
        for key, input_widget in self.option_inputs.items():
            text = input_widget.text().strip()
            if text:
                options[key] = text
        
        if len(options) < 2:
            QMessageBox.warning(self, "Validation Error", "At least 2 options are required.")
            return
        
        # Collect correct answers
        correct_answers = []
        for key, check_widget in self.correct_answer_checks.items():
            if check_widget.isChecked() and key in options:
                correct_answers.append(key)
        
        if not correct_answers:
            QMessageBox.warning(self, "Validation Error", "At least 1 correct answer is required.")
            return
        
        if self.is_edit:
            # Update existing question
            if self.db.update_question(self.question_id, subject_id, question_text, 
                                      question_type, options, correct_answers):
                QMessageBox.information(self, "Success", "Question updated successfully.")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Failed to update question.")
        else:
            # Add new question
            if self.db.add_question(subject_id, question_text, question_type, 
                                   options, correct_answers):
                QMessageBox.information(self, "Success", "Question added successfully.")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Failed to add question.")


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
