import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-insecure-secret-change-me")
    SITE_TITLE = os.getenv("SITE_TITLE", "George Leeh | Portfolio")
    CONTACT_EMAIL = os.getenv("CONTACT_EMAIL", "jobs@georgeleeh.com")
    LINKEDIN_URL = os.getenv("LINKEDIN_URL", "https://www.linkedin.com")

    PROFILE = {
        "name": "George Harris",
        "title": "Backend Developer · Data Platform & Analytics",
        "location": "Portsmouth, UK / Remote",
        "summary": (
            "Backend Developer at Retail Spotlight (Jan 2023 - Present) specializing in data-intensive backend systems. "
            "I manage warehousing architecture, build production data delivery pipelines, and maintain the Pinpoint "
            "analytics platform for enterprise clients using Python, SQL, AWS (S3, Lambda, ECS, Athena), Docker, and Terraform."
        ),
    }

    KEY_HIGHLIGHTS = [
        "Contribute to backend development and warehouse operations across Amazon Redshift and PostgreSQL for the Pinpoint platform.",
        "Process daily EPOS data sourced from roughly one-third of systems across the UK.",
        "Redesigned pipelines/report generators and reduced daily failures to near zero.",
        "Founder of StarrySkyMaps on Etsy (8 years), ranked #1 in Valentine's gifts in 2021.",
        "Deliver analytics trusted by major brands including Red Bull and Mondelez.",
    ]

    SKILLS = [
        "Python",
        "SQL",
        "Machine Learning",
        "Data Pipelines",
        "Data Warehousing",
        "Amazon Redshift",
        "PostgreSQL",
        "AWS (S3, Lambda, ECS, Athena)",
        "Terraform",
        "Docker",
        "Raspberry Pi",
        "Hardware Test Automation",
        "BOM Management",
        "Flask",
        "Etsy API Integrations",
        "Google Maps API",
        "Workflow Automation",
        "ETL / ELT",
        "Analytics Platform Engineering",
        "CI/CD",
        "Monitoring & Reliability",
    ]

    EXPERIENCE = [
        {
            "company": "Retail Spotlight",
            "role": "Backend Developer",
            "period": "Jan 2023 - Present",
            "bullets": [
                "Contribute to the Pinpoint backend platform, working with Amazon Redshift for warehousing and PostgreSQL for configuration and operational metadata.",
                "Design and run daily delivery pipelines using AWS Lambda, ECS, and S3 to ingest EPOS data at UK national scale (roughly one-third of UK systems).",
                "Re-architected pipelines and report generators, cutting daily failures to near zero and improving operational confidence.",
                "Maintain Pinpoint analytics systems consumed by global brands (including Red Bull and Mondelez) and stock trading firms.",
                "Build reproducible, resilient workflows with Python, SQL, AWS (Lambda, ECS, S3, Athena), Docker, and Terraform.",
            ],
        },
        {
            "company": "The Petersfield School",
            "role": "Teacher of Mathematics & Computer Science",
            "period": "Sep 2022 - Jan 2023",
            "bullets": [
                "Delivered Mathematics and Computer Science lessons with structured planning, assessment, and targeted feedback.",
                "Used practical programming examples to teach computational thinking and problem decomposition.",
                "Recognized for leadership potential and offered the position of Head of IT prior to returning to industry engineering work.",
            ],
        },
        {
            "company": "StarrySkyMaps (Etsy)",
            "role": "Founder / Backend Engineer",
            "period": "2018 - Present",
            "bullets": [
                "Built and operated an Etsy store for 8 years selling code-generated constellation posters, originally created as a personal gift idea.",
                "Scaled the store to #1 in Valentine's gifts on Etsy in 2021 through product automation and customer-focused personalization.",
                "Designed a custom database and API layer to extend Etsy's limited personalization options beyond a single free-text input.",
                "Built a self-hosted buyer portal where customers receive an instant email link, submit validated form data, and use Google API-powered location lookup.",
                "Engineered an event-driven fulfillment workflow that orchestrates poster rendering, approval state transitions, Etsy order status updates, and transactional customer notifications.",
                "Implemented secure, time-bound asset delivery with expiring download access, persistence controls, and automated lifecycle handling for generated poster files.",
            ],
        },
        {
            "company": "Focusrite",
            "role": "Production Engineer Intern",
            "period": "Aug 2019 - Aug 2020",
            "bullets": [
                "Owned factory communications and BOM management to support stable production of music-technology hardware.",
                "Developed hardware test suites in Focusrite's custom PyFactory platform running on Raspberry Pis deployed in East Asia.",
                "Enabled remote test updates and monitoring across factory lines, improving responsiveness and production quality control.",
                "Supported test and process reliability that contributed to product return rates below 0.5%.",
                "Built hardware test solutions for touch-sensitive MIDI devices.",
            ],
        },
    ]

    EDUCATION = [
        {
            "institution": "University of Portsmouth & The Petersfield School",
            "qualification": "PGCE with QTS (Qualified Teacher Status)",
            "period": "Sep 2021 - July 2022",
            "notes": [
                "Postgraduate teacher training pathway with school-based practice in Mathematics and Computer Science.",
            ],
        },
        {
            "institution": "University of Portsmouth",
            "qualification": "MEng Electronic Engineering with Music Technology Systems",
            "period": "Sep 2017 - Jul 2021",
            "notes": [
                "Graduated with a 2:1 classification.",
                "Specialized in Machine Learning and Biologically Inspired Computing.",
                "Dissertation: 'Using Machine Learning to Provide an Objective Measure of Speech Intelligibility in Dysarthric Speakers' (80%+).",
                "Additional advanced work included robotics, sonification of weather telemetry, real-time audio signal analysis, and sentiment analysis in mobile applications.",
            ],
        },
    ]

    PROJECTS = [
        {
            "name": "Portfolio Website",
            "description": "Personal portfolio site developed rapidly using AI tooling while maintaining clean, maintainable code architecture. Custom design system with PDF resume generation, mobile-responsive layouts, and modular Flask structure.",
            "stack": ["Python", "Flask", "ReportLab", "HTML/CSS", "JavaScript"],
            "link": "https://georgeleeh.com",
        },
        {
            "name": "ML Dissertation: Speech Intelligibility in Dysarthric Speakers",
            "description": "Research project applying machine learning to create an objective measure of speech intelligibility, awarded a dissertation mark above 80%.",
            "stack": ["Machine Learning", "Python", "Signal Processing", "Research"],
            "link": "#",
        },
        {
            "name": "StarrySkyMaps Automation Platform",
            "description": "End-to-end order personalization platform for Etsy constellation posters with instant buyer portal access, Google location integration, automated poster rendering, approval workflow, Etsy order closure, and timed digital delivery.",
            "stack": ["Python", "Flask", "SQL", "Etsy API", "Google Maps API", "Email Automation"],
            "link": "https://etsy.com/shop/StarrySkyMaps",
        },
        {
            "name": "Pinpoint Data Delivery Pipelines",
            "description": "Daily ingestion and transformation pipelines using AWS Lambda, ECS, and S3, sourcing UK EPOS data at national scale and delivering clean, analytics-ready datasets.",
            "stack": ["Python", "SQL", "AWS Lambda", "AWS ECS", "S3", "Docker", "Terraform"],
            "link": "#",
        },
        {
            "name": "Pinpoint Data Warehouse Operations",
            "description": "Warehouse operations across Redshift and PostgreSQL with Athena for ad-hoc querying, including schema design, transformation jobs, and data quality guardrails.",
            "stack": ["Amazon Redshift", "PostgreSQL", "Athena", "SQL", "Python", "S3"],
            "link": "#",
        },
        {
            "name": "Pinpoint Platform Reliability",
            "description": "Reliability-focused rebuild of pipelines and report generators that drove daily failures to almost zero while improving trust in decision-critical metrics for enterprise clients.",
            "stack": ["Python", "SQL", "Docker", "AWS ECS", "Observability"],
            "link": "#",
        },
    ]
