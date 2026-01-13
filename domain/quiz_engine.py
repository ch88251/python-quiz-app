"""Quiz Engine for managing quiz logic and state.

This module provides the QuizEngine class which encapsulates all the business
logic for running a quiz, managing state, and calculating results.
"""

from typing import List, Optional
from .models import Subject, Question, QuizSession, QuizResult, QuestionType


class QuizEngine:
    """Engine for managing quiz sessions and business logic.
    
    This class handles all quiz-related operations including:
    - Loading and shuffling questions
    - Managing quiz state and navigation
    - Tracking user answers
    - Calculating scores and results
    - Validating answers
    
    Attributes:
        session: The current quiz session
        db: Database connection object
    """
    
    def __init__(self, db):
        """Initialize the quiz engine.
        
        Args:
            db: Database connection object (QuizDatabase instance)
        """
        self.db = db
        self.session: Optional[QuizSession] = None
    
    def load_quiz(self, subject_id: int, subject_name: str, shuffle: bool = True) -> bool:
        """Load a new quiz for the specified subject.
        
        Args:
            subject_id: ID of the subject to load questions for
            subject_name: Name of the subject
            shuffle: Whether to shuffle the questions (default: True)
            
        Returns:
            True if quiz loaded successfully, False otherwise
        """
        try:
            # Load questions from database
            question_dicts = self.db.get_questions_by_subject(subject_id, shuffle=shuffle)
            
            if not question_dicts:
                return False
            
            # Convert database dictionaries to Question objects
            questions = []
            for q_dict in question_dicts:
                question = Question(
                    question_text=q_dict['question'],
                    question_type=QuestionType(q_dict['type']),
                    options=q_dict['options'],
                    correct_answers=q_dict['correct_answer'],
                    subject_id=subject_id
                )
                questions.append(question)
            
            # Create subject object
            subject = Subject(name=subject_name, id=subject_id)
            
            # Create new quiz session
            self.session = QuizSession(
                subject=subject,
                questions=questions
            )
            
            return True
            
        except Exception as e:
            print(f"Error loading quiz: {e}")
            return False
    
    def get_current_question(self) -> Optional[Question]:
        """Get the current question in the quiz.
        
        Returns:
            Current Question object or None if no active session
        """
        if not self.session:
            return None
        return self.session.get_current_question()
    
    def get_question_number(self) -> tuple[int, int]:
        """Get the current question number and total questions.
        
        Returns:
            Tuple of (current_number, total_questions) where current_number is 1-based
        """
        if not self.session:
            return (0, 0)
        return (self.session.current_question_index + 1, len(self.session.questions))
    
    def save_answer(self, answer: List[str]) -> None:
        """Save the user's answer for the current question.
        
        Args:
            answer: List of selected answer keys
        """
        if self.session:
            self.session.save_answer(answer)
    
    def next_question(self) -> bool:
        """Move to the next question.
        
        Returns:
            True if moved successfully, False if already at last question
        """
        if not self.session:
            return False
        return self.session.next_question()
    
    def previous_question(self) -> bool:
        """Move to the previous question.
        
        Returns:
            True if moved successfully, False if already at first question
        """
        if not self.session:
            return False
        return self.session.previous_question()
    
    def can_go_next(self) -> bool:
        """Check if can move to next question.
        
        Returns:
            True if not at last question
        """
        if not self.session:
            return False
        return not self.session.is_last_question()
    
    def can_go_previous(self) -> bool:
        """Check if can move to previous question.
        
        Returns:
            True if not at first question
        """
        if not self.session:
            return False
        return not self.session.is_first_question()
    
    def is_last_question(self) -> bool:
        """Check if currently on the last question.
        
        Returns:
            True if on last question
        """
        if not self.session:
            return False
        return self.session.is_last_question()
    
    def is_first_question(self) -> bool:
        """Check if currently on the first question.
        
        Returns:
            True if on first question
        """
        if not self.session:
            return False
        return self.session.is_first_question()
    
    def get_current_answer(self) -> Optional[List[str]]:
        """Get the user's answer for the current question.
        
        Returns:
            List of selected answer keys or None if not answered
        """
        if not self.session:
            return None
        
        idx = self.session.current_question_index
        if 0 <= idx < len(self.session.user_answers):
            return self.session.user_answers[idx]
        return None
    
    def get_unanswered_questions(self) -> List[int]:
        """Get list of unanswered question numbers.
        
        Returns:
            List of question numbers (1-based) that haven't been answered
        """
        if not self.session:
            return []
        return self.session.get_unanswered_questions()
    
    def has_unanswered_questions(self) -> bool:
        """Check if there are any unanswered questions.
        
        Returns:
            True if any questions remain unanswered
        """
        return len(self.get_unanswered_questions()) > 0
    
    def calculate_results(self) -> Optional[QuizResult]:
        """Calculate and return quiz results.
        
        Returns:
            QuizResult object with score and details, or None if no session
        """
        if not self.session:
            return None
        
        # Calculate score
        score = self.session.calculate_score()
        percentage = self.session.get_percentage()
        rating = self.session.get_performance_rating()
        
        # Build detailed results
        question_results = []
        for i, question in enumerate(self.session.questions):
            user_answer = self.session.user_answers[i] if self.session.user_answers[i] else []
            is_correct = question.is_answer_correct(user_answer)
            question_results.append((question, user_answer, is_correct))
        
        return QuizResult(
            subject=self.session.subject,
            total_questions=len(self.session.questions),
            correct_answers=score,
            percentage=percentage,
            performance_rating=rating,
            question_results=question_results
        )
    
    def get_progress_percentage(self) -> float:
        """Get the current progress through the quiz as a percentage.
        
        Returns:
            Progress percentage (0.0 to 100.0)
        """
        if not self.session:
            return 0.0
        return self.session.get_progress_percentage()
    
    def restart_quiz(self, shuffle: bool = True) -> bool:
        """Restart the current quiz with the same subject.
        
        Args:
            shuffle: Whether to shuffle the questions (default: True)
            
        Returns:
            True if restarted successfully, False otherwise
        """
        if not self.session:
            return False
        
        subject_id = self.session.subject.id
        subject_name = self.session.subject.name
        
        return self.load_quiz(subject_id, subject_name, shuffle=shuffle)
    
    def go_to_question(self, question_index: int) -> bool:
        """Navigate to a specific question by index.
        
        Args:
            question_index: 0-based index of the question to navigate to
            
        Returns:
            True if navigation successful, False otherwise
        """
        if not self.session:
            return False
        
        if 0 <= question_index < len(self.session.questions):
            self.session.current_question_index = question_index
            return True
        return False
    
    def get_question_at_index(self, index: int) -> Optional[Question]:
        """Get a question at a specific index.
        
        Args:
            index: 0-based index of the question
            
        Returns:
            Question object or None if index out of bounds
        """
        if not self.session:
            return None
        
        if 0 <= index < len(self.session.questions):
            return self.session.questions[index]
        return None
    
    def get_answer_at_index(self, index: int) -> Optional[List[str]]:
        """Get the user's answer at a specific index.
        
        Args:
            index: 0-based index of the question
            
        Returns:
            List of selected answer keys or None
        """
        if not self.session:
            return None
        
        if 0 <= index < len(self.session.user_answers):
            return self.session.user_answers[index]
        return None
    
    def is_answer_correct_at_index(self, index: int) -> bool:
        """Check if the answer at a specific index is correct.
        
        Args:
            index: 0-based index of the question
            
        Returns:
            True if answer is correct, False otherwise
        """
        question = self.get_question_at_index(index)
        answer = self.get_answer_at_index(index)
        
        if question and answer is not None:
            return question.is_answer_correct(answer)
        return False
    
    def get_total_questions(self) -> int:
        """Get the total number of questions in the current quiz.
        
        Returns:
            Number of questions or 0 if no active session
        """
        if not self.session:
            return 0
        return len(self.session.questions)
    
    def get_score(self) -> int:
        """Get the current score.
        
        Returns:
            Current score or 0 if no session
        """
        if not self.session:
            return 0
        return self.session.score
