import streamlit as st
import importlib.util
import os

# Load the medical schema
schema_file = "medical_schema.py"
spec = importlib.util.spec_from_file_location("medical_schema", schema_file)
schema_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(schema_module)
schema = schema_module.get_medical_schema()

# Mermaid ER diagram generator
def generate_mermaid_er_diagram(schema):
    lines = ["erDiagram"]
    
    # Add all table definitions
    for table_name, table_def in schema.items():
        lines.append(f"  {table_name} {{")
        for attr, info in table_def.items():
            if isinstance(info, dict) and "type" in info:
                attr_type = info.get("type", "string").lower()
                suffix = " PK" if info.get("primary_key") else ""
                lines.append(f"    {attr_type} {attr}{suffix}")
        lines.append("  }")

    # Add relationships
    for table_name, table_def in schema.items():
        for attr, info in table_def.items():
            if isinstance(info, dict) and "foreign_key" in info:
                fk = info["foreign_key"]
                if "." in fk:
                    ref_table, _ = fk.split(".")
                    lines.append(f"  {table_name} ||--o| {ref_table} : \"{attr}\"")
    
    return "\n".join(lines)

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🏥 Medical Schema Explorer")

tab1, tab2 = st.tabs(["📈 ER Diagram", "📋 Table Schemas"])

with tab1:
    st.subheader("Entity Relationship Diagram (Mermaid)")
    diagram_code = generate_mermaid_er_diagram(schema)
    st.code(diagram_code, language="mermaid")

    try:
        import streamlit.components.v1 as components
        components.html(f"""
        <pre class="mermaid">
        {diagram_code}
        </pre>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """, height=900)
    except Exception as e:
        st.error(f"Unable to render diagram: {e}")

with tab2:
    st.subheader("All Table Definitions")
    for table, table_data in schema.items():
        with st.expander(f"📁 {table.capitalize()}"):
            table_schema = {
                col: info for col, info in table_data.items()
                if isinstance(info, dict) and "type" in info
            }
            st.json(table_schema)
