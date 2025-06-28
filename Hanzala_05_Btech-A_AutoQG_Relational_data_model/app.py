import json

with open("schemas.json", "r") as f:
    schemas = json.load(f)

# Embedded Q&A templates (your full provided data)
qna_templates = {
    "Relational Schema": {
        "easy": [
            "What is the primary key in the table {table_name}?",
            "List the columns in table {table_name}.",
            "Is there a foreign key in the table {table_name}?",
            "Which column can be used as an identifier in table {table_name}?",
            "What is the purpose of the table {table_name}?"
        ],
        "medium": [
            "List all columns in table {table_name} that have a UNIQUE or PRIMARY KEY constraint.",
            "Which columns in table {table_name} define relationships with other tables?",
            "What type of data is stored in column {column_name} in table {table_name}?",
            "Can you describe the structure of table {table_name}?",
            "Does table {table_name} reference any other tables through foreign keys?"
        ],
        "hard": [
            "Explain the purpose of the {column_name} column in table {table_name}.",
            "How do you design a relational schema for a system involving {table_name}?",
            "What happens if a duplicate entry is inserted in a UNIQUE column in {table_name}?",
            "Can {table_name} have two foreign keys? Justify your answer.",
            "Explain normalization based on the current schema of {table_name}."
        ]
    },
    "Domain Constraints": {
        "easy": [
            "What constraints are applied to column {column_name} in table {table_name}?",
            "Is {column_name} in table {table_name} allowed to have NULL values?",
            "What is the data type of column {column_name} in table {table_name}?",
            "Can column {column_name} in table {table_name} store negative values?",
            "Is there a default value for column {column_name} in table {table_name}?"
        ],
        "medium": [
            "What is the domain constraint on column {column_name} in table {table_name}?",
            "Which columns in table {table_name} have check constraints?",
            "What range of values are allowed in column {column_name} in table {table_name}?",
            "Does table {table_name} enforce a constraint on data format for {column_name}?",
            "How are domain constraints different from entity integrity in {table_name}?"
        ],
        "hard": [
            "How does the data type of {column_name} in table {table_name} affect storage?",
            "Explain how violating domain constraints can affect table {table_name}.",
            "How can domain constraints prevent invalid data in column {column_name}?",
            "What happens if a value outside the domain is inserted into {column_name}?",
            "Can a domain constraint depend on another column in table {table_name}?"
        ]
    },
    "Key Constraints": {
        "easy": [
            "What key constraints are defined in table {table_name}?",
            "What is a primary key in table {table_name}?",
            "Can table {table_name} have duplicate values in a key column?",
            "What happens if a duplicate value is inserted into a primary key column?",
            "How is the uniqueness of a column enforced in table {table_name}?"
        ],
        "medium": [
            "How is uniqueness enforced in table {table_name}?",
            "Does table {table_name} have any composite keys?",
            "What is the difference between primary key and unique key in table {table_name}?",
            "How is key constraint related to data retrieval in {table_name}?",
            "Is it mandatory to define a primary key for table {table_name}?"
        ],
        "hard": [
            "Can a table {table_name} have more than one candidate key? Give reasoning.",
            "How does violation of key constraints affect referential integrity?",
            "Is it possible to change the primary key of table {table_name} after creation?",
            "Explain the role of a superkey in table {table_name}.",
            "Design an alternate key for table {table_name} and explain your choice."
        ]
    },
    "Candidate Keys and Primary Key": {
        "easy": [
            "What is a candidate key in table {table_name}?",
            "What is the difference between a candidate key and primary key in {table_name}?",
            "Which columns in table {table_name} can be considered candidate keys?",
            "Can a candidate key in {table_name} contain NULL values?",
            "Is a primary key always a candidate key in {table_name}?"
        ],
        "medium": [
            "Is {column_name} a valid candidate key in table {table_name}? Why or why not?",
            "How is the primary key chosen from candidate keys in {table_name}?",
            "Can a table {table_name} have multiple candidate keys?",
            "What are the benefits of having multiple candidate keys in {table_name}?",
            "What factors influence the selection of a primary key from candidate keys?"
        ],
        "hard": [
            "Does table {table_name} have any composite primary keys?",
            "How would you handle a situation where no single column qualifies as a candidate key in {table_name}?",
            "Explain the impact of poor primary key selection on query performance in {table_name}.",
            "Design a candidate key strategy for the table {table_name} and explain.",
            "Can a foreign key reference a candidate key instead of the primary key in another table?"
        ]
    },
    "Foreign Key and Referential Integrity": {
        "easy": [
            "What are the foreign keys in table {table_name}?",
            "Which column in table {table_name} is used as a foreign key?",
            "What does a foreign key in {table_name} reference?",
            "Can a foreign key in {table_name} be NULL?",
            "Is it possible to have multiple foreign keys in table {table_name}?"
        ],
        "medium": [
            "What does the FOREIGN KEY on column {column_name} in table {table_name} reference?",
            "How is referential integrity maintained in table {table_name}?",
            "What is the purpose of foreign key in table {table_name}?",
            "How does foreign key improve data integrity in {table_name}?"
        ],
        "hard": [
            "Why is {column_name} in table {table_name} important for referential integrity?",
            "What are the different referential actions supported in table {table_name}?",
            "Can you design a table with foreign keys and explain referential integrity constraints involved?"
        ]
    },
    "NOT NULL & Entity Integrity": {
        "easy": [
            "Which columns in table {table_name} cannot be NULL?",
            "What is the purpose of the NOT NULL constraint in {table_name}?",
            "Is the primary key column of {table_name} allowed to have NULLs?",
            "Can a NOT NULL column in {table_name} be updated to NULL?",
            "What is the default behavior of columns in {table_name} regarding NULL values?"
        ],
        "medium": [
            "What is entity integrity in the context of table {table_name}?",
            "What would happen if a NULL value is inserted in {column_name} of table {table_name}?",
            "Can a foreign key column in {table_name} have NULL values?",
            "Explain how NOT NULL constraint ensures data integrity in table {table_name}.",
            "Can a composite primary key have one nullable column in table {table_name}?"
        ],
        "hard": [
            "Why is entity integrity essential in relational databases using table {table_name}?",
            "Can a table with NULL primary key values be used in foreign key relationships?",
            "Discuss a situation where NOT NULL constraint could conflict with application logic.",
            "Design a schema with strict entity integrity constraints for {table_name}.",
            "What are the alternatives to NOT NULL constraints for ensuring valid data in {table_name}?"
        ]
    },
    "Assertion Constraints": {
        "easy": [
            "What is an assertion in relational schema context?",
            "Can you give an example of an assertion for table {table_name}?",
            "Is assertion constraint defined at table or database level?",
            "Can assertions be used to enforce business rules in {table_name}?",
            "Are assertions commonly implemented in modern DBMS?"
        ],
        "medium": [
            "How can redundancy be reduced in table {table_name} using foreign keys?",
            "Is there any constraint that limits the range or length of {column_name} in table {table_name}?",
            "Can assertion constraints compare values across multiple tables?",
            "How do assertion constraints improve data quality in relational schema?",
            "Explain how to enforce an assertion that every employee's salary is > 0."
        ],
        "hard": [
            "How are assertion constraints different from table-level constraints in {table_name}?",
            "Can assertion constraints replace triggers? Why or why not?",
            "How would you implement an assertion involving aggregates across {table_name}?",
            "Describe a complex business rule that can be enforced using assertions on {table_name}.",
            "Why are assertion constraints rarely implemented directly in most RDBMS systems?"
        ]
    }
}



def generate_answer(question_text, table_name=None, column_name=None):
    q = question_text.lower()

    if "primary key" in q:
        return f"The primary key in the {table_name} table is the column with the PRIMARY KEY constraint."
    elif "foreign key" in q:
        return f"A foreign key in the {table_name} table is a column that refers to a primary key in another table."
    elif "columns" in q and "list" in q:
        return f"The columns in the {table_name} table are: {', '.join(column_name)}."
    elif "null" in q:
        return f"The column {column_name} in the {table_name} table has a NOT NULL constraint, so it must have a value."
    elif "data type" in q:
        return f"The data type of column {column_name} in the {table_name} table is defined according to the schema."
    elif "domain constraint" in q or "check constraint" in q:
        return f"The domain constraints define what kind of values column {column_name} in {table_name} can store."
    elif "unique" in q or "candidate key" in q:
        return f"A candidate key is a column or combination of columns in {table_name} that can uniquely identify rows."
    elif "assertion" in q:
        return f"Assertions are conditions that must hold true for data in {table_name} across the whole database."
    elif "entity integrity" in q:
        return f"Entity integrity means the primary key in {table_name} cannot have NULL values."
    elif "referential integrity" in q:
        return f"Referential integrity ensures that foreign keys in {table_name} match primary keys in the referenced tables."
    elif "normalization" in q:
        return f"Normalization reduces data redundancy and improves integrity in {table_name}."
    elif "design" in q:
        return f"Designing {table_name} involves identifying fields, keys, and relationships."
    elif "identifier" in q:
        return f"In {table_name}, a column with PRIMARY KEY or UNIQUE constraint is typically used as an identifier."
    elif "negative value" in q:
        return f"Whether {column_name} in {table_name} can store negative values depends on its domain constraint."
    elif "default" in q:
        return f"The default value for {column_name} in {table_name} is determined by schema or application logic."
    else:
        return f"This question is based on {table_name} and involves understanding its schema or constraints."

# Store all generated Q&A pairs here
all_qna = []

# Loop over each topic, difficulty level, and question
for topic, levels in qna_templates.items():
    for level, templates in levels.items():
        for db_name, tables in schemas.items():
            for table_name, table_info in tables.items():
                column_names = list(table_info["columns"].keys())

                for template in templates:
                    # Determine which placeholders are needed
                    needs_column = "{column_name}" in template
                    needs_table = "{table_name}" in template

                    # If both table and column are needed
                    if needs_table and needs_column:
                        for col in column_names:
                            try:
                                question = template.format(table_name=table_name, column_name=col)
                                answer = generate_answer(question, table_name, col)
                                all_qna.append({
                                    "topic": topic,
                                    "difficulty": level,
                                    "db_name": db_name,
                                    "question": question,
                                    "answer": answer
                                })
                            except Exception as e:
                                print(f"Error formatting question: {template} -> {e}")
                                continue

                    # If only table is needed
                    elif needs_table:
                        try:
                            question = template.format(table_name=table_name)
                            answer = generate_answer(question, table_name, column_names)
                            all_qna.append({
                                "topic": topic,
                                "difficulty": level,
                                "db_name": db_name,
                                "question": question,
                                "answer": answer
                            })
                        except Exception as e:
                            print(f"Error formatting question: {template} -> {e}")
                            continue

                    # If only column is needed
                    elif needs_column:
                        for col in column_names:
                            try:
                                question = template.format(column_name=col)
                                answer = generate_answer(question, table_name, col)
                                all_qna.append({
                                    "topic": topic,
                                    "difficulty": level,
                                    "db_name": db_name,
                                    "question": question,
                                    "answer": answer
                                })
                            except Exception as e:
                                print(f"Error formatting question: {template} -> {e}")
                                continue

# Save the full dataset
output_path = "relational_model_full_qna.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_qna, f, indent=4, ensure_ascii=False)

print("Q&A generation complete. Saved to:", output_path)