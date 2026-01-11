-- Initialize the Quiz Database Schema

-- Create subjects table
CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create questions table
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    subject_id INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) NOT NULL CHECK (question_type IN ('multiple_choice', 'multi_select')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create options table (for answer choices)
CREATE TABLE IF NOT EXISTS options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    option_key VARCHAR(10) NOT NULL,
    option_text TEXT NOT NULL,
    UNIQUE(question_id, option_key)
);

-- Create correct_answers table (supports multiple correct answers)
CREATE TABLE IF NOT EXISTS correct_answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
    answer_key VARCHAR(10) NOT NULL,
    UNIQUE(question_id, answer_key)
);

-- Create indexes for better performance
CREATE INDEX idx_questions_subject_id ON questions(subject_id);
CREATE INDEX idx_options_question_id ON options(question_id);
CREATE INDEX idx_correct_answers_question_id ON correct_answers(question_id);

-- Optional: Create a view for easier querying
CREATE OR REPLACE VIEW quiz_view AS
SELECT 
    q.id,
    q.subject_id,
    s.name as subject_name,
    q.question_text,
    q.question_type,
    json_object_agg(o.option_key, o.option_text) as options,
    array_agg(DISTINCT ca.answer_key) as correct_answers
FROM questions q
LEFT JOIN subjects s ON q.subject_id = s.id
LEFT JOIN options o ON q.id = o.question_id
LEFT JOIN correct_answers ca ON q.id = ca.question_id
GROUP BY q.id, q.subject_id, s.name, q.question_text, q.question_type;
