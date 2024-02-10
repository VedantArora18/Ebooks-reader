from flask import Flask, request, jsonify
import os
import pyttsx3
import PyPDF2

app = Flask(__name__)

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file is a PDF
    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Invalid file format. Please upload a PDF file'})

    # Save the uploaded PDF file
    pdf_path = 'uploaded_file.pdf'
    file.save(pdf_path)

    # Process the PDF file and generate speech
    try:
        book = open(pdf_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages

        speaker = pyttsx3.init()

        speech_output = []

        for num in range(pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
            speech_output.append(text)

        return jsonify({'success': True, 'speech_output': speech_output})

    except Exception as e:
        return jsonify({'error': f'Error processing the PDF file: {str(e)}'})

    finally:
        # Remove the uploaded file
        os.remove(pdf_path)

if __name__ == '_main_':
    app.run(debug=True)
