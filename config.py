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
                "Supported test and process reliability that contributed to exceptionally low product return rates.",
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
            "slug": "portfolio-website",
            "description": "Personal portfolio site developed rapidly using AI tooling while maintaining clean, maintainable code architecture. Custom design system with PDF resume generation, mobile-responsive layouts, and modular Flask structure.",
            "stack": ["Python", "Flask", "ReportLab", "HTML/CSS", "JavaScript"],
            "link": "https://georgeleeh.com",
            "details": [
                "Leveraged AI pair programming to accelerate development while maintaining code quality and architectural consistency.",
                "Built a custom dark-themed design system from scratch, removing Bootstrap dependency for a unique, performance-focused aesthetic.",
                "Implemented dynamic PDF resume generation using ReportLab with sophisticated layout algorithms for text wrapping, spacing, and multi-column design.",
                "Created a fully responsive mobile-first interface with custom navigation, timeline components, and skill visualization.",
                "Structured as a modular Flask application with separation of concerns: configuration, routes, templates, and static assets.",
                "Demonstrates practical application of modern web development practices while showcasing personality and technical breadth.",
            ],
        },
        {
            "name": "ML Dissertation: Speech Intelligibility in Dysarthric Speakers",
            "slug": "ml-speech-intelligibility",
            "description": "Research project applying machine learning to create an objective measure of speech intelligibility, awarded a dissertation mark above 80%.",
            "stack": ["Machine Learning", "Python", "Signal Processing", "Research"],
            "link": "#",
            "details": [
                "Developed machine learning models to objectively measure speech intelligibility in individuals with dysarthria.",
                "Applied signal processing techniques to extract acoustic features from speech samples.",
                "Conducted comprehensive literature review of existing assessment methods and their limitations.",
                "Trained and evaluated multiple ML approaches including neural networks and traditional classifiers.",
                "Achieved dissertation mark above 80%, demonstrating research rigor and technical execution.",
                "Contributed to the broader field of accessible technology and speech therapy assessment tools.",
            ],
        },
        {
            "name": "StarrySkyMaps Automation Platform",
            "slug": "starrymaps-automation",
            "description": "End-to-end order personalization platform for Etsy constellation posters with instant buyer portal access, Google location integration, automated poster rendering, approval workflow, Etsy order closure, and timed digital delivery.",
            "stack": ["Python", "Flask", "SQL", "Etsy API", "Google Maps API", "Email Automation"],
            "link": "https://etsy.com/shop/StarrySkyMaps",
            "details": [
                "Built an event-driven workflow system triggered by Etsy webhook events for new orders.",
                "Integrated Google Maps API to validate and geocode customer-provided locations automatically.",
                "Automated poster rendering pipeline that generates personalized constellation maps from astronomical data.",
                "Created secure buyer portal with instant email delivery, allowing customers to view drafts and provide feedback.",
                "Implemented approval workflow that automatically marks Etsy orders as complete and schedules digital delivery.",
                "Scaled to handle 8 years of continuous operation with peak performance during Valentine's season (ranked #1 Valentine's gifts category in 2021).",
                "Reduced manual intervention from hours per order to minutes, enabling sustainable solo operation of the business.",
            ],
        },
        {
            "name": "Pinpoint Data Delivery Pipelines",
            "slug": "pinpoint-data-pipelines",
            "description": "Daily ingestion and transformation pipelines using AWS Lambda, ECS, and S3, sourcing UK EPOS data at national scale and delivering clean, analytics-ready datasets.",
            "stack": ["Python", "SQL", "AWS Lambda", "AWS ECS", "S3", "Docker", "Terraform"],
            "link": "#",
            "details": [
                "Architected serverless data ingestion pipelines using AWS Lambda for lightweight transformations and ECS for compute-intensive processing.",
                "Processed UK Electronic Point of Sale (EPOS) data at national scale, handling millions of transactions daily.",
                "Built modular Python ETL jobs containerized with Docker and orchestrated through event-driven triggers.",
                "Implemented data validation and quality checks at each pipeline stage to ensure analytics-ready outputs.",
                "Managed infrastructure as code using Terraform for reproducible deployments and environment consistency.",
                "Designed S3 storage patterns with partitioning strategies for efficient querying and cost optimization.",
                "Delivered clean, transformed datasets to downstream consumers including data warehouse and analytics platforms.",
            ],
        },
        {
            "name": "Pinpoint Data Warehouse Operations",
            "slug": "pinpoint-warehouse-operations",
            "description": "Warehouse operations across Redshift and PostgreSQL with Athena for ad-hoc querying, including schema design, transformation jobs, and data quality guardrails.",
            "stack": ["Amazon Redshift", "PostgreSQL", "Athena", "SQL", "Python", "S3"],
            "link": "#",
            "details": [
                "Designed and maintained star schema data models in Amazon Redshift optimized for analytical query performance.",
                "Managed PostgreSQL metadata databases tracking pipeline state, data lineage, and operational metrics.",
                "Built transformation jobs that aggregate, denormalize, and enrich raw data for business intelligence consumption.",
                "Implemented data quality guardrails including constraint validation, outlier detection, and completeness checks.",
                "Configured AWS Athena for ad-hoc querying of S3 data lakes, enabling exploratory analysis without warehouse impact.",
                "Optimized query performance through distribution keys, sort keys, and compression encoding strategies.",
                "Maintained documentation of schema evolution, data dictionaries, and transformation logic for cross-team collaboration.",
            ],
        },
        {
            "name": "Pinpoint Platform Reliability",
            "slug": "pinpoint-platform-reliability",
            "description": "Reliability-focused rebuild of pipelines and report generators that drove daily failures to almost zero while improving trust in decision-critical metrics for enterprise clients.",
            "stack": ["Python", "SQL", "Docker", "AWS ECS", "Observability"],
            "link": "#",
            "details": [
                "Led comprehensive rebuild of data pipelines that were experiencing frequent daily failures impacting client trust.",
                "Implemented robust error handling, retry logic, and graceful degradation patterns throughout the processing pipeline.",
                "Added structured logging and observability instrumentation to enable rapid diagnosis of failures.",
                "Refactored report generation logic to handle edge cases, null values, and data inconsistencies reliably.",
                "Introduced automated testing covering critical data transformation paths and business logic.",
                "Reduced daily pipeline failures from multiple occurrences to near-zero, restoring confidence in decision-critical metrics.",
                "Documented operational runbooks and incident response procedures for sustainable reliability.",
            ],
        },
        {
            "name": "Hidden Bookshelf Door",
            "slug": "hidden-bookshelf-door",
            "description": "Custom-built hidden bookshelf door replacing a standard airing cupboard entrance. Designed from scratch using precise measurements, YouTube tutorials, and hands-on carpentry to create a functional and aesthetic solution.",
            "stack": ["Carpentry", "DIY", "Problem Solving", "Measuring & Planning"],
            "link": "#",
            "details": [
                "Removed existing airing cupboard door and assessed structural requirements for a pivot-hinge bookshelf door.",
                "Researched hidden door mechanisms and hinge systems through YouTube tutorials and online resources.",
                "Created custom templates and precise measurements specific to the flat's dimensions and door frame.",
                "Sourced appropriate hinges and hardware online, selecting components based on weight capacity and swing clearance.",
                "Built bookshelf structure from scratch with consideration for book weight distribution and door balance.",
                "Installed and calibrated the door to ensure smooth operation while maintaining the appearance of a standard bookshelf.",
                "Applied hands-on problem-solving throughout to handle unexpected challenges like wall alignment and clearance issues.",
            ],
        },
        {
            "name": "Home Automation System",
            "slug": "home-automation",
            "description": "Invisible-by-design home automation built on Home Assistant, integrating sensors and devices across platforms with custom YAML and Python logic. Provides quality-of-life improvements that work naturally for anyone, whether they know the system exists or not.",
            "stack": ["Home Assistant", "Python", "YAML", "IoT", "Smart Home"],
            "link": "#",
            "details": [
                "Built unified smart home system using Home Assistant as the central hub, integrating devices from multiple manufacturers and protocols.",
                "Developed custom integrations and automations in YAML and Python to bridge incompatible platforms and add missing functionality.",
                "Designed automation logic prioritizing invisibility and natural interaction—guests use the home normally without knowing smart features exist.",
                "Implemented battery-powered wireless switches that appear and function as traditional light switches while secretly controlling smart bulbs.",
                "Created context-aware automations that adjust lighting, temperature, and other parameters based on time, presence, and usage patterns.",
                "Maintained system reliability and graceful degradation so that manual control always works even if automation fails.",
                "Balanced technical sophistication with user experience simplicity, ensuring quality-of-life improvements don't require technical knowledge.",
            ],
        },
    ]
