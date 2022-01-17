import os
import webbrowser
from fpdf import FPDF


class PdfReport:
    """Guess"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """"""
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("./files/house.png")

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=80, txt="Flatmates Bill", border=1, align='c', ln=1)
        pdf.cell(w=50, h=40, txt=bill.period, border=0, align='c', ln=2)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=80, txt=flatmate1.name, border=0, align='c', ln=1)
        pdf.cell(w=50, h=40, txt=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)), border=0, align='c',
                 ln=1)

        pdf.cell(w=100, h=80, txt=flatmate2.name, border=0, align='c', ln=1)
        pdf.cell(w=50, h=40, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, align='c',
                 ln=1)

        os.chdir("files")
        pdf.output(self.filename)

        webbrowser.open(self.filename)
