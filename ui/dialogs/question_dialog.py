"""Question-related UI components for the Quiz Application."""

from PyQt6.QtWidgets import (QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QTextEdit, QDialogButtonBox, QComboBox,
                             QHeaderView, QAbstractItemView, QCheckBox)
from PyQt6.QtGui import QFont


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