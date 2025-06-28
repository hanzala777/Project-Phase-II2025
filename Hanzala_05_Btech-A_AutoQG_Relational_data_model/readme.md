---
title: "Relational Data Model - Summary"
author: ["MD Arsalan Khan", "MD Jawad Aaquib", "Hanzala Ahmad"]
institute: "MGM's College of Engineering, Nanded"
advisor: "Mr. Shivparasad Titre"
format: html
---

# Topic Introduction: Relational Data Model

The Relational Data Model is a foundational concept in database systems, organizing data into tables (relations) composed of rows and columns. This model underpins SQL and is critical for understanding data storage, retrieval, and integrity.



## Domain Understanding (Criteria 1)

Understanding how database schemas, keys, and constraints ensure data consistency and integrity across levels of complexity.

### Foundational Concepts
These are the basic building blocks of the relational data model, crucial for beginners.

- **Relational Schema**: Structure of tables and how they relate.
- **Domain Constraints**: Ensuring values in a column belong to a specific type or range.
- **Key Constraints**: Uniqueness of values for identification (e.g., no duplicate primary keys).

### Intermediate Concepts
Build upon the basics and introduce relationships and data integrity enforcement.

- **Candidate Keys and Primary Key**: Understanding all possible unique identifiers, and selecting one as the primary.
- **Entity Integrity & NOT NULL Constraint**: Ensures that primary keys are never left undefined (null).
- **Foreign Key**: Used to create a link between two tables.

### Complex Concepts
Require a deeper understanding of multiple concepts working together.

- **Referential Integrity Constraint**: Ensures foreign keys in a table correctly refer to valid rows in another table.
- **Integrity Constraints**: General rules that enforce database consistency.
- **Assertion Constraints**: Custom-defined complex rules across multiple relations.

---

## Topic Question Mapping (Criteria 2)

Questions are categorized by difficulty and topic, ranging from definitions to application-based scenarios.

Each question is linked to a DBMS topic and difficulty level

**Easy**: Definitions (e.g., "What is a primary key?")

**Medium**: Conceptual understanding (e.g., "Why is referential integrity needed?")

**Hard**: Application-based (e.g., "Given this schema, identify all candidate keys.").

```python
DATABASES = [
    "space_research_db",
    "hospital_db",
    "farming_db",
    "company_db",
    "retail_db",
    "college_db"
]
TOPICS = [
    "Relational Schema",
    "Domain Constraints",
    "Key Constraints",
    "Candidate Keys and Primary Key",
    "Foreign Key and Referential Integrity",
    "NOT NULL & Entity Integrity",
    "Assertion Constraints"
]
```

```python
TRUE OR FALSE Template Example
{
    "topic": "Relational Schema",
    "difficulty": "easy",
    "db_name": "{database}",
    "question": "Tables like '{table}' in '{database}' are essential components of a relational schema.",
    "answer": true
}
```
```python
MCQs Template Example
{
    "topic": "NOT NULL & Entity Integrity",
    "difficulty": "easy",
    "db_name": "{database}",
    "question": "How does the NOT NULL constraint on '{column}' in '{table}' of '{database}' support entity integrity?",
    "options": [
        "By disallowing missing essential data in the primary key",
        "By linking databases",
        "By sorting rows",
        "By setting auto-increment"
    ],
    "answer": "By disallowing missing essential data in the primary key"
}
```
```python
Text-Based Template Example
{
    "topic": "NOT NULL & Entity Integrity",
    "difficulty": "hard",
    "db_name": "{database}",
    "question": "What does entity integrity ensure for the primary key in the '{table}' table of '{database}'?",
    "answer": "Entity integrity ensures that the primary key in the '{table}' table cannot contain NULL values."
}
```

---

## Algorithm Design (Criteria 3)

A template-driven algorithm parses schema and fills predefined question formats using schema metadata.

- The algorithm supports parameterization for generating a variety of questions.  

- It uses a **template-driven approach** to ensure consistent and structured question formats.  

- It **parses the selected database schema** to extract metadata such as table names, attributes, and constraints.  

- It **matches metadata with predefined templates** that define how questions are phrased. 

- It **fills placeholders in the templates** with actual schema elements like table names, column names, and constraints.  



###  Pseudocode

#### 1. Load Required Files
```python
- Load database schemas from `schemas.json`.
```


#### 2. Display Question Type Options
```python
- Prompt user to choose the type of questions:
  - `1 → MCQs`
  - `2 → True/False`
  - `3 → Text-Based`
- Based on the choice, load the corresponding dataset:
  - `relational_model_mcqs.json`
  - `relational_model_TF.json`
  - `relational_model_full_qna.json`
```


#### 3. Select Topic
```python
- Display a numbered list of relational model topics.
- Prompt the user to select a topic.
```


#### 4. Select Difficulty
```python
- Ask the user to choose a difficulty level:
  - `1 → Easy`
  - `2 → Medium`
  - `3 → Hard`
```

#### 5. Select Database
```python
- Show a list of available databases (e.g., `college_db`, `hospital_db`, `retail_db`, etc.).
- Prompt the user to select one.
```


#### 6. Choose Number of Questions
```python
- Ask the user how many questions they want to attempt (between 3 and 10).
```


#### 7. Filter Questions
```python
- From the loaded dataset, filter the questions using:
  - Selected topic
  - Selected difficulty
  - Selected database
```


#### 8. Display Selected Questions
```python
- For each selected question:
  - Print the question.
  - If question type is `MCQ`, show multiple choice options (A, B, C, D...).
  - If question type is `True/False`, show `True` and `False` options.
```


#### 9. Display Related Schema
```python
- Display schema for the selected database:
  - Table names
  - Column names with data types
  - Any constraints associated with the columns
```


#### 10. Launch ER Diagram
```python
- Check if an ER diagram file exists for the selected database (e.g., `college_db_er.py`).
  - If exists:
    - Run the file using `streamlit`.
    - Wait for the user to finish viewing the diagram.
  - If not:
    - Display a message saying the ER diagram is not available.
```


#### 11. Ask to Show Answers
```python
- Prompt the user: "Do you want to see the answers?"
  - If yes → Display the correct answers to the selected questions.
  - If no → Exit the program politely.
```

---

## Template Development (Criteria 4)

Each subtopic has flexible templates with placeholders to match schema and difficulty.
1.**MCQ**: "Which of the following is not a candidate key?"

2.**Template Based**: "Explain how referential integrity is maintained.“ Templates designed with placeholders to match schema and difficulty.

3.**True Or False**

### Question Types

| Type              | Use Case                                 | Design Notes                  |
|-------------------|------------------------------------------|-------------------------------|
| True/False (TFQ)  | Schema rules, relational properties      | Must be unambiguous           |
| MCQ               | Keys, constraints, algebra operators     | Use plausible distractors     |
| Text Based        | Based on templates                       | Templates                     |

```python
TRUE OR FALSE Template Example
{
    "topic": "Relational Schema",
    "difficulty": "easy",
    "db_name": "{database}",
    "question": "Tables like '{table}' in '{database}' are essential components of a relational schema.",
    "answer": true
}
```
```python
MCQs Template Example
{
    "topic": "NOT NULL & Entity Integrity",
    "difficulty": "easy",
    "db_name": "{database}",
    "question": "How does the NOT NULL constraint on '{column}' in '{table}' of '{database}' support entity integrity?",
    "options": [
        "By disallowing missing essential data in the primary key",
        "By linking databases",
        "By sorting rows",
        "By setting auto-increment"
    ],
    "answer": "By disallowing missing essential data in the primary key"
}
```
```python
Text-Based Template Example
{
    "topic": "NOT NULL & Entity Integrity",
    "difficulty": "hard",
    "db_name": "{database}",
    "question": "What does entity integrity ensure for the primary key in the '{table}' table of '{database}'?",
    "answer": "Entity integrity ensures that the primary key in the '{table}' table cannot contain NULL values."
}
```
---

## Difficulty Calibration (Criteria 5)

Questions are tagged from easy to hard based on conceptual depth and schema complexity.
**Level 1 (Easy)**: Direct definitions and concept checks

**Level 2 (Medium)**: Schema-based application (e.g., find key violations)

**Level 3 (Hard)**: Combine constraints, analyze integrity across relations

| **Difficulty** | **Criteria** |
|----------------|--------------|
| **Easy** | - Focuses on basic facts and direct definitions<br>- Requires minimal or no schema navigation<br>- Answers are primarily recall-based and explicitly available in the schema |
| **Medium** | - Involves moderate reasoning and understanding of table relationships<br>- Requires interpreting column-level metadata (e.g., data types, constraints)<br>- May reference more than one attribute or concept |
| **Hard** | - Demands deep understanding of schema logic, relationships, and constraints<br>- Requires analytical or application-based thinking (e.g., candidate keys, normalization)<br>- Often may span multiple tables and rules |


#### Level 01: 

```python
level_01 = [
    {
        "question": "In a relational database, a tuple is also known as a row.",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "question": "Which of the following is a valid candidate key for a relation R(StudentID, Name, Email)?",
        "options": ["StudentID", "Name", "Email", "Name and Email"],
        "answer": "StudentID"
    },
    {
        "question": "Which term describes the number of tuples in a relation?",
        "options": ["Degree", "Cardinality", "Domain", "Attribute"],
        "answer": "Cardinality"
    }
]
```

#### Level 02:

```python
level_02 = [
    {
        "question": "Which relational algebra operation removes duplicate tuples?",
        "options": ["Projection", "Selection", "Join", "Union"],
        "answer": "Projection"
    },
    {
        "question": "Which SQL clause is used to combine rows from two or more tables based on a related column?",
        "options": ["WHERE", "GROUP BY", "JOIN", "SELECT"],
        "answer": "JOIN"
    },
    {
        "question": "What is the result of a Cartesian product between two relations with 3 and 4 tuples respectively?",
        "options": ["7", "12", "3", "4"],
        "answer": "12"
    }
]
```

#### Level 03: 

```python
level_03 = [
    {
        "question": "If A → B and B → C in a relation, which of the following is implied by transitivity?",
        "options": ["A → C", "C → A", "B → A", "A → B, B → C implies nothing"],
        "answer": "A → C"
    },
    {
        "question": "Which of the following is an example of a partial dependency?",
        "options": [
            "A → B in a relation R(A, B)",
            "AB → C and A → C in R(A, B, C)",
            "A → B and B → A",
            "A → B and B → C"
        ],
        "answer": "AB → C and A → C in R(A, B, C)"
    },
    {
        "question": "In a relation R(A, B, C), A → B and B → C. What is the closure of A?",
        "options": ["A", "AB", "ABC", "BC"],
        "answer": "ABC"
    }
]
```

---

## Evaluation of Generated Questions (Criteria 6)

Each question is evaluated on:

- **Correctness**: Accurate answers and well-formed questions
- **Schema Relevance**: Aligns with the selected database schema
- **Topic Alignment**: Properly mapped to the correct subtopic
- **Difficulty Match**: Complexity level fits the selected difficulty

The system supports automated validation and manual review during testing.

---

## Code Implementation and Functionality (Criteria 7)

The system is developed using **Python**, with clean, modular code and logical separation of components.

- Core components:
  - **File Loader**: Parses schema and question banks
  - **Filter**: Matches topic, difficulty, and DB
  - **Question Renderer**: Displays questions and options
  - **Answer Verifier**: Matches user response with correct answer
  - **Schema Displayer**: Prints schema from `schemas.json`
  - **ER Diagram Launcher**: Opens Streamlit ER viewer

All operations are performed via a **menu-driven CLI**, ensuring a smooth user experience without GUI overhead.

---

## Documentation And Github Repository (Criteria 8)

The project is fully documented with:

- `README.md`: Overview, setup, templates, architecture
- **Inline Comments**: In every Python file to explain logic
- **Pseudocode**: Embedded in documentation for algorithm clarity
- **Schema File**: `schemas.json` with structured metadata
- **Question Files**: Clearly named (`relational_model_mcqs.json`, etc.)
- **Github**: Well documented github repository

This ensures **ease of understanding**, maintainability, and extension.

---

## Innovation and Originality (Criteria 9)

This system introduces several aspects:

- **Schema-aware templated generation**: Customizes questions using real schema data
- **ER viewer**: Combines command line interaction with ER diagram's visual support
- **Difficulty-calibrated question generation**: Designed to align with academic learning progression

---

## Separation of Concerns (Criteria 10)

The project follows a clean architecture with **SoC (Separation of Concerns)**:

- `schemas.json`: Loads and parses schema files
- `relational_model_full_qna.json`: Loads and parses the text based questions
- `relational_model_TF.json`: Loads and parses the True/False questions
- `relational_model_mcqs.json`: Loads and parses Multiple Choice questions
- `app.py`: Handles filtering logic
- `main.py`: Orchestrates user flow and I/O
- `<selected_db>_er_diagram.py`: Launches ER viewer if present

Each component is self-contained, **modular**, and **reusable**.

---

## Self Rubrics Evaluation 

| Criteria No. | Criteria                              | Max Score | Self-Assigned Score | Justification                                                                 |
|--------------|----------------------------------------|-----------|----------------------|-------------------------------------------------------------------------------|
| 1            | Domain Understanding                  | 4         | 3                    | All relational concepts (keys, constraints, integrity) thoroughly covered     |
| 2            | Topic-Question Mapping                | 4         | 3                    | Clear mapping of each question to topic, DB, and difficulty level             |
| 3            | Algorithm Design                      | 4         | 3                    | Clean, template-based design with detailed pseudocode                         |
| 4            | Template Development                  | 4         | 2                    | Covers MCQs, True/False, and Text-Based formats with placeholders             |
| 5            | Difficulty Calibration                | 4         | 3                    | Questions categorized accurately into easy, medium, and hard                  |
| 6            | Evaluation of Generated Questions     | 4         | 3                    | Well-structured with schema alignment, correctness, clarity                   |
| 7            | Code Implementation & Functionality   | 4         | 3                    | Modular Python code with CLI + ER Viewer, handles all user flows              |
| 8            | Documentation                         | 4         | 3                    | Complete with README, inline comments, schema examples, and pseudocode        |
| 9            | Innovation and Originality            | 4         | 3                    | Schema-aware generation + ER diagram launcher is unique and academic-aligned  |
| 10           | Separation of Concerns                | 4         | 4                    | All modules have clear responsibility and are reusable                        |
|              | **Total**                             | **40**    | **30**               |                                                                               |
---

