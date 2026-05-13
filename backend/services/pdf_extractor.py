import pdfplumber

def extract_text_from_pdf(file_byte: bytes) -> str:
    with pdfplumber.open(file_byte) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    return "\n".join([p for p in pages if p])