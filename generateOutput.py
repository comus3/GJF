import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Spacer


def generateMotiv(replacement_dict):
    def replace_in_file_and_save(dictionary):
        input_filename = "MOTIV_TMPL8.txt"
        output_filename = "MOTIV_REPLACED_text.txt"
        try:
            with open(input_filename, 'r',encoding="utf-8") as file:
                content = file.read()

            for key, value in dictionary.items():
                content = content.replace(key, value)

            output_folder = "output"

            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, 'w',encoding="utf-8") as file:
                file.write(content)

            print(f"GENERATEOUTPUT (GenerateMOTIV (replace in file)):Replacements saved to '{output_path}' successfully.")
        except FileNotFoundError:
            print(f"GENERATEOUTPUT (GenerateMOTIV (replace in file)): File '{input_filename}' not found.")
        except Exception as e:
            print(f"GENERATEOUTPUT (GenerateMOTIV (replace in file)): An error occurred: {str(e)}")
            
    def generate_pdf():
        input_file = "output/MOTIV_REPLACED_text.txt"
        output_file = "output/CPC-Motiv.pdf"
        try:
            # Read the content from the input file and decode it as UTF-8
            with open(input_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Initialize a PDF document
            doc = SimpleDocTemplate(output_file, pagesize=letter)
            story = []

            # Define the styles for the document
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='CustomStyle', parent=styles['Normal'],fontName='Helvetica-Bold',fontSize=12))
            bold = styles['CustomStyle']
            normal = styles['Normal']

            # Add paragraphs to the document
            for i, line in enumerate(lines):
                if i == 0:
                    p = Paragraph(line.strip(), bold)
                elif i >= len(lines) - 2:
                    p = Paragraph(line.strip(), bold)
                else:
                    p = Paragraph(line.strip(), normal)
                story.append(p)
                story.append(Spacer(1, 12))  # Add some space between paragraphs

            doc.build(story)
            
            print(f"GENERATEOUPUT(GenerateMOTIV(generatePDF)): PDF saved to '{output_file}' successfully.")
        except FileNotFoundError:
            print(f"GENERATEOUPUT(GenerateMOTIV(generatePDF)): File '{input_file}' not found.")
        except Exception as e:
            print(f"GENERATEOUPUT(GenerateMOTIV(generatePDF)): An error occurred: {str(e)}")
    
    try:
        replace_in_file_and_save(replacement_dict)
        generate_pdf()
        return 0
    except:
        return 1
    
def generateMail(replacement_text):
    output_folder = 'output'
    # Read the content of the input file
    input_file_path = 'MAIL_TMPL8.txt'
    with open(input_file_path, 'r') as file:
        content = file.read()

    # Replace '{ELEMENT_1}' with the provided replacement text
    modified_content = content.replace('{ELEMENT_1}', replacement_text)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construct the output file path
    output_file_path = os.path.join(output_folder, 'email.txt')

    # Write the modified content to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(modified_content)

    print(f'GENERATEOUTPUT (MAIL): Replacement completed. Modified content saved to {output_file_path}')
    return 0

if __name__ == "__main__":
    #tesst functions
    replacement_dict = {
        "{ELEMENT_1}": "HELLOO ITS WORKING?(ELEMENT 1)",
        "{ELEMENT_2}": "HELLOO ITS WORKING?(ELEMENT 2)",
    }
    
    generateMotiv(replacement_dict)
    generateMail("THe big Come COMPANY")
    



#the following are old versions and are NOT WORKING ):

"""
import fitz  # PyMuPDF library

def generateMotiv(replacement_dict):
    pdf_file_path = "CPC-MOTIV-TEMP.pdf"
    output_pdf_path = "output/CPC-Motiv.pdf"
    # Open the input PDF file
    pdf_document = fitz.open(pdf_file_path)
    pdf_document_new = fitz.open()

    page = pdf_document[0]

    # Get the page's dimensions as integers
    page_width = int(page.mediabox[2])
    page_height = int(page.mediabox[3])

    # Create a new page with the same dimensions
    page_new = pdf_document_new.new_page(page_width, page_height)

    for block in page.get_text("blocks"):
        for line in block:
            for span in line:
                text = span[4]
                for old_word, new_word in replacement_dict.items():
                    # Replace all occurrences of old_word with new_word in the text
                    text = text.replace(old_word, new_word)
                page_new.insert_text(span[:4], text)

    # Save the modified PDF to the output path
    pdf_document_new.save(output_pdf_path)
    pdf_document.close()
    pdf_document_new.close()
"""

#NOT WORKING
"""
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import DecodedStreamObject, EncodedStreamObject, NameObject
import shutil

def replace_text(content, replacements = dict()):
    lines = content.splitlines()

    result = ""
    in_text = False

    for line in lines:
        if line == "BT":
            in_text = True

        elif line == "ET":
            in_text = False

        elif in_text:
            cmd = line[-2:]
            if cmd.lower() == 'tj':
                replaced_line = line
                for k, v in replacements.items():
                    replaced_line = replaced_line.replace(k, v)
                result += replaced_line + "\n"
            else:
                result += line + "\n"
            continue

        result += line + "\n"

    return result

def process_data(object, replacements):
    data = object.getData()
    decoded_data = data.decode('utf-8')

    replaced_data = replace_text(decoded_data, replacements)

    encoded_data = replaced_data.encode('utf-8')
    if object.decodedSelf is not None:
        object.decodedSelf.setData(encoded_data)
    else:
        object.setData(encoded_data)

def generateMotiv(replacements):
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--input", required=True, help="CPC-MOTIV-TEMP.pdf")
    # args = vars(ap.parse_args())

    #in_file = args["input"]
    in_file = "CPC-MOTIV-TEMP.pdf"
    filename_base = in_file.replace(os.path.splitext(in_file)[1], "")

    #replacements = { 'test': 'works!!!'}

    pdf = PdfFileReader(in_file)
    writer = PdfFileWriter()

    for page_number in range(0, pdf.getNumPages()):

        page = pdf.getPage(page_number)
        contents = page.getContents()

        if isinstance(contents, DecodedStreamObject) or isinstance(contents, EncodedStreamObject):
            process_data(contents, replacements)
        elif len(contents) > 0:
            for obj in contents:
                if isinstance(obj, DecodedStreamObject) or isinstance(obj, EncodedStreamObject):
                    streamObj = obj.getObject()
                    process_data(streamObj, replacements)

        # Force content replacement
        page[NameObject("/Contents")] = contents.decodedSelf
        writer.addPage(page)

    with open(filename_base + ".result.pdf", 'wb') as out_file:
        writer.write(out_file)
        
    
    # Define the source file (result.pdf) and the destination folder (output)
    source_file = "CPC-MOTIV-TEMP.result.pdf"
    destination_folder = "output"

    # Rename the file while moving it to the destination folder
    new_file_name = "CPC-Motiv.pdf"
    shutil.move(source_file, os.path.join(destination_folder, new_file_name))
    
"""