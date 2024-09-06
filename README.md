# PDF Compressor App
This is a Streamlit-based web application that compresses PDF files. The app uses **Aspose** for PDF compression by converting PDF pages to JPEG images and then reconstructing them as a PDF file.

## Features
- Compress PDFs while maintaining good quality.
- Input PDF size must be between 1 MB and 25 MB.
- User-friendly interface built using Streamlit.
- Download the compressed PDF after compression.

## Demo
You can try the app live here: [PDF Compressor App](https://ak-pdf-compress.streamlit.app)

## How It Works
1. Upload a PDF file using the interface.
2. The app compresses the file by converting PDF pages to JPEG and rebuilding them as a PDF.
3. Download the compressed version.

## Acknowledgments
This project is powered by:
- **[Aspose.Words for PDF processing](https://products.aspose.com/words/)**, enabling high-quality PDF manipulation and compression.
- **[Streamlit](https://streamlit.io/)**, which provided an incredibly easy-to-use framework to create the web application interface.
- **[Streamlit Cloud](https://streamlit.io/cloud)**, which allows free hosting and sharing of this app with the community.

## Dependencies
- `streamlit`
- `aspose-words`
- `PyPDF2`
