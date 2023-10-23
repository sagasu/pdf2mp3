import pyttsx3
from PyPDF2 import PdfReader

fileReader = PdfReader(open('foo.pdf', 'rb'))

ttsEngine = pyttsx3.init()

for i,page in enumerate(fileReader.pages):
    text = fileReader.pages[i].extract_text().strip().replace('\n', ' ')

ttsEngine.save_to_file(text, 'foo.mp3')
ttsEngine.runAndWait()

ttsEngine.stop()
