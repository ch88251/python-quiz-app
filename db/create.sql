-- Drop tables if they exist to start fresh
DROP TABLE IF EXISTS options;
DROP TABLE IF EXISTS questions;

-- Create the 'questions' table with sequence starting at 1
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    question_type VARCHAR(20) CHECK (question_type IN ('true_false', 'multiple_choice')),
    correct_answer VARCHAR(10) NOT NULL
);

-- Ensure the sequence starts at 1
ALTER SEQUENCE questions_id_seq RESTART WITH 1;

-- Create the 'options' table
CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    option_letter CHAR(1) CHECK (option_letter IN ('A', 'B', 'C', 'D', 'E')),
    option_text TEXT NOT NULL
);
