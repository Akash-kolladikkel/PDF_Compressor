import streamlit as st
import aspose.words as aw
from io import BytesIO
import os
import PyPDF2  

def compress_pdf(input_stream):
    # Create a PDF renderer
    renderer = aw.pdf2word.fixedformats.PdfFixedRenderer()
    
    # Set PDF read options
    pdf_read_options = aw.pdf2word.fixedformats.PdfFixedOptions()
    pdf_read_options.image_format = aw.pdf2word.fixedformats.FixedImageFormat.JPEG
    pdf_read_options.jpeg_quality = 50
    
    # Convert PDF pages to images
    pages_stream = renderer.save_pdf_as_images(input_stream, pdf_read_options)
    
    # Create a new document
    builder = aw.DocumentBuilder()
    
    for i in range(len(pages_stream)):
        # Set maximum page size to avoid the current page image scaling
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
        
        # Insert a page break if it's not the last page
        if i != len(pages_stream) - 1:
            builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
    
    # Save options
    save_options = aw.saving.PdfSaveOptions()
    save_options.cache_background_graphics = True
    
    # Save the document to a BytesIO object
    output = BytesIO()
    builder.document.save(output, save_options)
    output.seek(0)
    
    # Remove the first page from the compressed PDF
    output_without_watermark = remove_first_page(output)
    
    return output_without_watermark

def set_page_size(page_setup, width, height):
    page_setup.page_width = width
    page_setup.page_height = height

def remove_first_page(pdf_stream):
    # Use PyPDF2 to remove the first page from the compressed PDF
    pdf_stream.seek(0)
    reader = PyPDF2.PdfReader(pdf_stream)
    writer = PyPDF2.PdfWriter()

    # Add all pages except the first one
    for page_num in range(1, len(reader.pages)):
        page = reader.pages[page_num]
        writer.add_page(page)
    
    # Write the modified PDF to a new BytesIO stream
    output_stream = BytesIO()
    writer.write(output_stream)
    output_stream.seek(0)
    
    return output_stream

def main():
    # Add a sidebar for additional options
    st.sidebar.title("About Us")
    st.sidebar.write("""
     This app was developed by the **AI team** of the **R&D department** at **MAFIL**.
     Our team is dedicated to leveraging artificial intelligence and machine learning technologies to innovate and enhance the efficiency
     of financial services.
    """)

    st.image("mannapuram2.jpeg", width=300)
    st.title("PDF Compressor")
    st.write("Upload a PDF file to compress it and download the compressed version.")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write(f"Uploaded file: {uploaded_file.name}")
        
        # Get original file size
        uploaded_file.seek(0)
        original_size = len(uploaded_file.getvalue())
        
        # Compress PDF
        with st.spinner("Compressing PDF..."):
            compressed_file = compress_pdf(uploaded_file)
        
        # Get compressed file size
        compressed_size = len(compressed_file.getvalue())
        
        # Display file sizes before and after compression
        st.write(f"Original file size: {original_size / 1024:.2f} KB")
        st.write(f"Compressed file size: {compressed_size / 1024:.2f} KB")

        # Display the compression ratio
        compression_ratio = compressed_size / original_size * 100
        st.write(f"Compression ratio: {compression_ratio:.2f}%")
        
        st.success("PDF compression completed!")
        
        # Provide download button for the compressed PDF
        st.download_button(
            label="Download Compressed PDF",
            data=compressed_file,
            file_name="compressed_" + uploaded_file.name,
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
