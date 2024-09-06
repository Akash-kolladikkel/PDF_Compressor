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

## Code Logic

The logic for PDF compression uses the **Aspose.Words** library to convert each PDF page to an image, compress it, and reassemble the images into a PDF. Below is the core code that handles the conversion:

```python
import aspose.words as aw

# Create a PDF renderer
renderer = aw.pdf2word.fixedformats.PdfFixedRenderer()

# Set PDF read options
pdf_read_options = aw.pdf2word.fixedformats.PdfFixedOptions()
pdf_read_options.image_format = aw.pdf2word.fixedformats.FixedImageFormat.JPEG
pdf_read_options.jpeg_quality = 50

with open("Input.pdf", 'rb') as pdf_stream:
    pages_stream = renderer.save_pdf_as_images(pdf_stream, pdf_read_options)

    builder = aw.DocumentBuilder()

    for i in range(0, len(pages_stream)):
        # Set maximum page size to avoid the current page image scaling.
        max_page_dimension = 1584
        page_setup = builder.page_setup
        set_page_size(page_setup, max_page_dimension, max_page_dimension)

        # Insert the page image
        page_image = builder.insert_image(pages_stream[i])
        set_page_size(page_setup, page_image.width, page_image.height)

        # Set margins to 0
        page_setup.top_margin = 0
        page_setup.left_margin = 0
        page_setup.bottom_margin = 0
        page_setup.right_margin = 0

        if i != len(pages_stream) - 1:
            builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)

    # Save the output
    save_options = aw.saving.PdfSaveOptions()
    save_options.cache_background_graphics = True
    builder.document.save("Output.pdf", save_options)

def set_page_size(page_setup, width, height):
    page_setup.page_width = width
    page_setup.page_height = height
```

## Acknowledgments
This project is powered by:
- **[Aspose.Words for PDF processing](https://products.aspose.com/words/)**, enabling high-quality PDF manipulation and compression.
- **[Streamlit](https://streamlit.io/)**, which provided an incredibly easy-to-use framework to create the web application interface.
- **[Streamlit Cloud](https://streamlit.io/cloud)**, which allows free hosting and sharing of this app with the community.

## Dependencies
- `streamlit`
- `aspose-words`
- `PyPDF2`
