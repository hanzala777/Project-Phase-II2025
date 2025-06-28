import streamlit as st
import importlib.util
import os

# Load the schema from the uploaded file
schema_file = "agriculture_schema.py"
spec = importlib.util.spec_from_file_location("agriculture_schema", schema_file)
schema_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(schema_module)
# schema = schema_module.schema
schema = schema_module.get_agriculture_schema()


# Mermaid ER diagram generator
def generate_mermaid_er_diagram(schema):
    lines = ["erDiagram"]
    for table_name, columns in schema.items():
        lines.append(f"  {table_name} {{")
        for attr, info in columns.items():
            if isinstance(info, dict):
                attr_type = info.get("type", "string").lower()
                suffix = " PK" if info.get("primary_key") else ""
                lines.append(f"{attr_type} {attr}{suffix}")
        lines.append("  }")

    for table_name, columns in schema.items():
        for attr, info in columns.items():
            if isinstance(info, dict) and "foreign_key" in info:
                fk = info["foreign_key"]
                if "." in fk:
                    ref_table, _ = fk.split(".")
                    lines.append(f"  {table_name} ||--o| {ref_table} : \"{attr}\"")
    return "\n".join(lines)

# Streamlit UI
st.title("📊 Agricultural Schema ER Diagram")

with st.expander("🔍 View Schema Dictionary"):
    st.json(schema)

st.subheader("📈 Entity Relationship Diagram (Mermaid)")
diagram_code = generate_mermaid_er_diagram(schema)
st.code(diagram_code, language="mermaid")

# Optional: render diagram using Mermaid plugin in Streamlit
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
    """, height=600)
except Exception as e:
    st.error(f"Unable to render diagram: {e}")
