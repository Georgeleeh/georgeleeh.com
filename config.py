import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-insecure-secret-change-me")
    SITE_TITLE = os.getenv("SITE_TITLE", "George Leeh | Portfolio")
    CONTACT_EMAIL = os.getenv("CONTACT_EMAIL", "hello@georgeleeh.com")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/georgeleeh")
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
        "Own data warehouse operations across Amazon Redshift and PostgreSQL for Pinpoint platform.",
        "Process daily EPOS data sourced from roughly one-third of systems across the UK.",
        "Redesigned pipelines/report generators and reduced daily failures to near zero.",
        "Deliver analytics trusted by major brands including Red Bull and Mondelez.",
    ]

    SKILLS = [
        "Python",
        "SQL",
        "Data Pipelines",
        "Data Warehousing",
        "Amazon Redshift",
        "PostgreSQL",
        "AWS (S3, Lambda, ECS, Athena)",
        "Terraform",
        "Docker",
        "Flask",
        "ETL / ELT",
        "Analytics Platform Engineering",
        "CI/CD",
        "Monitoring & Reliability",
    ]

    EXPERIENCE = [
        {
            "company": "Retail Spotlight",
            "role": "Backend Developer",
            "period": "2023 - Present",
            "bullets": [
                "Own Pinpoint data platform with Amazon Redshift for warehousing and PostgreSQL for config/operational metadata.",
                "Design and run daily delivery pipelines using AWS Lambda, ECS, and S3 to ingest EPOS data at UK national scale (roughly one-third of UK systems).",
                "Re-architected pipelines and report generators, cutting daily failures to near zero and improving operational confidence.",
                "Maintain Pinpoint analytics systems consumed by global brands (including Red Bull and Mondelez) and stock trading firms.",
                "Build reproducible, resilient workflows with Python, SQL, AWS (Lambda, ECS, S3, Athena), Docker, and Terraform.",
            ],
        },
        {
            "company": "Independent Projects",
            "role": "Backend Engineer",
            "period": "2020 - 2022",
            "bullets": [
                "Built Flask-based backend systems and tools for data processing and commerce-style workflows.",
                "Implemented SQL-first data models and APIs with a focus on maintainability and correctness.",
                "Containerized development/runtime environments to simplify setup and improve consistency.",
            ],
        },
    ]

    PROJECTS = [
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
