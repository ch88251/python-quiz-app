# Quiz Desktop Application

A quiz application with a Graphical User Interface (GUI) using PyQt6 and PostgreSQL database backend.

## Features

- Multiple-choice questions from PostgreSQL database
- Support for single and multi-select questions
- Random question shuffling for each quiz session
- Score tracking and performance feedback
- Modern graphical interface
- PostgreSQL database backend with Docker

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
- Docker and Docker Compose

### Quick Setup

Run the automated setup script:

```bash
./setup_postgres.sh
```

This will:
1. Install Python dependencies
2. Start PostgreSQL in Docker
3. Migrate data from quiz.json to PostgreSQL
4. Verify the setup

### Manual Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start PostgreSQL container:
```bash
cd db
docker-compose up -d
cd ..
```

3. Run migration:
```bash
python migrate_to_postgres.py
```

4. Verify setup (optional):
```bash
python verify_database.py
```

## Usage

```bash
python quiz_gui.py
```

## PostgreSQL Migration

The application now uses PostgreSQL instead of JSON files. See [POSTGRES_MIGRATION.md](POSTGRES_MIGRATION.md) for detailed information about:
- Database schema
- Migration process
- Database management
- API usage
- Troubleshooting

## Quiz Format

Questions are now stored in PostgreSQL with the following schema:

- **questions** table: question text and type
- **options** table: answer choices for each question
- **correct_answers** table: correct answer keys

The original `quiz.json` format is still supported for migration purposes.

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

## Database Management

### Start/Stop PostgreSQL

```bash
cd db
docker compose up -d
docker compose down
```

### View Database Logs

```bash
cd db
docker compose logs -f
```

### Connect to Database

```bash
cd db
docker compose exec -it db psql -U quiz_user -d quiz_db
```

### View Database Tables

```bash
quiz_db=# \dt
              List of relations
 Schema |      Name       | Type  |   Owner   
--------+-----------------+-------+-----------
 public | correct_answers | table | quiz_user
 public | options         | table | quiz_user
 public | questions       | table | quiz_user
 public | subjects        | table | quiz_user
(4 rows)
```

## Database Backup and Restore

### Database Backup

```bash
docker compose exec -e PGPASSWORD=quiz_password db pg_dump -U quiz_user -d quiz_db > quiz_backup.sql
```

### Database Restore

```bash
docker compose exec -i db pg_restore -U quiz_user -d quiz_db < quiz_backup.sql
```