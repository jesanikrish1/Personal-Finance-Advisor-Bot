from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def make_pdf(budget, expenses):
    buf=BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=letter)
    styles=getSampleStyleSheet()
    story=[Paragraph("Personal Finance Advisor Bot",styles["Title"]),
           Paragraph("Monthly budget learning summary",styles["Heading2"]),
           Paragraph("Educational use only — not financial advice.",styles["Normal"]),Spacer(1,12)]
    data=[["Item","Amount (₹)"],["Monthly income",f'{budget["income"]:,.0f}'],
          ["Suggested needs (50%)",f'{budget["needs_target"]:,.0f}'],
          ["Suggested wants (30%)",f'{budget["wants_target"]:,.0f}'],
          ["Suggested savings (20%)",f'{budget["savings_target"]:,.0f}'],
          ["Entered total",f'{budget["total_expenses"]:,.0f}'],
          ["Remaining",f'{budget["remaining"]:,.0f}']]
    table=Table(data, colWidths=[300,150])
    table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#dbeafe")),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),("PADDING",(0,0),(-1,-1),7)]))
    story += [table,Spacer(1,12),Paragraph("Reminder",styles["Heading3"]),
              Paragraph("The 50–30–20 split is a guideline. SIP investments are market-linked and can lose value. "
                        "Consider your goals and risk tolerance and consult a qualified professional for personal advice.",styles["BodyText"])]
    doc.build(story)
    return buf.getvalue()
