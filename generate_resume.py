from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

pdf_output = "Shahmir_Qureshi_Resume.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Heading", fontSize=16, leading=18, spaceAfter=8, alignment=TA_LEFT, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="SubHeading", fontSize=12, leading=14, spaceAfter=4, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="NormalText", fontSize=10, leading=12, spaceAfter=2, fontName="Helvetica"))
styles.add(ParagraphStyle(name="Link", fontSize=10, leading=12, textColor=colors.blue, underline=True))

doc = SimpleDocTemplate(pdf_output, pagesize=A4,
                        leftMargin=30, rightMargin=30, topMargin=20, bottomMargin=20)

story = []

# Header
story.append(Paragraph("<b>Shahmir Qureshi</b>", styles["Heading"]))
story.append(Paragraph("FRONTEND WEB DEVELOPER", styles["SubHeading"]))
story.append(Spacer(1, 10))

# Left column
left_column = [
    Paragraph("<b>Details</b>", styles["SubHeading"]),
    Paragraph("Karachi, Pakistan", styles["NormalText"]),
    Paragraph("3437943625", styles["NormalText"]),
    Paragraph("developershahmir@gmail.com", styles["NormalText"]),
    Spacer(1, 6),
    Paragraph("<b>Nationality</b>: Pakistani", styles["NormalText"]),
    Paragraph("<b>DOB</b>: 25-10-2007, Karachi", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Links</b>", styles["SubHeading"]),
    Paragraph('<link href="https://github.com/ShahmirAliQureshii">GitHub</link>', styles["Link"]),
    Paragraph('<link href="https://www.linkedin.com/in/shahmir-qureshi-162200252">LinkedIn</link>', styles["Link"]),
    Paragraph('<link href="https://shahmirqureshi.vercel.app">Portfolio</link>', styles["Link"]),
    Spacer(1, 10),
    Paragraph("<b>Skills</b>", styles["SubHeading"]),
    Paragraph("HTML, CSS, JavaScript, TypeScript, ReactJS, Redux, Tailwind CSS, Bootstrap, GSAP, API Integration, DOM Manipulation, Git & GitHub", styles["NormalText"]),
]

# Right column
right_column = [
    Paragraph("<b>Profile</b>", styles["SubHeading"]),
    Paragraph("Enthusiastic Frontend Developer with hands-on experience in building responsive and user-friendly web applications...", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Education</b>", styles["SubHeading"]),
    Paragraph("Matriculation, NED Foundation School", styles["NormalText"]),
    Paragraph("Computer Science, Nusrat Bhutto Government Degree Boys College, Karachi (August 2024 – Present)", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Interests</b>", styles["SubHeading"]),
    Paragraph("Front-end Web Development, Creative UI/UX Design, Full-stack MERN Development...", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Certifications & Achievements</b>", styles["SubHeading"]),
    Paragraph("Flutter Application Development Course (August 2022) – Completed at age 14", styles["NormalText"]),
    Paragraph("English Language Course Certificate", styles["NormalText"]),
    Paragraph("React + Redux Certificate, Karachi (July 2025 – August 2025)", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Projects</b>", styles["SubHeading"]),
    Paragraph("Flipkart Clone, Quran Website, QR Code Generator, Calculator Website, Cara Website (Incomplete), Plant Website (Incomplete), Blog Website (Incomplete), Chips Website, Burger Website, Employee Management System (August 2025)", styles["NormalText"]),
    Spacer(1, 10),
    Paragraph("<b>Internships</b>", styles["SubHeading"]),
    Paragraph("Web Developer Intern, Hex Softwares (August 2023 – September 2025)", styles["NormalText"]),
]

table_data = [[left_column, right_column]]
table = Table(table_data, colWidths=[180, 340])
table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
]))

story.append(table)

doc.build(story)

print(f"PDF created: {pdf_output}")