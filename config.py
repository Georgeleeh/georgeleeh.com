import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SITE_TITLE = os.getenv("SITE_TITLE")
    CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
    LINKEDIN_URL = os.getenv("LINKEDIN_URL")
    AVAILABLE_FOR_WORK = True
    ANALYTICS_DB_PATH = os.getenv("ANALYTICS_DB_PATH")
    ANALYTICS_DASHBOARD_KEY = os.getenv("ANALYTICS_DASHBOARD_KEY", "")

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
                "<strong>The Challenge:</strong> Pinpoint needed to ingest millions of daily transactions from thousands of UK retail point-of-sale systems across the country, transforming messy, heterogeneous data into clean, analytics-ready datasets that feed their enterprise analytics platform.",
                "<strong>The Approach:</strong> I designed a serverless architecture that separates concerns by processing type. AWS Lambda handles lightweight, stateless transformations with near-instant scaling, while AWS ECS provides cost-efficient compute pools for heavier workloads that benefit from persistent state and longer execution times. Each component is containerized with Docker, enabling consistent development-to-production workflows.",
                "<strong>The Result:</strong> The system now processes billions of transactions daily with minimal operational overhead. By partitioning data in S3 using time-based and categorical keys, downstream consumers query only relevant data, slashing query costs and latency. Infrastructure is entirely codified in Terraform, meaning deployments are reproducible and disaster recovery takes minutes rather than days.",
                "<strong>Key Technical Decisions:</strong> Event-driven architecture triggers jobs in response to data arrival rather than on a fixed schedule, reducing unnecessary compute. Data validation occurs at each pipeline stage, catching problems early and preventing cascading failures. The modular Python ETL jobs are designed to be independent and recomposable, making it easy to add new transformations without disrupting existing workflows.",
            ],
        },
        {
            "name": "Pinpoint Data Warehouse Operations",
            "slug": "pinpoint-warehouse-operations",
            "description": "Warehouse operations across Redshift and PostgreSQL with Athena for ad-hoc querying, including schema design, transformation jobs, and data quality guardrails.",
            "stack": ["Amazon Redshift", "PostgreSQL", "Athena", "SQL", "Python", "S3"],
            "link": "#",
            "details": [
                "<strong>The Challenge:</strong> As Pinpoint scaled, the data warehouse became the critical path. Clients relied on reports with SLA guarantees, but query performance degraded as the warehouse grew and complexity increased. We needed a schema that could handle complex analytical queries at scale while maintaining data quality across transformations.",
                "<strong>The Approach:</strong> I designed a star schema in Amazon Redshift with carefully chosen distribution and sort keys to optimize the client-report queries that run daily. Facts and dimensions are denormalized strategically—not into a single flat table, but thoughtfully to balance query speed with storage efficiency. PostgreSQL serves as our metadata database, tracking which pipeline runs produced which data, enabling lineage tracking and audit compliance.",
                "<strong>The Result:</strong> Reports that previously took 15+ minutes now complete in seconds. Data quality improved dramatically through guardrails that validate constraints, detect statistical outliers, and flag incomplete periods before reports reach clients. When clients ask ad-hoc questions, Athena provides instant access to raw S3 data without impacting the warehouse.",
                "<strong>Key Technical Decisions:</strong> We chose Redshift's columnar storage and compression for analytics workflows, but keep frequently-accessed metadata in PostgreSQL's fast row-based structure. Distribution keys are chosen to co-locate facts with their dimensions, reducing shuffles during joins. Athena acts as a pressure relief valve—heavy exploratory queries run there while predictable reporting queries use the optimized warehouse.",
            ],
        },
        {
            "name": "Pinpoint Platform Reliability",
            "slug": "pinpoint-platform-reliability",
            "description": "Reliability-focused rebuild of pipelines and report generators that drove daily failures to almost zero while improving trust in decision-critical metrics for enterprise clients.",
            "stack": ["Python", "SQL", "Docker", "AWS ECS", "Observability"],
            "link": "#",
            "details": [
                "<strong>The Problem:</strong> When I joined Pinpoint, the data platform was experiencing multiple failures daily. Clients woke up to empty reports, store managers couldn't access critical metrics, and the team spent hours firefighting issues instead of building features. The code lacked observability, tests, and defensive patterns—a single malformed data record could cascade into a complete pipeline failure.",
                "<strong>The Mission:</strong> I undertook a comprehensive rebuild, not by rewriting everything at once, but by systematically refactoring the most critical paths. Each transformation job now validates its inputs, handles errors gracefully, and provides detailed structured logging. Retry logic distinguishes between transient failures (retry) and permanent ones (fail fast and alert). Report generators now anticipate edge cases: null values, missing dimensions, and inconsistent states.",
                "<strong>The Transformation:</strong> Daily failures dropped from multiple incidents to near-zero. More importantly, when something does fail, the team now has enough observability to diagnose it in minutes rather than hours. Clients regained confidence in their decision-critical metrics. New team members onboard faster because runbooks and incident response procedures are documented.",
                "<strong>The Lesson:</strong> This taught me that reliability isn't a feature—it's a mindset baked into architecture. It's choosing defensive programming patterns, writing tests for the paths that matter, and investing in observability even when everything works. The code isn't always the most elegant, but it's predictable and easy to debug.",
            ],
        },
        {
            "name": "Third-Party Data Feed Takeover & CPD Migration",
            "slug": "third-party-datafeed-cpd-migration",
            "description": "Led the transition from a third-party intermediary to direct delivery by replicating their Central Product Database logic, rebuilding smoothing/manipulation workflows, and integrating everything into Pinpoint's production datafeed infrastructure.",
            "stack": ["Python", "SQL", "Data Modeling", "ETL/ELT", "AWS", "Datafeed Operations"],
            "link": "#",
            "details": [
                "<strong>The Context:</strong> Retail Spotlight originally supplied data to a third-party partner who repackaged it and distributed it to downstream clients as part of a commercial agreement. After Retail Spotlight took over that partner, we needed to internalize the entire delivery capability without disrupting existing client contracts.",
                "<strong>The Core Challenge:</strong> Their output quality depended on a Central Product Database (CPD) plus bespoke manipulation and smoothing logic layered on top of our raw feeds. We could not simply copy tables; we had to faithfully reproduce transformation behavior so downstream clients saw continuity in both schema and business meaning.",
                "<strong>The Delivery Approach:</strong> I helped replicate the CPD structures, mapped transformation rules into maintainable pipeline logic, and implemented a scheduled load process aligned with client delivery windows. We validated parity by running side-by-side comparisons of old versus new outputs, reconciling differences at product, category, and aggregate levels before cutover.",
                "<strong>Integration & Operations:</strong> Instead of creating a one-off system, we integrated the new CPD-derived outputs into Pinpoint's existing datafeed infrastructure, including monitoring, retry behavior, and operational alerting. This reduced long-term maintenance risk and gave the team one consistent operational model for all feeds.",
                "<strong>Outcome:</strong> The takeover preserved client-facing continuity while removing intermediary dependency. Retail Spotlight gained direct control over transformation quality, release cadence, and support workflows, with a reproducible process for future feed onboarding and migration work.",
            ],
        },
        {
            "name": "Python Test Data Factory Framework",
            "slug": "python-test-data-factory-framework",
            "description": "Built a reusable sample data factory framework to generate valid, normalized test data in a few readable lines, dramatically improving unit test speed and maintainability.",
            "stack": ["Python", "pytest", "SQL", "Data Modeling", "Test Engineering"],
            "link": "#",
            "details": [
                "<strong>The Problem:</strong> Our test suites depended on large, heavily normalized schemas with many non-nullable columns. In most unit tests, only a few fields were actually relevant, but developers still had to manually populate many unrelated columns and dependent dimension tables just to get one valid row.",
                "<strong>The Goal:</strong> Make tests faster to write, easier to read, and less brittle by letting engineers specify only the values that matter to the scenario while automatically generating valid defaults everywhere else.",
                "<strong>The Approach:</strong> I created a framework of Python factory classes that understand table relationships and required fields. Tests can override known-important values (including values in related dimension tables) while the framework fills non-essential columns with deterministic dummy data that always satisfies constraints.",
                "<strong>Design Choices:</strong> Factories expose a concise API focused on intent (what is important for this test) rather than schema mechanics (how every foreign key and non-null column is populated). Builders compose across normalized tables so one call can produce a complete, valid graph of records.",
                "<strong>Outcome:</strong> Test setup shrank from verbose multi-table fixtures to a few clear lines, improving readability and onboarding for new developers. We reduced fixture noise, sped up authoring, and made unit tests more robust by standardizing how valid sample data is generated.",
            ],
        },
        {
            "name": "StarrySkyMaps Automation Platform",
            "slug": "starrymaps-automation",
            "description": "End-to-end order personalization platform for Etsy constellation posters with instant buyer portal access, Google location integration, automated poster rendering, approval workflow, Etsy order closure, and timed digital delivery.",
            "stack": ["Python", "Flask", "SQL", "Etsy API", "Google Maps API", "Email Automation"],
            "link": "https://etsy.com/shop/StarrySkyMaps",
            "details": [
                "<strong>The Genesis:</strong> I started StarrySkyMaps as a side project in 2018—a simple idea: personalized constellation maps showing what the stars looked like at a meaningful moment and place. The Etsy store became unexpectedly successful, but the process was a nightmare. Each order meant manually creating a custom poster, emailing proofs, waiting for feedback, and manually uploading files. In peak season (Valentine's Day, I ranked #1 in the 'Valentine's gifts' category), processing orders manually became the bottleneck.",
                "<strong>The Automation Challenge:</strong> I built a system that catches orders the moment they arrive via Etsy webhooks. The customer provides a location and date, the system validates the location using Google Maps API, renders a personalized constellation poster using astronomical calculations, and emails a preview. The customer approves in the portal. Once approved, the system automatically closes the order on Etsy and emails the final digital file on schedule. The entire workflow is invisible—customers experience instant service without knowing a robot orchestrated it.",
                "<strong>The Business Impact:</strong> What once took 1-2 hours of manual work per order now takes seconds of unattended processing time. This transformed StarrySkyMaps from a side gig requiring constant attention into something I could run sustainably alongside a full-time job. Customers love the instant experience, and the business ran continuously for 8 years and 4 months, generating meaningful income.",
                "<strong>The Technical Lesson:</strong> This project taught me that automation should be invisible by default. The customer doesn't see the Flask app, the database, or the poster renderer—they just see their order appear in their inbox faster than expected. It also taught me the power of integrating with existing platforms (Etsy's API, Google Maps, email services) rather than building everything from scratch.",
            ],
        },
        {
            "name": "ML Dissertation: Speech Intelligibility in Dysarthric Speakers",
            "slug": "ml-speech-intelligibility",
            "description": "Research project applying machine learning to create an objective measure of speech intelligibility, awarded a dissertation mark above 80%.",
            "stack": ["Machine Learning", "Python", "Signal Processing", "Research"],
            "link": "#",
            "download_url": "/dissertation/download",
            "details": [
                "<strong>The Problem:</strong> Speech-language pathologists have no objective measure of intelligibility in individuals with dysarthria. Current assessment relies on listener subjective judgment—inefficient, variable, and painful for the patient who watches the clinician struggle to understand them. Could machine learning provide an objective, quantifiable measure that updates as therapy progresses?",
                "<strong>The Research:</strong> I trained multiple machine learning models on speech samples from dysarthric speakers, extracting acoustic features like pitch, formants, and speech rate. Different approaches performed differently: neural networks captured complex patterns but were hard to interpret; simpler classifiers were more transparent but missed subtle acoustic variations.",
                "<strong>The Insight:</strong> The most successful approach combined signal processing intuition with machine learning. Rather than throwing raw audio at a model, I engineered meaningful acoustic features based on speech science literature, then let the ML find optimal combinations. This hybrid approach achieved strong predictive performance while remaining interpretable—clinicians can understand why the model made its predictions.",
                "<strong>The Impact:</strong> The dissertation achieved a mark above 80% and opened doors to accessible technology research. More importantly, it showed me how ML is most powerful when paired with domain expertise. A purely data-driven approach would fail here; understanding speech pathology was essential.",
            ],
        },
        {
            "name": "Portfolio Website",
            "slug": "portfolio-website",
            "description": "Personal portfolio site developed rapidly using AI tooling while maintaining clean, maintainable code architecture. Custom design system with PDF resume generation, mobile-responsive layouts, and modular Flask structure.",
            "stack": ["Python", "Flask", "ReportLab", "HTML/CSS", "JavaScript"],
            "link": "https://georgeleeh.com",
            "details": [
                "<strong>The Experiment:</strong> I built this portfolio site as a practical experiment in using AI for rapid development. Rather than defaulting to templates or frameworks, I worked with Claude to design a custom system from first principles, maintaining high code quality throughout.",
                "<strong>Design Philosophy:</strong> I rejected Bootstrap and built a custom dark design system that feels personal rather than generic. The color palette, typography, and components reflect my aesthetic while keeping the site fast and accessible. The layout prioritizes content hierarchy—each section reveals information progressively.",
                "<strong>Technical Highlights:</strong> The most complex feature is the PDF resume generator. It uses ReportLab to dynamically render a well-designed resume from the same data structure that powers the website. This means resume, website, and actual work experience stay in sync automatically. The layout algorithm handles text wrapping, multi-column sections, and careful spacing to maximize readability within a single page.",
                "<strong>Architecture:</strong> The site is structured as a clean Flask application where configuration lives separately from logic. Projects, experience, education, and skills are all defined in a central config file, then rendered dynamically into templates. This makes it easy to update content or add new sections without touching code.",
                "<strong>The Lesson:</strong> AI tooling genuinely accelerates development, but only when paired with clear architectural thinking. The site came together fast because I knew what I wanted before I started coding, and I reviewed every AI suggestion critically.",
            ],
        },
        {
            "name": "Hidden Bookshelf Door",
            "slug": "hidden-bookshelf-door",
            "description": "Custom-built hidden bookshelf door replacing a standard airing cupboard entrance. Designed from scratch using precise measurements, YouTube tutorials, and hands-on carpentry to create a functional and aesthetic solution.",
            "stack": ["Carpentry", "DIY", "Problem Solving", "Measuring & Planning"],
            "link": "#",
            "details": [
                "<strong>The Vision:</strong> My flat had an awkward airing cupboard door right in the main living space. Rather than hide it with something bland, I thought: what if it wasn't there at all? What if you could swing a bookshelf open to reveal the storage inside?",
                "<strong>The Planning Phase:</strong> I spent weeks researching hidden door mechanisms, studying pivot hinge systems, and understanding the structural requirements. An ordinary bookshelf door is front-heavy and unstable. To make it work, I needed to carefully distribute weight, use heavy-duty pivot hinges designed for exactly this application, and ensure the door balanced properly so it could swing smoothly without slamming.",
                "<strong>The Build:</strong> I measured the doorframe obsessively—clearances are unforgiving. I built a sturdy bookshelf structure reinforced to handle the weight of hundreds of books while serving as a moving door. The pivot hinges were positioned carefully to provide enough leverage while keeping the door hidden when closed. Every angle mattered; being even 2-3mm off would cause binding or gaps.",
                "<strong>The Problem-Solving:</strong> Real carpentry rarely matches theory. The wall wasn't perfectly plumb, the floor wasn't perfectly level. I had to adapt on the fly, creating shims and adjusting component placements. The door had to swing freely through a full range while looking like a normal bookshelf.",
                "<strong>The Payoff:</strong> It works beautifully. The door swings open smoothly, looks indistinguishable from a regular bookshelf when closed, and impresses everyone who discovers the secret. This project taught me that good engineering isn't just about software—it's about understanding constraints, planning meticulously, and solving problems as they appear.",
            ],
        },
        {
            "name": "Home Automation System",
            "slug": "home-automation",
            "description": "Invisible-by-design home automation built on Home Assistant, integrating sensors and devices across platforms with custom YAML and Python logic. Provides quality-of-life improvements that work naturally for anyone, whether they know the system exists or not.",
            "stack": ["Home Assistant", "Python", "YAML", "IoT", "Smart Home"],
            "link": "#",
            "details": [
                "<strong>The Philosophy:</strong> Most smart home systems fail because they're visible. You have to open an app, remember weird automations, or explain to guests how everything works. I wanted the opposite: a system so well-designed that anyone could live in the space and it would just work naturally.",
                "<strong>The Technical Foundation:</strong> Home Assistant provides the central hub that ties together devices from incompatible manufacturers and protocols. I built custom integrations in Python and YAML to bridge gaps—creating unified interfaces for devices that couldn't otherwise talk to each other.",
                "<strong>The Key Innovation:</strong> Wireless switches. Guests walk in and see normal light switches on the walls. They flip them. The lights turn on. They don't know those switches are battery-powered and wirelessly communicate with smart bulbs; from their perspective, they're using a house like any other house. This requires reliability—if the system fails, manual control must always work.",
                "<strong>The Smart Logic:</strong> Automations run silently in the background. Lighting adjusts based on time of day without any user action. Temperature responds to weather, time, and whether anyone's home. Presence detection uses multiple sensors (phones, network, cameras) so the system doesn't get confused by someone leaving one room and entering another.",
                "<strong>The Lesson:</strong> The best automation is invisible automation. Technical sophistication is useless if it creates friction. A home automation system should improve quality of life so seamlessly that inhabitants forget it's there.",
            ],
        },
        {
            "name": "Nissan Figaro Restoration & Maintenance",
            "slug": "nissan-figaro-restoration",
            "description": "Ongoing restoration and maintenance of a classic Nissan Figaro purchased in poor condition. Brought the car back to reliable daily use through mechanical repairs, component replacements, and hands-on problem diagnosis.",
            "stack": ["Automotive Repair", "Mechanical Engineering", "Problem Diagnosis", "Hands-on Work"],
            "link": "#",
            "details": [
                "<strong>The Project:</strong> I purchased a 1989 Nissan Figaro—a charming Japanese retro car—that hadn't run in years. It was a shell: seized engine, corroded fuel system, failing emissions, interior falling apart. Most people would take it to a mechanic. I decided to diagnose and fix it myself.",
                "<strong>The Diagnosis Phase:</strong> I approached it systematically. No spark, no fuel—classic non-start symptoms. The fuel system had two failing injectors that weren't atomizing fuel properly. The carburetor wasn't getting adequate pressure. I traced fuel delivery from tank to injector and found the culprit.",
                "<strong>The Teardown:</strong> Once I committed to fuel system repairs, more problems appeared. The rocker shaft was worn, leaking oil everywhere. Gaskets were cracked. I replaced not just what was immediately broken but everything that looked like it would fail soon. The exhaust system was beyond salvage—complete corrosion—so I replaced it entirely.",
                "<strong>The Learning Curve:</strong> Classic cars are mechanical systems where you can actually see how things work. You can trace fuel lines, understand ignition timing, and diagnose problems through first principles rather than plugging into a computer. Each repair taught me something about how cars actually function.",
                "<strong>The Payoff:</strong> The car now runs reliably and I've driven it hundreds of miles. It's not perfect—classic cars demand ongoing maintenance—but it's functional. More importantly, I developed skills that transfer directly to backend engineering: systematic diagnosis, building mental models of complex systems, and accepting that real-world systems are messier than diagrams suggest.",
            ],
        },
        {
            "name": "Boutique Guitar Pedal Builds (FuzzDog Kits)",
            "slug": "guitar-pedal-builds",
            "description": "Non-serious but deeply technical pedal-building workflow: start from FuzzDog kits, prototype and tune circuits on breadboard, then finish with custom powder-coated enclosures and self-designed decals.",
            "stack": ["Electronics", "Analog Circuits", "Breadboarding", "Soldering", "Powder Coating", "Graphic Design"],
            "link": "#",
            "details": [
                "<strong>The Hobby:</strong> I build custom guitar pedals for fun, usually starting with FuzzDog kits as a solid reference design. It scratches the same itch as software engineering: start with a known-good baseline, test assumptions, then iterate toward something that feels uniquely mine.",
                "<strong>The Engineering Process:</strong> Before committing to solder, I breadboard the circuit and audition component/value changes by ear and measurement. I tweak resistor and capacitor values, try different clipping diode combinations, and adjust gain/filter sections to shape the response for my playing style rather than sticking rigidly to the stock schematic.",
                "<strong>The Finishing Workflow:</strong> Once the circuit is dialed in, I move to enclosure work. I powder-coat the pedal housings myself, design original artwork/labels, print custom decals, and apply them before final assembly. The goal is a pedal that sounds personal and looks like a finished product, not a prototype.",
                "<strong>Why It Matters:</strong> It keeps my electronics fundamentals sharp—signal path reasoning, tolerance trade-offs, noise management, and practical debugging. It is intentionally non-serious, but it has made me better at disciplined experimentation and translating theory into tactile, working systems.",
            ],
        },
    ]
