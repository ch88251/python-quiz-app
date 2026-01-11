# Python Quiz App

A comprehensive quiz application with both Command-Line Interface (CLI) and Graphical User Interface (GUI) versions using PyQt6.

## Features

- 📚 Multiple-choice questions from a JSON database
- ✅ Support for single and multi-select questions
- 🔀 Random question shuffling for each quiz session
- 📊 Score tracking and performance feedback
- 🎨 Modern graphical interface (GUI version)
- 💻 Traditional command-line interface (CLI version)

### GUI-Specific Features

- **Modern User Interface**: Clean and intuitive design with PyQt6
- **Progress Tracking**: Visual progress bar showing quiz completion
- **Navigation**: Move forward and backward through questions
- **Answer Review**: Review all answers after completing the quiz with color-coded feedback
- **Restart Capability**: Retake the quiz with newly shuffled questions
- **Multi-select Support**: Checkboxes for multi-answer questions, radio buttons for single-answer questions

## Installation

### Prerequisites

- Python 3.8 or higher

### Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- PyQt6 (for the GUI version)

## Usage

### GUI Version (Recommended)

Run the graphical interface:

```bash
python quiz_gui.py
```

#### GUI Features:

1. **Question Display**: Each question is clearly displayed with its number and total count
2. **Answer Selection**: 
   - Radio buttons for single-choice questions
   - Checkboxes for multi-choice questions
3. **Navigation**:
   - Use "Next" and "Previous" buttons to navigate between questions
   - Your answers are automatically saved when you navigate
4. **Submit**: Click "Submit Quiz" on the last question
5. **Results**: View your score with performance feedback
6. **Review**: Option to review all answers with correct/incorrect indicators
7. **Restart**: Take the quiz again with shuffled questions

### CLI Version

Run the command-line interface:

```bash
python quiz.py
```

#### CLI Features:

1. Questions are presented one at a time
2. Enter your answer (e.g., 'A', 'B', 'C', or 'D')
3. For multi-select questions, enter comma-separated answers (e.g., 'A,C,D')
4. Immediate feedback after each question
5. Final score displayed at the end

## Quiz Format

The quiz questions are stored in `quiz.json` with the following format:

```json
{
  "quiz": [
    {
      "question": "Question text here?",
      "type": "multiple_choice",
      "options": {
        "A": "First option",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
      },
      "correct_answer": ["A"]
    }
  ]
}
```

### Multi-Select Questions

For questions with multiple correct answers, use an array:

```json
"correct_answer": ["A", "C", "E"]
```

## Screenshots

### GUI Version

The GUI provides:
- A clean, modern interface
- Progress bar showing quiz completion
- Easy navigation between questions
- Visual feedback for correct/incorrect answers during review
- Responsive design that works on different screen sizes

## File Structure

```
python-quiz-app/
├── quiz.py           # CLI version of the quiz
├── quiz_gui.py       # GUI version of the quiz (PyQt6)
├── quiz.json         # Quiz questions database
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── .gitignore       # Git ignore file
```

## Development

### Adding New Questions

Edit `quiz.json` to add new questions following the format shown above.

### Customization

#### GUI Styling

The GUI uses PyQt6 stylesheets which can be customized in the `init_ui()` method of the `QuizApp` class in `quiz_gui.py`.

#### CLI Behavior

Modify `quiz.py` to change how questions are displayed or how answers are validated in the command-line version.

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues and enhancement requests!
