"""Domain models for the Quiz Application.

This module contains the domain entities representing the core business objects
of the quiz application. These models provide a clean separation between the
database layer and the UI layer.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class QuestionType(Enum):
    """Enum representing the types of questions in a quiz."""
    MULTIPLE_CHOICE = "multiple_choice"
    MULTI_SELECT = "multi_select"


@dataclass
class Subject:
    """Represents a quiz subject/category.
    
    Attributes:
        id: Unique identifier for the subject
        name: Name of the subject
        description: Optional description of the subject
    """
    name: str
    description: str = ""
    id: Optional[int] = None
    
    def __str__(self) -> str:
        return self.name


@dataclass
class Question:
    """Represents a quiz question.
    
    Attributes:
        id: Unique identifier for the question
        subject_id: ID of the subject this question belongs to
        question_text: The text of the question
        question_type: Type of question (single or multiple correct answers)
        options: Dictionary mapping option keys (A, B, C, etc.) to option text
        correct_answers: List of correct answer keys
        subject_name: Name of the subject (optional, for display purposes)
    """
    question_text: str
    question_type: QuestionType
    options: Dict[str, str]
    correct_answers: List[str]
    subject_id: Optional[int] = None
    id: Optional[int] = None
    subject_name: Optional[str] = None
    
    def __post_init__(self):
        """Validate and normalize the question data."""
        # Convert string question type to enum if needed
        if isinstance(self.question_type, str):
            self.question_type = QuestionType(self.question_type)
        
        # Ensure correct_answers is a list
        if not isinstance(self.correct_answers, list):
            self.correct_answers = [self.correct_answers]
        
        # Sort correct answers for consistency
        self.correct_answers = sorted(self.correct_answers)
    
    def is_multi_select(self) -> bool:
        """Check if this question has multiple correct answers."""
        return len(self.correct_answers) > 1
    
    def is_answer_correct(self, user_answer: List[str]) -> bool:
        """Check if the user's answer is correct.
        
        Args:
            user_answer: List of answer keys selected by the user
            
        Returns:
            True if the answer is correct, False otherwise
        """
        if not user_answer:
            return False
        return sorted(set(user_answer)) == sorted(set(self.correct_answers))
    
    def get_truncated_text(self, max_length: int = 100) -> str:
        """Get a truncated version of the question text.
        
        Args:
            max_length: Maximum length of the text
            
        Returns:
            Truncated question text with ellipsis if needed
        """
        if len(self.question_text) <= max_length:
            return self.question_text
        return self.question_text[:max_length - 3] + "..."
    
    @classmethod
    def from_db_dict(cls, data: Dict) -> 'Question':
        """Create a Question instance from database dictionary.
        
        Args:
            data: Dictionary containing question data from database
            
        Returns:
            Question instance
        """
        return cls(
            id=data.get('id'),
            subject_id=data.get('subject_id'),
            subject_name=data.get('subject_name'),
            question_text=data['question_text'],
            question_type=QuestionType(data['question_type']),
            options=data['options'],
            correct_answers=data.get('correct_answers', data.get('correct_answer', []))
        )
    
    def to_db_dict(self) -> Dict:
        """Convert Question instance to database dictionary format.
        
        Returns:
            Dictionary suitable for database operations
        """
        return {
            'id': self.id,
            'subject_id': self.subject_id,
            'question_text': self.question_text,
            'question_type': self.question_type.value,
            'options': self.options,
            'correct_answers': self.correct_answers
        }


@dataclass
class QuizSession:
    """Represents an active quiz session.
    
    Attributes:
        subject: The subject of this quiz
        questions: List of questions in this quiz
        current_question_index: Index of the current question (0-based)
        user_answers: List of user's answers for each question
        score: Current score
    """
    subject: Subject
    questions: List[Question]
    current_question_index: int = 0
    user_answers: List[Optional[List[str]]] = field(default_factory=list)
    score: int = 0
    
    def __post_init__(self):
        """Initialize user answers list if not provided."""
        if not self.user_answers:
            self.user_answers = [None] * len(self.questions)
    
    def get_current_question(self) -> Optional[Question]:
        """Get the current question.
        
        Returns:
            Current question or None if index is out of bounds
        """
        if 0 <= self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    
    def save_answer(self, answer: List[str]) -> None:
        """Save the user's answer for the current question.
        
        Args:
            answer: List of selected answer keys
        """
        if 0 <= self.current_question_index < len(self.questions):
            self.user_answers[self.current_question_index] = sorted(answer) if answer else None
    
    def next_question(self) -> bool:
        """Move to the next question.
        
        Returns:
            True if moved successfully, False if already at last question
        """
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return True
        return False
    
    def previous_question(self) -> bool:
        """Move to the previous question.
        
        Returns:
            True if moved successfully, False if already at first question
        """
        if self.current_question_index > 0:
            self.current_question_index -= 1
            return True
        return False
    
    def is_last_question(self) -> bool:
        """Check if currently on the last question."""
        return self.current_question_index == len(self.questions) - 1
    
    def is_first_question(self) -> bool:
        """Check if currently on the first question."""
        return self.current_question_index == 0
    
    def get_unanswered_questions(self) -> List[int]:
        """Get list of unanswered question numbers (1-based).
        
        Returns:
            List of question numbers that haven't been answered
        """
        return [i + 1 for i, answer in enumerate(self.user_answers) if answer is None]
    
    def calculate_score(self) -> int:
        """Calculate the total score for the quiz.
        
        Returns:
            Number of correctly answered questions
        """
        self.score = 0
        for i, question in enumerate(self.questions):
            user_answer = self.user_answers[i] if self.user_answers[i] else []
            if question.is_answer_correct(user_answer):
                self.score += 1
        return self.score
    
    def get_percentage(self) -> float:
        """Get the percentage score.
        
        Returns:
            Percentage score (0.0 to 100.0)
        """
        if not self.questions:
            return 0.0
        return (self.score / len(self.questions)) * 100
    
    def get_performance_rating(self) -> str:
        """Get a performance rating based on the score.
        
        Returns:
            Performance rating string
        """
        percentage = self.get_percentage()
        if percentage >= 90:
            return "Excellent work! 🌟"
        elif percentage >= 70:
            return "Good job! 👍"
        elif percentage >= 50:
            return "Not bad! Keep practicing! 📚"
        else:
            return "Keep studying! You can do better! 💪"
    
    def get_progress_percentage(self) -> float:
        """Get the current progress through the quiz as a percentage.
        
        Returns:
            Progress percentage (0.0 to 100.0)
        """
        if not self.questions:
            return 0.0
        return (self.current_question_index / len(self.questions)) * 100


@dataclass
class QuizResult:
    """Represents the result of a completed quiz.
    
    Attributes:
        subject: The subject of the quiz
        total_questions: Total number of questions
        correct_answers: Number of correct answers
        percentage: Percentage score
        performance_rating: Performance rating text
        question_results: List of tuples (question, user_answer, is_correct)
    """
    subject: Subject
    total_questions: int
    correct_answers: int
    percentage: float
    performance_rating: str
    question_results: List[tuple] = field(default_factory=list)
    
    def __str__(self) -> str:
        return (f"Quiz Results - {self.subject.name}\n"
                f"Score: {self.correct_answers}/{self.total_questions} "
                f"({self.percentage:.1f}%)\n"
                f"{self.performance_rating}")
