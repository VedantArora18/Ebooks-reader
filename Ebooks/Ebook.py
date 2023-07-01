import pyttsx3
import PyPDF2
book = open('For the Love of Physics by Walter Lewin.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(pages):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
