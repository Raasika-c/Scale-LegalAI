import sys
import json
from docx import Document

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No DOCX path provided"}))
        return

    docx_path = sys.argv[1]

    try:
        document = Document(docx_path)
        text = ""

        for para in document.paragraphs:
            if para.text.strip():
                text += para.text + "\n"

        print(json.dumps({"text": text}, ensure_ascii=False))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
