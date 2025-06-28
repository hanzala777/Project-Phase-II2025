import json
import os
import subprocess
import webbrowser
import time


# Load schema file
with open("schemas.json", "r") as f:
    schemas = json.load(f)

# Constants
TOPICS = [
    "Relational Schema",
    "Domain Constraints",
    "Key Constraints",
    "Candidate Keys and Primary Key",
    "Foreign Key and Referential Integrity",
    "NOT NULL & Entity Integrity",
    "Assertion Constraints"
]

DIFFICULTY_MAP = {
    "1": "easy",
    "2": "medium",
    "3": "hard"
}

DATABASES = [
    "space_research_db",
    "hospital_db",
    "farming_db",
    "company_db",
    "retail_db",
    "college_db"
]

# Prompt user for input
print("Choose question type:")
print("1. MCQs")
print("2. True/False")
print("3. Text-Based")
qtype_input = input("Enter choice (1/2/3): ").strip()
print()

if qtype_input == "1":
    qtype = "MCQ"
    data_file = "relational_model_mcqs.json"
elif qtype_input == "2":
    qtype = "TF"
    data_file = "relational_model_TF.json"
elif qtype_input == "3":
    qtype = "Text"
    data_file = "relational_model_full_qna.json"
else:
    print("Invalid choice. Exiting.")
    exit()

# Load selected dataset
with open(data_file, "r") as f:
    data = json.load(f)

# Choose topic
print("Choose a topic:")
for i, topic in enumerate(TOPICS, 1):
    print(f"{i}. {topic}")
topic_choice = int(input("Enter topic number: "))
selected_topic = TOPICS[topic_choice - 1]
print()

# Choose difficulty
difficulty_input = input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): ")
selected_difficulty = DIFFICULTY_MAP.get(difficulty_input)
print()

# Choose database
print("Choose a database:")
for i, db in enumerate(DATABASES, 1):
    print(f"{i}. {db}")
db_choice = int(input("Enter database number: "))
selected_db = DATABASES[db_choice - 1]

print()

# Choose number of questions
num_questions = int(input("Enter number of questions (3 to 10): "))
if num_questions < 3 or num_questions > 10:
    print("Please enter a number")
    exit()

print()

# Filter datasetye
filtered_qna = [
    item for item in data
    if item["topic"] == selected_topic
    and item["difficulty"] == selected_difficulty
    and item["db_name"] == selected_db
]

if not filtered_qna:
    print("No questions found for the given selection.")
    exit()

# Select and display questions
selected_qna = filtered_qna[:num_questions]
print("\nSelected Questions:")

for idx, qna in enumerate(selected_qna, 1):
    print(f"\nQ{idx}: {qna['question']}")
    if qtype == "MCQ" and "options" in qna:
        for opt_idx, option in enumerate(qna["options"], 1):
            print(f"  {chr(64+opt_idx)}. {option}")
    elif qtype == "TF":
        print("  A. True")
        print("  B. False")

print()
# Show related schema
print("\nRefer the below schema to answer the questions:")
print(f"\n📚 Schema for database: {selected_db}")
db_schema = schemas[selected_db]

for table_name, table_info in db_schema.items():
    print(f"\n📘 Table: {table_name}")
    print("Columns:")
    for column_name, col_details in table_info["columns"].items():
        col_type = col_details["type"]
        constraints = ", ".join(col_details["constraints"]) if col_details["constraints"] else "None"
        print(f"  - {column_name}: {col_type} | Constraints: {constraints}")


er_filename = f"{selected_db}_er.py"

if os.path.exists(er_filename):
    print("\nLaunching ER Diagram for the selected database...")

    # Start Streamlit app in a new process
    proc = subprocess.Popen(["streamlit", "run", er_filename])

    # Wait a moment for the browser to open
    time.sleep(3)
    print("ER diagram opened in your browser. Please view it, then come back here.")

    # Prompt user to continue
    input("Press Enter here after you're done viewing the ER diagram...")

    # Optional: kill the ER diagram process if it's still running
    proc.terminate()
else:
    print(f"\nER diagram file '{er_filename}' not found.")



# Ask if user wants to see answers
show_answers = input("\nDo you want to see the answers? (yes/no): ").strip().lower()
if show_answers in ("yes", "y"):
    print("\nAnswers:")
    for idx, qna in enumerate(selected_qna, 1):
        print(f"A{idx}: {qna['answer']}")
else:
    print("Okay, program ended.")
