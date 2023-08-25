from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")
for index,row in df.iterrows():
    pdf.add_page()

    # Header
    pdf.set_font('Times', 'B', 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for i in range(33,290,10):
        pdf.line(10,i , 200, i)
    pdf.line(10,22,200,22)

    # Footer
    pdf.ln(265)
    pdf.set_font('Times','I',8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font('Times', 'I', 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for i in range(33, 290, 10):
            pdf.line(10, i, 200, i)

pdf.output("output.pdf")
