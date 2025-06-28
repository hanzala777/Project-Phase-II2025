def get_medical_schema():
    return {
        "patient": {
            "patient_id": {"type": "int", "primary_key": True},
            "name": {"type": "string"},
            "dob": {"type": "date"},
            "gender": {"type": "string"},
            "contact": {"type": "string"},
            "sample_data": [
                {"patient_id": 1, "name": "Alice Smith", "dob": "1990-05-14", "gender": "F", "contact": "916-555-1234"},
                {"patient_id": 2, "name": "Bob Johnson", "dob": "1985-09-23", "gender": "M", "contact": "993-555-5678"},
            ]
        },
        "doctor": {
            "doctor_id": {"type": "int", "primary_key": True},
            "name": {"type": "string"},
            "specialization": {"type": "string"},
            "department_id": {"type": "int"},
            "sample_data": [
                {"doctor_id": 1, "name": "Dr. Taylor", "specialization": "Cardiology"},
                {"doctor_id": 2, "name": "Dr. Patel", "specialization": "Neurology"},
            ]
        },
        "appointment": {
            "appointment_id": {"type": "int", "primary_key": True},
            "patient_id": {"type": "int", "foreign_key": "patient.patient_id"},
            "doctor_id": {"type": "int", "foreign_key": "doctor.doctor_id"},
            "appointment_date": {"type": "date"},
            "reason": {"type": "string"},
            "sample_data": [
                {"appointment_id": 1001, "patient_id": 1, "doctor_id": 1, "appointment_date": "2024-07-01", "reason": "Checkup"},
                {"appointment_id": 1002, "patient_id": 2, "doctor_id": 2, "appointment_date": "2024-07-02", "reason": "Headache"},
            ]
        },
        "prescription": {
            "prescription_id": {"type": "int", "primary_key": True},
            "appointment_id": {"type": "int", "foreign_key": "appointment.appointment_id"},
            "notes": {"type": "string"},
            "sample_data": [
                {"prescription_id": 2001, "appointment_id": 1001, "notes": "Take rest"},
                {"prescription_id": 2002, "appointment_id": 1002, "notes": "MRI recommended"},
            ]
        },
        "medication": {
            "medication_id": {"type": "int", "primary_key": True},
            "prescription_id": {"type": "int", "foreign_key": "prescription.prescription_id"},
            "medicine_name": {"type": "string"},
            "dosage": {"type": "string"},
            "duration": {"type": "string"},
            "sample_data": [
                {"medication_id": 3001, "prescription_id": 2001, "medicine_name": "Paracetamol", "dosage": "500mg", "duration": "5 days"},
                {"medication_id": 3002, "prescription_id": 2002, "medicine_name": "Ibuprofen", "dosage": "200mg", "duration": "3 days"},
            ]
        }
    }

def validate_schema(schema):
    # Map schema types to Python types
    type_mapping = {
        "string": str,
        "int": int,
        "float": float,
        "date": str,  # Dates are usually strings in sample data unless parsed
    }

    for table_name, table_def in schema.items():
        sample_data = table_def.get("sample_data", [])
        columns = {
            col: col_def for col, col_def in table_def.items()
            if isinstance(col_def, dict) and "type" in col_def
        }

        # Validate each row in sample_data
        for row in sample_data:
            # Check that all required keys exist
            for col_name, col_def in columns.items():
                if col_name not in row:
                    raise ValueError(f"Missing column '{col_name}' in table '{table_name}' sample_data.")
                expected_type = type_mapping.get(col_def["type"])
                if expected_type and not isinstance(row[col_name], expected_type):
                    raise ValueError(
                        f"Invalid type for column '{col_name}' in table '{table_name}'. "
                        f"Expected {col_def['type']}, got {type(row[col_name]).__name__}."
                    )

            # Check for unexpected keys
            for key in row.keys():
                if key not in columns:
                    raise ValueError(f"Unexpected column '{key}' in table '{table_name}' sample_data.")

        # Check for duplicate primary keys
        primary_keys = [col for col, col_def in columns.items() if col_def.get("primary_key")]
        if primary_keys:
            seen_keys = set()
            for row in sample_data:
                pk_values = tuple(row[pk] for pk in primary_keys)
                if pk_values in seen_keys:
                    raise ValueError(f"Duplicate primary key {pk_values} in table '{table_name}'.")
                seen_keys.add(pk_values)

        # Check for foreign key validity
        for col, col_def in columns.items():
            if "foreign_key" in col_def:
                ref_table, ref_col = col_def["foreign_key"].split(".")
                ref_table_data = schema.get(ref_table, {}).get("sample_data", [])
                ref_values = {row[ref_col] for row in ref_table_data}
                for row in sample_data:
                    if row[col] not in ref_values:
                        raise ValueError(
                            f"Foreign key constraint violation in table '{table_name}', column '{col}'. "
                            f"Value '{row[col]}' not found in '{ref_table}.{ref_col}'."
                        )
    return True


def test_schema():
    schema = get_medical_schema()
    try:
        if validate_schema(schema):
            print("✅ Schema validation passed.")
    except ValueError as e:
        print(f"❌ Schema validation failed: {e}")


if __name__ == "__main__":
    test_schema()