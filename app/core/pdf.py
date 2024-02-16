import pdfkit
import jinja2
import os

templateLoader = jinja2.FileSystemLoader(searchpath="./app/templates")
templateEnv = jinja2.Environment(loader=templateLoader)

wkhtmltopdf_path = os.getenv("BINPATH")

config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def create_pdf_invoice(data: dict):
    print(wkhtmltopdf_path, "PATH")
    template = templateEnv.get_template("invoice_template.html")
    html = template.render(invoice=data)
    pdf = pdfkit.from_string(html, options={"enable-local-file-access": True}, configuration=config)
    return pdf
  
def create_pdf_menu(data: dict):
    pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    template = templateEnv.get_template("menu_template.html")
    html = template.render(menu=data)
    pdf = pdfkit.from_string(html, options={"enable-local-file-access": True}, configuration=config)
    return pdf
  