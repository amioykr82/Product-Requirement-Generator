import pdfplumber

def extract_text_chunks(pdf_path: str, min_lines: int = 3, max_lines: int = 15):
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = [line.strip() for line in text.split("\n") if line.strip()]
            buffer = []

            for line in lines:
                buffer.append(line)
                if len(buffer) >= max_lines or (len(buffer) >= min_lines and line.endswith(":")):
                    chunks.append(" ".join(buffer))
                    buffer = []

            if buffer:
                chunks.append(" ".join(buffer))

    return chunks

