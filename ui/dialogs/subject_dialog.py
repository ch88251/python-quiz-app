"""Subject-related UI components for the Quiz Application."""

from PyQt6.QtWidgets import (QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, 
                             QLineEdit, QTextEdit, QDialogButtonBox, QFormLayout, 
                             QHeaderView, QAbstractItemView)
from PyQt6.QtGui import QFont


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
