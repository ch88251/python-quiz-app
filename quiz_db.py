"""
Database module for Quiz App - PostgreSQL backend
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import random


class QuizDatabase:
    """Handle all database operations for the quiz application."""
    
    def __init__(self, host="localhost", port=5432, database="quiz_db", 
                 user="quiz_user", password="quiz_password"):
        """Initialize database connection parameters."""
        self.connection_params = {
            "host": host,
            "port": port,
            "database": database,
            "user": user,
            "password": password
        }
        self.conn = None
    
    def connect(self):
        """Establish connection to the database."""
        try:
            self.conn = psycopg2.connect(**self.connection_params)
            return True
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            return False
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def get_all_subjects(self):
        """
        Retrieve all subjects from the database.
        
        Returns:
            List of subject dictionaries with id, name, and description
        """
        if not self.conn:
            if not self.connect():
                return []
        
        try:
            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT id, name, description
                FROM subjects
                ORDER BY name
            """)
            
            subjects = cursor.fetchall()
            cursor.close()
            return [dict(s) for s in subjects]
            
        except psycopg2.Error as e:
            print(f"Database query error: {e}")
            return []
    
    def get_questions_by_subject(self, subject_id, shuffle=True):
        """
        Retrieve quiz questions for a specific subject.
        
        Args:
            subject_id: The ID of the subject to filter by
            shuffle: Whether to randomize the order of questions
        
        Returns:
            List of question dictionaries in the same format as JSON
        """
        if not self.conn:
            if not self.connect():
                return []
        
        try:
            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            
            # Get questions for the specific subject
            cursor.execute("""
                SELECT id, question_text, question_type
                FROM questions
                WHERE subject_id = %s
                ORDER BY id
            """, (subject_id,))
            
            questions = cursor.fetchall()
            quiz_data = []
            
            for question in questions:
                question_id = question['id']
                
                # Get options for this question
                cursor.execute("""
                    SELECT option_key, option_text
                    FROM options
                    WHERE question_id = %s
                    ORDER BY option_key
                """, (question_id,))
                
                options = {row['option_key']: row['option_text'] 
                          for row in cursor.fetchall()}
                
                # Get correct answers for this question
                cursor.execute("""
                    SELECT answer_key
                    FROM correct_answers
                    WHERE question_id = %s
                    ORDER BY answer_key
                """, (question_id,))
                
                correct_answers = [row['answer_key'] for row in cursor.fetchall()]
                
                # Build question dict in same format as JSON
                quiz_data.append({
                    "question": question['question_text'],
                    "type": question['question_type'],
                    "options": options,
                    "correct_answer": correct_answers
                })
            
            cursor.close()
            
            # Shuffle if requested
            if shuffle:
                random.shuffle(quiz_data)
            
            return quiz_data
            
        except psycopg2.Error as e:
            print(f"Database query error: {e}")
            return []
    
    def get_question_count(self):
        """Get the total number of questions in the database."""
        if not self.conn:
            if not self.connect():
                return 0
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM questions")
            count = cursor.fetchone()[0]
            cursor.close()
            return count
        except psycopg2.Error as e:
            print(f"Database query error: {e}")
            return 0
    
    def add_question(self, subject_id, question_text, question_type, options, correct_answers):
        """
        Add a new question to the database.
        
        Args:
            subject_id: The ID of the subject this question belongs to
            question_text: The question text
            question_type: Type of question ('multiple_choice' or 'multi_select')
            options: Dictionary of options {key: text}
            correct_answers: List of correct answer keys
        
        Returns:
            question_id if successful, None otherwise
        """
        if not self.conn:
            if not self.connect():
                return None
        
        try:
            cursor = self.conn.cursor()
            
            # Insert question
            cursor.execute("""
                INSERT INTO questions (subject_id, question_text, question_type)
                VALUES (%s, %s, %s)
                RETURNING id
            """, (subject_id, question_text, question_type))
            
            question_id = cursor.fetchone()[0]
            
            # Insert options
            for key, text in options.items():
                cursor.execute("""
                    INSERT INTO options (question_id, option_key, option_text)
                    VALUES (%s, %s, %s)
                """, (question_id, key, text))
            
            # Insert correct answers
            for answer in correct_answers:
                cursor.execute("""
                    INSERT INTO correct_answers (question_id, answer_key)
                    VALUES (%s, %s)
                """, (question_id, answer))
            
            self.conn.commit()
            cursor.close()
            
            return question_id
            
        except psycopg2.Error as e:
            print(f"Database insert error: {e}")
            self.conn.rollback()
            return None
    
    def delete_question(self, question_id):
        """Delete a question and its related data from the database."""
        if not self.conn:
            if not self.connect():
                return False
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM questions WHERE id = %s", (question_id,))
            self.conn.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"Database delete error: {e}")
            self.conn.rollback()
            return False
    
    def add_subject(self, name, description=""):
        """
        Add a new subject to the database.
        
        Args:
            name: The name of the subject
            description: Optional description of the subject
        
        Returns:
            subject_id if successful, None otherwise
        """
        if not self.conn:
            if not self.connect():
                return None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO subjects (name, description)
                VALUES (%s, %s)
                RETURNING id
            """, (name, description))
            
            subject_id = cursor.fetchone()[0]
            self.conn.commit()
            cursor.close()
            
            return subject_id
            
        except psycopg2.Error as e:
            print(f"Database insert error: {e}")
            self.conn.rollback()
            return None
    
    def update_subject(self, subject_id, name, description=""):
        """
        Update an existing subject.
        
        Args:
            subject_id: The ID of the subject to update
            name: The new name of the subject
            description: The new description of the subject
        
        Returns:
            True if successful, False otherwise
        """
        if not self.conn:
            if not self.connect():
                return False
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE subjects
                SET name = %s, description = %s
                WHERE id = %s
            """, (name, description, subject_id))
            
            self.conn.commit()
            cursor.close()
            return True
            
        except psycopg2.Error as e:
            print(f"Database update error: {e}")
            self.conn.rollback()
            return False
    
    def delete_subject(self, subject_id):
        """
        Delete a subject and all associated questions (cascade).
        
        Args:
            subject_id: The ID of the subject to delete
        
        Returns:
            True if successful, False otherwise
        """
        if not self.conn:
            if not self.connect():
                return False
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM subjects WHERE id = %s", (subject_id,))
            self.conn.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            print(f"Database delete error: {e}")
            self.conn.rollback()
            return False
    
    def get_question_by_id(self, question_id):
        """
        Retrieve a single question with all its details.
        
        Args:
            question_id: The ID of the question to retrieve
        
        Returns:
            Dictionary with question details or None if not found
        """
        if not self.conn:
            if not self.connect():
                return None
        
        try:
            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            
            # Get question details
            cursor.execute("""
                SELECT id, subject_id, question_text, question_type
                FROM questions
                WHERE id = %s
            """, (question_id,))
            
            question = cursor.fetchone()
            if not question:
                cursor.close()
                return None
            
            question = dict(question)
            
            # Get options
            cursor.execute("""
                SELECT option_key, option_text
                FROM options
                WHERE question_id = %s
                ORDER BY option_key
            """, (question_id,))
            
            question['options'] = {row['option_key']: row['option_text'] 
                                  for row in cursor.fetchall()}
            
            # Get correct answers
            cursor.execute("""
                SELECT answer_key
                FROM correct_answers
                WHERE question_id = %s
                ORDER BY answer_key
            """, (question_id,))
            
            question['correct_answers'] = [row['answer_key'] for row in cursor.fetchall()]
            
            cursor.close()
            return question
            
        except psycopg2.Error as e:
            print(f"Database query error: {e}")
            return None
    
    def update_question(self, question_id, subject_id, question_text, question_type, options, correct_answers):
        """
        Update an existing question and its options/answers.
        
        Args:
            question_id: The ID of the question to update
            subject_id: The ID of the subject this question belongs to
            question_text: The updated question text
            question_type: Type of question ('multiple_choice' or 'multi_select')
            options: Dictionary of options {key: text}
            correct_answers: List of correct answer keys
        
        Returns:
            True if successful, False otherwise
        """
        if not self.conn:
            if not self.connect():
                return False
        
        try:
            cursor = self.conn.cursor()
            
            # Update question
            cursor.execute("""
                UPDATE questions
                SET subject_id = %s, question_text = %s, question_type = %s
                WHERE id = %s
            """, (subject_id, question_text, question_type, question_id))
            
            # Delete existing options and answers
            cursor.execute("DELETE FROM options WHERE question_id = %s", (question_id,))
            cursor.execute("DELETE FROM correct_answers WHERE question_id = %s", (question_id,))
            
            # Insert new options
            for key, text in options.items():
                cursor.execute("""
                    INSERT INTO options (question_id, option_key, option_text)
                    VALUES (%s, %s, %s)
                """, (question_id, key, text))
            
            # Insert new correct answers
            for answer in correct_answers:
                cursor.execute("""
                    INSERT INTO correct_answers (question_id, answer_key)
                    VALUES (%s, %s)
                """, (question_id, answer))
            
            self.conn.commit()
            cursor.close()
            
            return True
            
        except psycopg2.Error as e:
            print(f"Database update error: {e}")
            self.conn.rollback()
            return False
    
    def get_all_questions(self):
        """
        Retrieve all questions with their subject information.
        
        Returns:
            List of question dictionaries with subject details
        """
        if not self.conn:
            if not self.connect():
                return []
        
        try:
            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT q.id, q.subject_id, s.name as subject_name, 
                       q.question_text, q.question_type
                FROM questions q
                JOIN subjects s ON q.subject_id = s.id
                ORDER BY s.name, q.id
            """)
            
            questions = cursor.fetchall()
            cursor.close()
            return [dict(q) for q in questions]
            
        except psycopg2.Error as e:
            print(f"Database query error: {e}")
            return []
