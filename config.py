import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SITE_TITLE = os.getenv("SITE_TITLE")
    CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
    LINKEDIN_URL = os.getenv("LINKEDIN_URL")

    PROFILE = {
        "name": "George Harris",
        "title": "Backend Developer · Data Platform & Analytics",
        "location": "Portsmouth, UK / Remote or Hybrid",
        "summary": (
            "Backend Developer at Retail Spotlight (Jan 2023 - Present) specializing in data-intensive backend systems. "
            "I manage warehousing architecture, build production data delivery pipelines, and maintain the Pinpoint "
            "analytics platform for enterprise clients using Python, SQL, AWS (S3, Lambda, ECS, Athena), Docker, and Terraform. "
            "Working in a small, fast-moving team with direct customer interaction and production ownership."
        ),
    }

    KEY_HIGHLIGHTS = [
        "Manage backend development and data warehouse operations on Amazon Redshift and PostgreSQL for the Pinpoint analytics platform.",
        "Process billions of transactions daily across millions of products from thousands of individual EPOS systems and batch data providers.",
        "Maintain terabytes of active warehouse storage with deep archival storage for historical analysis.",
        "Work in small startup team with direct production ownership, customer interaction, and cross-functional collaboration.",
        "Re-architected critical pipelines and report generators, reducing daily production failures to near-zero.",
        "Founded and scaled StarrySkyMaps on Etsy for 8 years, achieving #1 ranking in Valentine's gifts category (2021).",
    ]

    SKILLS = [
        "Python",
        "SQL",
        "AWS (S3, Lambda, ECS, Athena)",
        "Amazon Redshift",
        "PostgreSQL",
        "Docker",
        "Terraform",
        "Data Pipelines",
        "pandas",
        "ETL / ELT",
        "Data Warehousing",
        "boto3",
        "NumPy",
        "pytest",
        "Grafana",
        "Git / Version Control",
        "Bitbucket / CI/CD",
        "Monitoring & Observability",
        "Analytics Platform Engineering",
        "Flask",
        "SciPy",
        "Machine Learning",
        "API Integration",
        "Workflow Automation",
        "Hardware Test Automation",
        "Raspberry Pi",
    ]

    EXPERIENCE = [
        {
            "company": "Retail Spotlight",
            "role": "Backend Developer",
            "period": "Jan 2023 - Present",
            "bullets": [
                "Manage backend development for the Pinpoint analytics platform, utilizing Amazon Redshift for data warehousing and PostgreSQL for configuration and operational metadata.",
                "Architect and maintain batch data pipelines processing billions of transactions daily across millions of products from thousands of individual EPOS systems.",
                "Work autonomously in small startup team environment with direct production ownership, customer interaction, and requirement gathering from enterprise clients.",
                "Collaborate with internal data and analytics teams to develop tooling, respond to bug reports, and deliver customer-facing solutions.",
                "Maintain terabytes of active warehouse storage with deep archival infrastructure for historical analysis.",
                "Re-architected critical pipelines and report generators, reducing daily production failures from frequent occurrences to near-zero.",
                "Migrated legacy Node.js data parser to version-controlled Python, improving performance, operational visibility, and cost efficiency.",
                "Design and maintain Grafana dashboards for production monitoring, pipeline health tracking, and performance optimization.",
                "Regularly present technical concepts to cross-functional teams, including data development processes and raw data structures.",
                "Implement production-grade workflows using Python (pandas, NumPy, SciPy, pytest), SQL, AWS services (boto3), Docker, Terraform, and Bitbucket CI/CD.",
            ],
        },
        {
            "company": "The Petersfield School",
            "role": "Teacher of Mathematics & Computer Science",
            "period": "Sep 2022 - Jan 2023",
            "bullets": [
                "Delivered Mathematics and Computer Science curriculum with structured lesson planning, formative assessment, and differentiated instruction.",
                "Used practical programming examples to teach computational thinking, algorithm design, and problem decomposition.",
                "Recognized for leadership potential and offered Head of IT position prior to returning to software engineering.",
                "Developed communication skills translating complex technical concepts for varied audiences.",
            ],
        },
        {
            "company": "StarrySkyMaps (Etsy)",
            "role": "Founder / Software Engineer",
            "period": "2018 - Present",
            "bullets": [
                "Founded and operated Etsy store for 8 years selling algorithmically-generated constellation posters, scaling to #1 in Valentine's gifts category (2021).",
                "Designed custom database and API layer extending Etsy's personalization capabilities beyond single free-text inputs.",
                "Built self-service buyer portal with Google Maps API integration for location validation and instant customer access via transactional email.",
                "Engineered event-driven fulfillment workflow orchestrating poster generation, approval workflows, Etsy order updates, and automated customer notifications.",
                "Implemented secure asset delivery system with time-bound download access and automated lifecycle management.",
                "Reduced order processing time from hours to minutes through end-to-end automation, enabling sustainable solo operation.",
                "Presented business and technical case studies demonstrating entrepreneurial software engineering.",
            ],
        },
        {
            "company": "Focusrite",
            "role": "Production Engineer Intern",
            "period": "Aug 2019 - Aug 2020",
            "bullets": [
                "Managed factory communications and Bill of Materials (BOM) coordination supporting production of professional audio hardware.",
                "Developed automated hardware test suites using Focusrite's PyFactory platform deployed on Raspberry Pi hardware in East Asian manufacturing facilities.",
                "Enabled remote test deployment and real-time monitoring across international factory lines, improving quality control responsiveness.",
                "Contributed to production reliability initiatives that maintained exceptionally low product return rates (sub-0.5%).",
                "Built test solutions for touch-sensitive MIDI controller devices requiring precise calibration and validation.",
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
                "Graduated with 2:1 classification (Upper Second-Class Honours).",
                "Specialized in Machine Learning and Biologically Inspired Computing.",
                "Dissertation: 'Using Machine Learning to Provide an Objective Measure of Speech Intelligibility in Dysarthric Speakers' (First Class, 80%+).",
                "Advanced coursework in robotics, real-time audio signal processing, weather telemetry sonification, and mobile application sentiment analysis.",
            ],
        },
    ]

    PROJECTS = [
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
        {
            "name": "Nissan Figaro Restoration & Maintenance",
            "slug": "nissan-figaro-restoration",
            "description": "Ongoing restoration and maintenance of a classic Nissan Figaro purchased in poor condition. Brought the car back to reliable daily use through mechanical repairs, component replacements, and hands-on problem diagnosis.",
            "stack": ["Automotive Repair", "Mechanical Engineering", "Problem Diagnosis", "Hands-on Work"],
            "link": "#",
            "details": [
                "Purchased Nissan Figaro in non-running condition and systematically diagnosed engine and fuel system issues.",
                "Replaced two fuel injectors after identifying fuel delivery problems affecting engine performance.",
                "Replaced rocker shaft and multiple gaskets to resolve oil leaks and improve engine reliability.",
                "Installed complete exhaust system replacement to address corrosion and emissions issues.",
                "Sourced and fitted replacement seats to restore interior comfort and aesthetics.",
                "Successfully brought the car to reliable running condition and driven hundreds of miles since repairs.",
                "Developed mechanical troubleshooting skills and hands-on experience with classic car systems through iterative problem-solving.",
            ],
        },
    ]
