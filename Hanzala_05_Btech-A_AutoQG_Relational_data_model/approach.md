# Auto-Question Generator for Relational Data Model

## **1. Introduction**
An auto-question generator for **Relational Data Model** dynamically generates database-related questions, helping learners understand core database concepts. The system ensures that every generated question is unique by using randomized elements.

## **2. Concepts Covered**
This generator focuses on:

### **Relational Data Model:**
- **Relational Schema**: Understanding table structures and relationships.
- **Domain Constraints**: Ensuring column values belong to a specific domain.
- **Key Constraints**: Enforcing uniqueness constraints on attributes.
- **Candidate Keys and Primary Key**: Understanding unique identifiers in tables.
- **Integrity Constraints**: Enforcing database consistency rules.
- **Entity Integrity and NOT NULL Constraints**: Ensuring valid records.
- **Foreign Key**: Establishing relationships between tables.
- **Referential Integrity Constraint**: Maintaining consistent references.
- **Assertion Constraints**: Enforcing complex constraints on data.


Each type of question is generated dynamically to ensure variety in learning.

## **3. Approach to Auto-Question Generation**

### **Step 1: Identify Question Types**
Each concept can be used to create different types of questions:
- **Conceptual Questions**: Understanding relational data model rules.
- **MCQs**: Choosing the correct constraint or key type.
- **Schema-Based Questions**: Using relational schemas to formulate queries.

### **Step 2: Template based Data Generation**
To ensure dynamic question creation:
- Random table and column names are selected.
- Different constraints and keys are used based on the schema.
- Entity-relationship structures are assigned.

### **Step 3: Implementing Question Generators**
Each topic has a separate function to generate a dynamic question and its correct answer.

## **4. Example Implementations**

### **(A) Relational Schema**
#### **Generating Relational Schema Auto-Questions**
```python
import random

def generate_schema_question():
    table_name = random.choice(["students", "employees", "orders"])
    question = f"Define a relational schema for the `{table_name}` table with at least three attributes."
    answer = f"""
    CREATE TABLE {table_name} (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    );
    """
    return question, answer
```

**Example Output:**
```
Generated Question: Define a relational schema for the `students` table with at least three attributes.
Correct Answer:
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
```

### **(B) Key Constraints**
#### **Generating Key Constraints Auto-Questions**
```python
def generate_key_constraint_question():
    table = "employees"
    column = "emp_id"
    question = f"What SQL constraint ensures that `{column}` in `{table}` is unique and cannot be NULL?"
    answer = "PRIMARY KEY"
    return question, answer
```

**Example Output:**
```
Generated Question: What SQL constraint ensures that `emp_id` in `employees` is unique and cannot be NULL?
Correct Answer: PRIMARY KEY
```

### **(C) Foreign Keys & Referential Integrity**
#### **Generating Foreign Key Auto-Questions**
```python
def generate_foreign_key_question():
    table1, table2 = "orders", "customers"
    question = f"Write an SQL query to create a foreign key in `{table1}` that references `{table2}`."
    answer = f"""
    ALTER TABLE {table1} 
    ADD CONSTRAINT fk_{table2}_id 
    FOREIGN KEY (customer_id) REFERENCES {table2}(id);
    """
    return question, answer
```

**Example Output:**
```
Generated Question: Write an SQL query to create a foreign key in `orders` that references `customers`.
Correct Answer:
ALTER TABLE orders 
ADD CONSTRAINT fk_customers_id 
FOREIGN KEY (customer_id) REFERENCES customers(id);
```

### **(D) Entity-Relationship (ER) Diagrams to Relational Schemas**
#### **Generating ER to Schema Auto-Questions**
```python
def generate_er_schema_question():
    entity = "students"
    relationship = "enrolled"
    question = f"Translate the ER diagram of `{entity}` and `{relationship}` into a relational schema."
    answer = f"""
    CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(255)
    );

    CREATE TABLE enrolled (
        student_id INT,
        course_id INT,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    """
    return question, answer
```

**Example Output:**
```
Generated Question: Translate the ER diagram of `students` and `enrolled` into a relational schema.
Correct Answer:
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE enrolled (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

## **5. Conclusion**
This auto-question generator dynamically creates relational model and data modeling questions, ensuring a varied and engaging learning experience. By leveraging **randomized query generation**, it provides a scalable approach to SQL learning. Future work includes **enhancing complexity levels and interactive query execution**.
