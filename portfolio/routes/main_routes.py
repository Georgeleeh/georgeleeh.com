from io import BytesIO

from flask import Blueprint, current_app, make_response, render_template, send_file, url_for
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

main_bp = Blueprint("main", __name__)


def _build_resume_pdf() -> BytesIO:
    profile = current_app.config["PROFILE"]
    highlights = current_app.config["KEY_HIGHLIGHTS"]
    experience = current_app.config["EXPERIENCE"]
    education = current_app.config["EDUCATION"]
    skills = current_app.config["SKILLS"]
    contact_email = current_app.config["CONTACT_EMAIL"]

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    margin = 40
    y = height - margin

    bg = colors.HexColor("#FFFFFF")
    panel = colors.HexColor("#EEF2FF")
    panel_soft = colors.HexColor("#F8FAFC")
    text = colors.HexColor("#0F172A")
    muted = colors.HexColor("#475569")
    accent = colors.HexColor("#1D4ED8")
    accent_alt = colors.HexColor("#7C3AED")
    line_color = colors.HexColor("#CBD5E1")

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
        pdf.setFillColor(text)
        pdf.setFont("Helvetica-Bold", 12)
        title_x = x_pos + 9
        pdf.drawString(title_x, y_pos, title_text)
        pdf.setStrokeColor(accent_alt)
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
        pdf.setFillColor(bg)
        pdf.rect(0, 0, width, height, stroke=0, fill=1)
        pdf.setFillColor(panel)
        pdf.rect(0, height - 66, width, 66, stroke=0, fill=1)
        pdf.setFillColor(accent)
        pdf.rect(0, height - 66, 10, 66, stroke=0, fill=1)
        pdf.setFillColor(accent_alt)
        pdf.rect(10, height - 66, 4, 66, stroke=0, fill=1)

        pdf.setFillColor(text)
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(margin, height - 36, profile["name"])
        pdf.setFont("Helvetica", 10)
        pdf.setFillColor(muted)
        pdf.drawString(margin, height - 52, f"{profile['title']} · {profile['location']}")

        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(text)
        pdf.drawRightString(width - margin, height - 36, contact_email)
        pdf.setFillColor(accent)
        pdf.drawRightString(width - margin, height - 50, "georgeleeh.com")

        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.9)
        pdf.line(margin, 36, width - margin, 36)
        pdf.setFont("Helvetica", 8)
        pdf.setFillColor(muted)
        pdf.drawString(margin, 24, "Resume generated from live portfolio data")
        pdf.drawRightString(width - margin, 24, "linkedin.com/in/george-leeh")

    draw_page_chrome()
    y = height - 80

    # Key Highlights section
    y = section_title("Key Highlights", margin, y, width - (margin * 2))
    pdf.setFillColor(muted)
    pdf.setFont("Helvetica", 10)
    for item in highlights:
        wrapped = wrap_text(item, "Helvetica", 10, width - (margin * 2) - 16)
        for i, line in enumerate(wrapped):
            y = ensure_space(y, 14)
            bullet = "• " if i == 0 else "  "
            pdf.drawString(margin + 8, y, f"{bullet}{line}")
            y -= 13
        y -= 4
    y -= 12

    # Experience section
    y = section_title("Experience", margin, y, width - (margin * 2))
    for job in experience:
        # Estimate height needed for this job entry
        card_text_w = width - (margin * 2) - 32
        estimated_height = 40
        for bullet in job["bullets"]:
            estimated_height += (len(wrap_text(bullet, "Helvetica", 9, card_text_w)) * 12) + 3
        
        y = ensure_space(y, estimated_height + 8)

        card_x = margin + 2
        card_w = width - (margin * 2) - 4
        pdf.setFillColor(panel_soft)
        pdf.roundRect(card_x, y - estimated_height + 8, card_w, estimated_height, 8, stroke=0, fill=1)
        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.8)
        pdf.roundRect(card_x, y - estimated_height + 8, card_w, estimated_height, 8, stroke=1, fill=0)

        line_y = y - 12
        
        # Job header
        pdf.setFillColor(text)
        pdf.setFont("Helvetica-Bold", 11)
        job_title = f"{job['role']} · {job['company']}"
        pdf.drawString(card_x + 10, line_y, job_title)
        
        # Period on the same line, right-aligned
        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(accent)
        period_width = pdf.stringWidth(job["period"], "Helvetica", 9)
        pdf.drawString(card_x + card_w - period_width - 10, line_y, job["period"])
        line_y -= 16
        
        # Job bullets
        pdf.setFillColor(muted)
        pdf.setFont("Helvetica", 9)
        for bullet in job["bullets"]:
            wrapped = wrap_text(bullet, "Helvetica", 9, card_text_w)
            for i, bullet_line in enumerate(wrapped):
                prefix = "• " if i == 0 else "  "
                pdf.drawString(card_x + 18, line_y, f"{prefix}{bullet_line}")
                line_y -= 12
            line_y -= 2
        y -= estimated_height + 10
    
    y -= 8

    # Skills section
    y = section_title("Skills", margin, y, width - (margin * 2))
    y = ensure_space(y, 80)
    
    pill_x = margin + 8
    pill_y = y
    row_height = 18
    
    for skill in skills:
        label = skill if len(skill) <= 30 else f"{skill[:27]}..."
        pill_w = pdf.stringWidth(label, "Helvetica", 9) + 16
        
        # Check if we need to wrap to next line
        if pill_x + pill_w > width - margin - 8:
            pill_x = margin + 8
            pill_y -= row_height
            y = ensure_space(pill_y, row_height)
            if y != pill_y:
                pill_y = y
        
        # Draw pill background
        pdf.setFillColor(panel_soft)
        pdf.roundRect(pill_x, pill_y - 10, pill_w, 14, 6, stroke=0, fill=1)
        
        # Draw pill border
        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.6)
        pdf.roundRect(pill_x, pill_y - 10, pill_w, 14, 6, stroke=1, fill=0)
        
        # Draw skill text
        pdf.setFillColor(text)
        pdf.setFont("Helvetica", 9)
        pdf.drawString(pill_x + 8, pill_y - 5, label)
        
        pill_x += pill_w + 6
    
    y = pill_y - 24

    # Education section
    y = section_title("Education & Qualifications", margin, y, width - (margin * 2))
    for item in education:
        period_width = pdf.stringWidth(item["period"], "Helvetica", 9)
        card_text_w = width - (margin * 2) - 32

        card_w = width - (margin * 2) - 4
        qualification_w = max(160, card_w - period_width - 44)
        qualification_lines = wrap_text(item["qualification"], "Helvetica-Bold", 11, qualification_w)
        institution_lines = wrap_text(item["institution"], "Helvetica-Oblique", 9, card_text_w)

        # Estimate height needed
        estimated_height = 22
        estimated_height += len(qualification_lines) * 13
        estimated_height += 3
        estimated_height += len(institution_lines) * 11
        estimated_height += 4
        if item.get("notes"):
            for note in item["notes"]:
                estimated_height += (len(wrap_text(note, "Helvetica", 9, card_text_w)) * 12) + 2
        
        y = ensure_space(y, estimated_height + 8)

        card_x = margin + 2
        pdf.setFillColor(panel_soft)
        pdf.roundRect(card_x, y - estimated_height + 8, card_w, estimated_height, 8, stroke=0, fill=1)
        pdf.setStrokeColor(line_color)
        pdf.setLineWidth(0.8)
        pdf.roundRect(card_x, y - estimated_height + 8, card_w, estimated_height, 8, stroke=1, fill=0)

        line_y = y - 12
        
        # Qualification header
        pdf.setFillColor(text)
        pdf.setFont("Helvetica-Bold", 11)
        for q_line in qualification_lines:
            pdf.drawString(card_x + 10, line_y, q_line)
            line_y -= 13
        
        # Period on the same line, right-aligned
        pdf.setFont("Helvetica", 9)
        pdf.setFillColor(accent)
        pdf.drawString(card_x + card_w - period_width - 10, y - 12, item["period"])
        line_y -= 2
        
        # Institution
        pdf.setFillColor(muted)
        pdf.setFont("Helvetica-Oblique", 9)
        for institution_line in institution_lines:
            pdf.drawString(card_x + 18, line_y, institution_line)
            line_y -= 11
        line_y -= 3
        
        # Notes
        if item.get("notes"):
            pdf.setFont("Helvetica", 9)
            for note in item["notes"]:
                wrapped = wrap_text(note, "Helvetica", 9, card_text_w)
                for i, note_line in enumerate(wrapped):
                    prefix = "• " if i == 0 else "  "
                    pdf.drawString(card_x + 18, line_y, f"{prefix}{note_line}")
                    line_y -= 12
                line_y -= 2
        y -= estimated_height + 10
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
        available_for_work=current_app.config.get("AVAILABLE_FOR_WORK", False),
    )


@main_bp.route("/resume")
def resume():
    return render_template(
        "resume.html",
        profile=current_app.config["PROFILE"],
        skills=current_app.config["SKILLS"],
        highlights=current_app.config["KEY_HIGHLIGHTS"],
        experience=current_app.config["EXPERIENCE"],
        education=current_app.config["EDUCATION"],
    )


@main_bp.route("/projects")
def projects():
    return render_template("projects.html", projects=current_app.config["PROJECTS"])


@main_bp.route("/projects/<slug>")
def project_detail(slug):
    all_projects = current_app.config["PROJECTS"]
    project = next((p for p in all_projects if p.get("slug") == slug), None)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)


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


@main_bp.route("/dissertation/download")
def download_dissertation():
    return send_file(
        "static/data/Final Dissertation.pdf",
        as_attachment=True,
        download_name="George_Harris_ML_Dissertation_Speech_Intelligibility.pdf",
        mimetype="application/pdf",
    )


@main_bp.route("/sitemap.xml")
def sitemap():
    pages = [
        {"loc": url_for("main.home", _external=True), "priority": "1.0"},
        {"loc": url_for("main.resume", _external=True), "priority": "0.9"},
        {"loc": url_for("main.projects", _external=True), "priority": "0.8"},
        {"loc": url_for("main.contact", _external=True), "priority": "0.7"},
    ]
    
    # Add project detail pages
    for project in current_app.config["PROJECTS"]:
        pages.append({
            "loc": url_for("main.project_detail", slug=project["slug"], _external=True),
            "priority": "0.6"
        })
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        sitemap_xml += '  <url>\n'
        sitemap_xml += f'    <loc>{page["loc"]}</loc>\n'
        sitemap_xml += f'    <priority>{page["priority"]}</priority>\n'
        sitemap_xml += '  </url>\n'
    sitemap_xml += '</urlset>'
    
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@main_bp.route("/robots.txt")
def robots():
    robots_txt = f"""User-agent: *\nAllow: /\n\nSitemap: {url_for('main.sitemap', _external=True)}"""
    response = make_response(robots_txt)
    response.headers["Content-Type"] = "text/plain"
    return response
