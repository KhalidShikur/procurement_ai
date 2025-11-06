from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# def generate_pdf(top_bids, filename="procurement_report.pdf"):
#     c = canvas.Canvas(filename, pagesize=A4)
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(100, 800, "Procurement Report")
#     c.setFont("Helvetica", 12)

#     y = 760
#     for i, row in top_bids.iterrows():
#         c.drawString(100, y, f"{i+1}. {row['bidder']} - Score: {row['score']:.4f}")
#         y -= 15
#         c.drawString(120, y, f"Summary: {row['summary']}")
#         y -= 25
#         if y < 50:
#             c.showPage()
#             y = 800
#     c.save()


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(top_bids, filename="procurement_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "Procurement Report")
    c.setFont("Helvetica", 11)

    y = 780
    for i, row in top_bids.iterrows():
        c.drawString(50, y, f"{i+1}. {row['bidder']} - Score: {row['score']:.4f}")
        y -= 15
        # Shorten summary for faster PDF writing
        summary_text = (row['summary'][:200] + '...') if len(row['summary']) > 200 else row['summary']
        c.drawString(70, y, f"Summary: {summary_text}")
        y -= 25
        if y < 50:
            c.showPage()
            y = 780
    c.save()
