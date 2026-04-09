# Traceability utilities — to be implemented by AI Dev in Phase 2
# Maps circular clause references to company document sections

def build_trace_reference(circular_section: str, document_name: str, document_section: str) -> dict:
    return {
        "circular_section": circular_section,
        "document_name": document_name,
        "document_section": document_section,
    }
