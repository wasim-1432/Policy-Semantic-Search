import os
import re


def extract_metadata(text):
    department = re.search(r"Department:\s*(.*)", text)
    document_type = re.search(r"Document Type:\s*(.*)", text)
    date = re.search(r"Date:\s*(.*)", text)
    access_level = re.search(r"Access Level:\s*(.*)", text)

    return {
        "department": department.group(1).strip() if department else "",
        "document_type": document_type.group(1).strip() if document_type else "",
        "date": date.group(1).strip() if date else "",
        "access_level": access_level.group(1).strip() if access_level else ""
    }


def load_documents(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            metadata = extract_metadata(text)

            metadata["source"] = filename

            documents.append({
                "text": text,
                "metadata": metadata
            })

    return documents