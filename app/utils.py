from docxtpl import DocxTemplate
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "templates" / "nda_template.docx"

def generate_nda(
    party1_name, party1_address, party1_state, party1_entity,
    party2_name, party2_address, party2_state, party2_entity
):
    doc = DocxTemplate(TEMPLATE_PATH)

    context = {
        'party1_name': party1_name,
        'party1_address': party1_address,
        'party1_state': party1_state,
        'party1_entity': party1_entity,
        'party2_name': party2_name,
        'party2_address': party2_address,
        'party2_state': party2_state,
        'party2_entity': party2_entity,
    }

    doc.render(context)

    output_path = Path(__file__).parent / "generated_nda.docx"
    doc.save(output_path)

    return output_path
