import fitz

def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    
    for page in doc:
        text += page.get_text()
    
    return text

if __name__ == "__main__":
    result = extract_text("test.pdf")
    print(f"Extracted {len(result)} characters")
    print(result[:500])