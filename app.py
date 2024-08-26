import streamlit as st
import aspose.pdf as ap
from io import BytesIO
import os

# Function to compress PDF and get file sizes
def pdf_compression(uploaded_file):
    # Save the uploaded file temporarily
    input_path = "uploaded.pdf"
    output_path = "compressed.pdf"
    
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    # Load the PDF document
    pdf_document = ap.Document(input_path)
    
    # Set optimization options for compression
    pdfoptimiz = ap.optimization.OptimizationOptions()
    pdfoptimiz.image_compression_options.compress_images = True
    pdfoptimiz.image_compression_options.image_quality = 15
    pdf_document.optimize_resources(pdfoptimiz)
    
    # Save the compressed PDF document
    pdf_document.save(output_path)
    
    # Get file sizes
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)
    
    # Prepare the compressed file for download
    with open(output_path, "rb") as f:
        compressed_file = BytesIO(f.read())
    
    compressed_file.seek(0)
    
    return compressed_file, original_size, compressed_size

# Streamlit app
def main():
    primaryColor="#c3bf19"
    backgroundColor="#f52323"
    secondaryBackgroundColor="#000000"
    textColor="#ffffff"

    # Add a sidebar for additional options
    st.sidebar.title("About Us")
    st.sidebar.write("""
    **Manappuram** is a leading non-banking financial company (NBFC) in India, known for providing a wide range of financial services, including gold loans, microfinance, housing finance, and insurance. With a commitment to financial inclusion and customer-centric services, **Manappuram** strives to make a significant impact in the financial sector through innovation and excellence.

    This app was developed by the **AI team** of the **R&D department** at **MAFIL**. Our team is dedicated to leveraging artificial intelligence and machine learning technologies to innovate and enhance the efficiency of financial services. The **AI team** at **MAFIL** is focused on research, development, and deployment of advanced AI solutions to solve real-world problems and drive digital transformation.
    """)

    st.image("C:\\Users\\kolla\\Downloads\\mannapuram2.jpeg",use_column_width=True)
    st.title("PDF Compressor")
    st.write("Upload a PDF file to compress it and download the compressed version.")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write(f"Uploaded file: {uploaded_file.name}")
        
        # Compress PDF and get file sizes
        compressed_file, original_size, compressed_size = pdf_compression(uploaded_file)
        
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
