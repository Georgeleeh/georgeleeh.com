from io import BytesIO

from flask import Blueprint, current_app, render_template, send_file
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

main_bp = Blueprint("main", __name__)


def _build_resume_pdf() -> BytesIO:
    profile = current_app.config["PROFILE"]
    highlights = current_app.config["KEY_HIGHLIGHTS"]
    experience = current_app.config["EXPERIENCE"]
    skills = current_app.config["SKILLS"]
    contact_email = current_app.config["CONTACT_EMAIL"]
    linkedin_url = current_app.config["LINKEDIN_URL"]

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    margin = 40
    y = height - margin

    ink = colors.HexColor("#0F172A")
    muted = colors.HexColor("#475569")
    accent = colors.HexColor("#1D4ED8")
    accent_soft = colors.HexColor("#DBEAFE")
    line_color = colors.HexColor("#CBD5E1")
    white = colors.HexColor("#FFFFFF")

    def wrap_text(text: str, font: str, size: int, max_width: float):
        words = text.split()
        if not words:
            return [""]
        lines = []
        current = words[0]
        for word in words[1:]:
            trial = f"{current} {word}"
            if pdf.stringWidth(trial, font, size) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
        return lines

    def ensure_space(y_pos: float, needed: float):
        if y_pos - needed < 46:
            pdf.showPage()
            draw_page_chrome()
            return height - 80
        return y_pos

    def section_title(
        label: str,
        x_pos: float,
        y_pos: float,
        width_limit: float,
        divider_len: float | None = None,
    ) -> float:
        title_text = label.upper()
        pdf.setFillColor(accent)
        pdf.rect(x_pos, y_pos - 3, 4, 13, stroke=0, fill=1)
        pdf.setFillColor(ink)
        pdf.setFont("Helvetica-Bold", 12)
        title_x = x_pos + 9
        pdf.drawString(title_x, y_pos, title_text)
        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.8)
        title_w = pdf.stringWidth(title_text, "Helvetica-Bold", 12)
        line_start = title_x + title_w + 8
        if divider_len is None:
            line_end = x_pos + width_limit
        else:
            line_end = min(line_start + divider_len, x_pos + width_limit)
        if line_end > line_start:
            pdf.line(line_start, y_pos + 3, line_end, y_pos + 3)
        return y_pos - 18

    def draw_page_chrome():
        pdf.setFillColor(white)
        pdf.rect(0, 0, width, height, stroke=0, fill=1)
        pdf.setFillColor(accent_soft)
        pdf.rect(0, height - 62, width, 62, stroke=0, fill=1)
        pdf.setFillColor(accent)
        pdf.rect(0, height - 62, 10, 62, stroke=0, fill=1)

        pdf.setFillColor(ink)
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(margin, height - 36, profile["name"])
        pdf.setFont("Helvetica", 10)
        pdf.setFillColor(muted)
        pdf.drawString(margin, height - 52, f"{profile['title']} · {profile['location']}")

        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(ink)
        pdf.drawRightString(width - margin, height - 36, contact_email)
        pdf.setFillColor(muted)
        pdf.drawRightString(width - margin, height - 50, "georgeleeh.com")

        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.9)
        pdf.line(margin, 36, width - margin, 36)
        pdf.setFont("Helvetica", 8)
        pdf.setFillColor(muted)
        pdf.drawString(margin, 24, "Resume generated from live portfolio data")
        pdf.drawRightString(width - margin, 24, "linkedin")

    draw_page_chrome()
    y = height - 80

    # Summary
    y = section_title("Summary", margin, y, width - (margin * 2))
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica", 10)
    for summary_line in wrap_text(profile["summary"], "Helvetica", 10, width - (margin * 2)):
        y = ensure_space(y, 14)
        pdf.drawString(margin, y, summary_line)
        y -= 13
    y -= 8

    # Two-column body
    left_x = margin
    gap = 16
    left_w = 180
    right_x = left_x + left_w + gap
    right_w = width - margin - right_x

    left_y = y
    right_y = y

    # Left column: highlights + skills + links
    left_y = section_title("Highlights", left_x, left_y, left_w)
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica", 9)
    for item in highlights:
        wrapped = wrap_text(item, "Helvetica", 9, left_w - 12)
        for i, line in enumerate(wrapped):
            bullet = "• " if i == 0 else "  "
            pdf.drawString(left_x + 6, left_y, f"{bullet}{line}")
            left_y -= 12
        left_y -= 2

    left_y -= 6
    left_y = section_title("Core Skills", left_x, left_y, left_w)
    pill_x = left_x + 1
    pill_y = left_y
    for skill in skills:
        label = skill if len(skill) <= 25 else f"{skill[:22]}..."
        pill_w = pdf.stringWidth(label, "Helvetica", 8) + 14
        if pill_x + pill_w > left_x + left_w:
            pill_x = left_x + 1
            pill_y -= 15
        pdf.setFillColor(accent_soft)
        pdf.roundRect(pill_x, pill_y - 9, pill_w, 12, 5, stroke=0, fill=1)
        pdf.setStrokeColor(colors.HexColor("#BFDBFE"))
        pdf.setLineWidth(0.6)
        pdf.roundRect(pill_x, pill_y - 9, pill_w, 12, 5, stroke=1, fill=0)
        pdf.setFillColor(ink)
        pdf.setFont("Helvetica", 8)
        pdf.drawString(pill_x + 6, pill_y - 5, label)
        pill_x += pill_w + 5
    left_y = pill_y - 28

    left_y = section_title("Links", left_x, left_y, left_w)
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica", 8)
    for link_line in [linkedin_url, "Portfolio: georgeleeh.com"]:
        for link_text_line in wrap_text(link_line, "Helvetica", 8, left_w - 10):
            pdf.drawString(left_x + 6, left_y, link_text_line)
            left_y -= 11
        left_y -= 2

    # Right column: timeline experience
    right_y = section_title("Experience Timeline", right_x, right_y, right_w)
    line_x = right_x + 8

    pdf.setStrokeColor(colors.HexColor("#93C5FD"))
    pdf.setLineWidth(1.2)
    pdf.line(line_x, right_y + 2, line_x, 56)

    for job in experience:
        estimated_height = 34
        for bullet in job["bullets"]:
            estimated_height += (len(wrap_text(bullet, "Helvetica", 9, right_w - 34)) * 11) + 3

        right_y = ensure_space(right_y, estimated_height + 14)

        pdf.setFillColor(accent)
        pdf.circle(line_x, right_y - 6, 2.5, stroke=0, fill=1)

        card_x = right_x + 16
        card_y_top = right_y
        card_h = estimated_height
        pdf.setFillColor(colors.HexColor("#F8FAFC"))
        pdf.roundRect(card_x, card_y_top - card_h + 10, right_w - 16, card_h, 8, stroke=0, fill=1)
        pdf.setStrokeColor(colors.HexColor("#E2E8F0"))
        pdf.setLineWidth(0.8)
        pdf.roundRect(card_x, card_y_top - card_h + 10, right_w - 16, card_h, 8, stroke=1, fill=0)

        pdf.setFillColor(ink)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(card_x + 10, card_y_top - 8, f"{job['role']} · {job['company']}")
        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(accent)
        pdf.drawString(card_x + 10, card_y_top - 21, job["period"])

        by = card_y_top - 34
        pdf.setFillColor(muted)
        pdf.setFont("Helvetica", 9)
        for bullet in job["bullets"]:
            wrapped = wrap_text(bullet, "Helvetica", 9, right_w - 34)
            for i, bullet_line in enumerate(wrapped):
                prefix = "• " if i == 0 else "  "
                pdf.drawString(card_x + 10, by, f"{prefix}{bullet_line}")
                by -= 11
            by -= 2
        right_y = card_y_top - card_h - 8

    pdf.save()
    buffer.seek(0)
    return buffer


@main_bp.route("/")
def home():
    return render_template(
        "index.html",
        profile=current_app.config["PROFILE"],
        skills=current_app.config["SKILLS"],
        highlights=current_app.config["KEY_HIGHLIGHTS"],
        featured_projects=current_app.config["PROJECTS"][:2],
    )


@main_bp.route("/resume")
def resume():
    return render_template(
        "resume.html",
        profile=current_app.config["PROFILE"],
        skills=current_app.config["SKILLS"],
        highlights=current_app.config["KEY_HIGHLIGHTS"],
        experience=current_app.config["EXPERIENCE"],
    )


@main_bp.route("/projects")
def projects():
    return render_template("projects.html", projects=current_app.config["PROJECTS"])


@main_bp.route("/contact")
def contact():
    return render_template("contact.html")


@main_bp.route("/resume/download")
def download_resume():
    pdf_buffer = _build_resume_pdf()
    filename = f"{current_app.config['PROFILE']['name'].replace(' ', '_')}_Resume.pdf"
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf",
    )
