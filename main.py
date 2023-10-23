import pyttsx3
from PyPDF2 import PdfReader

fileReader = PdfReader(open('foo.pdf', 'rb'))

ttsEngine = pyttsx3.init()
text = ""

for i,page in enumerate(fileReader.pages):
    text += fileReader.pages[i].extract_text().strip().replace('\n', ' ')

print(text)
ttsEngine.save_to_file('hello', 'HelloSound.mp3')
ttsEngine.save_to_file(text, 'foo.mp3')
ttsEngine.runAndWait()
print('done')

ttsEngine.stop()
