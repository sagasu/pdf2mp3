from spire.pdf.common import *
from spire.pdf import *

pdf = PdfDocument()

pdf.LoadFromFile("Foo.pdf")

pdf.SaveToFile("Foo.docx", FileFormat.DOCX)

pdf.Close()