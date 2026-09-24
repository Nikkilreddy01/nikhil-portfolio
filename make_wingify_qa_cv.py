from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
import sys
import pypdf

OUT = "/Users/nikhilreddy/cv/K_Ram_Nikhil_Reddy_Wingify_QA_Intern_CV.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    topMargin=0.26 * inch, bottomMargin=0.26 * inch,
    leftMargin=0.52 * inch, rightMargin=0.52 * inch,
)

name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15, alignment=TA_CENTER, spaceAfter=1)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.7, alignment=TA_CENTER, spaceAfter=4)
heading_style = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=9.8, spaceBefore=2.5, spaceAfter=1, textColor=colors.black)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=8.5, leading=10.6, spaceAfter=2)
bullet_style = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.4, leading=10.4, leftIndent=11, bulletIndent=0, spaceAfter=0.4)
proj_title_style = ParagraphStyle("proj_title", fontName="Helvetica-Bold", fontSize=9.0, leading=10.8, spaceBefore=1.5, spaceAfter=0)
proj_meta_style = ParagraphStyle("proj_meta", fontName="Helvetica-Oblique", fontSize=8.2, leading=9.8, spaceAfter=0.4)
proj_date_style = ParagraphStyle("proj_date", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.8, alignment=TA_RIGHT)
edu_title_style = ParagraphStyle("edu_title", fontName="Helvetica-Bold", fontSize=8.7, leading=10.8, spaceAfter=0)
edu_date_style = ParagraphStyle("edu_date", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.8, alignment=TA_RIGHT)
edu_sub_style = ParagraphStyle("edu_sub", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.2, spaceAfter=1.5)
cert_style = ParagraphStyle("cert", fontName="Helvetica", fontSize=8.4, leading=10.2, leftIndent=11)
cert_date_style = ParagraphStyle("cert_date", fontName="Helvetica", fontSize=8.4, leading=10.2, alignment=TA_RIGHT)

ROW_WIDTHS = [5.2 * inch, 2.03 * inch]

def rule():
    return HRFlowable(width="100%", thickness=0.75, color=colors.black, spaceBefore=1, spaceAfter=2.5)

def bullets(items):
    return [Paragraph(f"&bull;&nbsp;&nbsp;{t}", bullet_style) for t in items]

def date_row(left_html, right_html, left_style=proj_title_style, right_style=proj_date_style, space_before=1.5):
    t = Table([[Paragraph(left_html, left_style), Paragraph(right_html, right_style)]], colWidths=ROW_WIDTHS)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), space_before),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t

story = []

# HEADER
story.append(Paragraph("K RAM NIKHIL REDDY", name_style))
story.append(Paragraph(
    "Nellore, Andhra Pradesh &ndash; India &nbsp;|&nbsp; +91 8096502384 &nbsp;|&nbsp; ramnikhilreddy.pro@gmail.com<br/>"
    "linkedin.com/in/ram-nikhil-reddy &nbsp;|&nbsp; github.com/Nikkilreddy01",
    contact_style))

# PROFESSIONAL SUMMARY
story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
story.append(rule())
story.append(Paragraph(
    "Computer Science undergraduate specializing in Software Quality Assurance (QA) and Automated Web Testing. "
    "Experienced in designing and executing automated test frameworks with Playwright, TypeScript, JavaScript, and Python (Pytest), "
    "applying the Page Object Model (POM) and STLC methodologies. Skilled in manual exploratory testing, edge-case identification, "
    "REST API verification, and defect tracking. Passionate about software reliability and building high-performance web products.",
    body_style))

# TECHNICAL SKILLS
story.append(Paragraph("TECHNICAL SKILLS", heading_style))
story.append(rule())
skills_rows = [
    ("QA Automation &amp; Frameworks", "Playwright, TypeScript, JavaScript, Python (Pytest), Page Object Model (POM), Allure &amp; HTML Reporting"),
    ("Testing Methodologies", "Manual &amp; Functional Testing, Regression &amp; Smoke Testing, Cross-Browser / Multi-Tab UI Testing, E2E Test Design, Edge Cases"),
    ("API &amp; Backend Testing", "REST API Testing (Postman, FastAPI TestClient), Schema Validation (Zod, Pydantic), Database Testing (PostgreSQL, ClickHouse)"),
    ("QA Lifecycle &amp; Tools", "SDLC &amp; STLC, Test Case Design &amp; Execution, Bug Tracking &amp; Documentation (Jira, GitHub Issues), Root Cause Analysis"),
    ("DevOps &amp; Developer Tools", "Git/GitHub, GitHub Actions (CI/CD Automated Testing), Docker, Linux/macOS, Winston Logging"),
    ("Core Competencies", "Data Structures &amp; Algorithms, Analytical Problem Solving, Agile/Scrum Collaboration, Code Review"),
]
label_style = ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=8.5, leading=10.6)
val_style = ParagraphStyle("val", fontName="Helvetica", fontSize=8.5, leading=10.6)
skills_table_data = [[Paragraph(k, label_style), Paragraph(v, val_style)] for k, v in skills_rows]
skills_table = Table(skills_table_data, colWidths=[1.72 * inch, 5.51 * inch])
skills_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 0.3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.3),
]))
story.append(skills_table)

# EXPERIENCE
story.append(Paragraph("EXPERIENCE", heading_style))
story.append(rule())
story.append(date_row(
    "Software &amp; QA Engineer (Freelance) &mdash; ecentra2k26.in",
    "Remote | Jan &ndash; Jun 2026",
    space_before=0))
story.extend(bullets([
    "Executed manual and automated functional testing for a live event platform (React/Next.js frontend, Node.js REST backend, PostgreSQL) serving <b>1,500+ active users</b>.",
    "Designed structured test cases and automated regression suites; verified input validation schemas and edge-case boundaries, preventing runtime defects and maintaining 99.9% uptime.",
    "Documented and tracked UI inconsistencies, functional regressions, and database state issues, collaborating across development to ensure software stability.",
]))

# PROJECTS
story.append(Paragraph("PROJECTS", heading_style))
story.append(rule())

story.append(date_row(
    'Dream Portal &mdash; Automated Web Testing &amp; AI Validation &nbsp;|&nbsp; Playwright &middot; TypeScript &middot; POM &middot; OpenAI API &nbsp;|&nbsp; '
    '<link href="https://github.com/Nikkilreddy01/dream-portal-automation" color="blue">Repo</link>',
    "Sep 2026", space_before=0))
story.extend(bullets([
    "Architected an automated functional testing framework with Playwright and TypeScript, implementing the Page Object Model (POM) architecture across 13 test suites.",
    "Automated complex UI behaviors including 3-second loader animation verification, event-driven multi-tab synchronization (<code>context.on('page')</code>), and dynamic recurring dream frequency analysis.",
    "Integrated dual-layer AI sentiment classification using OpenAI API (<code>gpt-4o-mini</code>) and a keyword NLP fallback; built GitHub Actions CI pipeline for automated test execution and Allure reporting.",
]))

story.append(date_row(
    'Chrontinal &mdash; SIEM Testing &amp; High-Throughput Verification &nbsp;|&nbsp; Python &middot; Pytest &middot; FastAPI &middot; Go &middot; ClickHouse &nbsp;|&nbsp; '
    '<link href="https://github.com/Nikkilreddy01/chrontinal" color="blue">Repo</link>',
    "Feb 2026 &ndash; Apr 2026"))
story.extend(bullets([
    "Architected comprehensive automated test suites for an enterprise security platform, validating <b>3,882,816 triage events</b> and <b>7,476 automated investigations</b>.",
    "Conducted regression auditing and data leakage tests across 7 release cycles, identifying schema anomalies, edge-case bottlenecks, and metric distortions.",
    "Verified high-throughput data streaming sustaining <b>26,586 events/sec</b> with <b>0% data loss</b> across 26 ClickHouse analytical tables; won the <b>Jury's Choice Award</b> at MEITY &times; NASSCOM Cyber Security Innovation Challenge.",
]))

# ACHIEVEMENTS
story.append(Paragraph("ACHIEVEMENTS", heading_style))
story.append(rule())
story.extend(bullets([
    "<b>Jury's Choice Award</b> &mdash; Cyber Security Innovation Challenge 1.0 (MEITY, NASSCOM &amp; DSCI): built autonomous evaluation platform with automated threat detection and testing workflows.",
    "<b>2nd Position</b> &mdash; NASSCOM AI Code Sarathi - Agentic AI Hackathon: developed agentic AI workflow with automated evaluation and testing architecture.",
]))

# CERTIFICATIONS
story.append(Paragraph("CERTIFICATIONS", heading_style))
story.append(rule())
cert_rows = [
    ("Data Structures and Algorithms &mdash; Lovely Professional University", "May 2025"),
    ("Career Essentials in Generative AI &mdash; Microsoft / LinkedIn Learning", "Sep 2025"),
    ("AI Foundations Associate &mdash; Oracle", "Jul 2025"),
    ("Google Cybersecurity Professional Certificate &mdash; Google / Coursera", "Feb 2025"),
]
for left, right in cert_rows:
    story.append(date_row(f"&bull;&nbsp;&nbsp;{left}", right, left_style=cert_style, right_style=cert_date_style, space_before=0.8))

# EDUCATION
education_block = [
    Paragraph("EDUCATION", heading_style),
    rule(),
    date_row("B.Tech. Computer Science &amp; Engineering &mdash; CGPA: 8", "Aug 2023 &ndash; Present", left_style=edu_title_style, right_style=edu_date_style, space_before=0),
    Paragraph("Lovely Professional University, Phagwara, Punjab", edu_sub_style),
    date_row("Intermediate (PCM) &mdash; 96.7%", "Mar 2022 &ndash; May 2023", left_style=edu_title_style, right_style=edu_date_style, space_before=0),
    Paragraph("Narayana College, Nellore", edu_sub_style),
    date_row("Matriculation &mdash; 99%", "Mar 2019 &ndash; May 2020", left_style=edu_title_style, right_style=edu_date_style, space_before=0),
    Paragraph("Narayana School, Nellore", edu_sub_style),
]
story.append(KeepTogether(education_block))

doc.build(story)

reader = pypdf.PdfReader(OUT)
num_pages = len(reader.pages)
print(f"Generated {OUT} with {num_pages} page(s).")
if num_pages != 1:
    print(f"WARNING: Expected 1 page, but got {num_pages} pages!")
    sys.exit(1)
