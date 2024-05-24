# Example demonstrating Interface Segregation Principle

# Interface for a document
class Document:
    def open(self):
        pass

    def save(self):
        pass

# Interface for a printable document
class PrintableDocument:
    def print_document(self):
        pass

# Interface for a searchable document
class SearchableDocument:
    def search(self, keyword):
        pass

# Class implementing a PDF document
class PDFDocument(Document, PrintableDocument, SearchableDocument):
    def open(self):
        print("Opening PDF document")

    def save(self):
        print("Saving PDF document")

    def print_document(self):
        print("Printing PDF document")

    def search(self, keyword):
        print(f"Searching for '{keyword}' in PDF document")

# Class implementing a Word document
class WordDocument(Document, PrintableDocument):
    def open(self):
        print("Opening Word document")

    def save(self):
        print("Saving Word document")

    def print_document(self):
        print("Printing Word document")

# Usage
if __name__ == "__main__":
    pdf_document = PDFDocument()
    word_document = WordDocument()

    # Performing operations on PDF document
    pdf_document.open()
    pdf_document.print_document()
    pdf_document.search("SOLID principles")

    # Performing operations on Word document
    word_document.open()
    word_document.print_document()
