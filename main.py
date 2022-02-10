from jinja2 import Template
import pdfkit

from documentcontent import document_content

template = ""  # insert html string here
tm = Template(template)

msg = tm.render(data=document_content)
# print(msg)
filepath = './temp_pdf_file10.pdf'
options = {
    'margin-top': '30mm',
    'margin-bottom': '30mm',
    'header-right': 'Page [page] of [topage]',
    'header-font-size': '8',
}
pdfkit.from_string(msg, filepath, options=options)
