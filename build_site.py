import json

verification_sample = [
    {
        "id": 1,
        "app": "Salesforce",
        "category": "CRM and Sales",
        "initial_claim": "Self-serve: No (Requires paid corporate Salesforce org). Buildability: Medium.",
        "real_docs": "Salesforce provides a permanent, free Developer Edition org at developer.salesforce.com/signup with full REST/GraphQL/SOAP APIs and Connected App support.",
        "status": "Corrected",
        "verdict": "High (via Free Dev Org)",
        "lesson": "Agents overlook non-commercial developer programs and assume pricing page restrictions apply to sandbox APIs."
    },
    {
        "id": 2,
        "app": "HubSpot",
        "category": "CRM and Sales",
        "initial_claim": "OAuth2 & Private App Tokens. Self-serve: Yes. MCP: Community/Official. Buildability: High.",
        "real_docs": "Confirmed. Private app tokens generate in 3 clicks in Settings -> Integrations -> Private Apps. Free CRM tier available indefinitely.",
        "status": "Verified Hit",
        "verdict": "High",
        "lesson": "Gold-standard developer experience; agent easily extracted exact scopes and token models."
    },
    {
        "id": 28,
        "app": "WhatsApp Business",
        "category": "Communications and Messaging",
        "initial_claim": "Self-serve: Yes. API Key available immediately. Buildability: High.",
        "real_docs": "Meta Cloud API provides test numbers in developer portal, but live business production requires official Meta Business verification, display name review, and payment method.",
        "status": "Corrected",
        "verdict": "Medium (Production Gate)",
        "lesson": "Sandbox accessibility gave a false-positive signal for self-serve production readiness."
    },
    {
        "id": 31,
        "app": "Google Ads",
        "category": "Marketing, Ads, Email and Social",
        "initial_claim": "OAuth2. Self-serve: Yes. Standard REST API. Buildability: High.",
        "real_docs": "Test accounts work with basic developer token, but standard access to query live ad accounts requires a detailed application form and manual Google compliance approval.",
        "status": "Corrected",
        "verdict": "Medium (Developer Token Review)",
        "lesson": "Multi-tier developer credentialing is common in ad networks to curb fraud; agent missed the token tiering."
    },
    {
        "id": 56,
        "app": "Firecrawl",
        "category": "Data, SEO and Scraping",
        "initial_claim": "API Key. REST API. Instant self-serve with free credit tier. Buildability: High.",
        "real_docs": "Confirmed. Open-source or hosted; sign up with GitHub/Google, instant key, documented cURL examples.",
        "status": "Verified Hit",
        "verdict": "High",
        "lesson": "AI-native tooling built in the last 24 months almost universally adheres to frictionless API key onboarding."
    },
    {
        "id": 60,
        "app": "Clay",
        "category": "Data, SEO and Scraping",
        "initial_claim": "Public REST API available. Self-serve: Yes.",
        "real_docs": "Clay is a UI-first spreadsheet/workflow platform. While it supports webhooks and HTTP enrichments, its external platform API is invite-only/private.",
        "status": "Caught Hallucination",
        "verdict": "Low / Blocked",
        "lesson": "Agent conflated 'Clay connecting to external APIs' with 'Clay providing an external public REST API'."
    },
    {
        "id": 73,
        "app": "Linear",
        "category": "Productivity and Project Management",
        "initial_claim": "GraphQL API. Personal API Keys + OAuth2. Instant self-serve. Buildability: High. MCP: Official.",
        "real_docs": "Confirmed. Settings -> API -> Create Personal API Key in 5 seconds. Comprehensive GraphQL schema and official MCP server.",
        "status": "Verified Hit",
        "verdict": "High",
        "lesson": "Modern developer productivity platforms are the fastest integrations for Composio toolkits."
    },
    {
        "id": 82,
        "app": "Plaid",
        "category": "Finance and Fintech",
        "initial_claim": "API Key + Client ID. Self-serve: Yes. Instant live access. Buildability: High.",
        "real_docs": "Sandbox credentials are instant. However, Production access requires submitting company details, passing security questionnaire, and compliance approval.",
        "status": "Refined",
        "verdict": "Medium (Production Approval)",
        "lesson": "Fintech regulations mandate KYC/compliance gates; sandbox is not equal to production."
    },
    {
        "id": 90,
        "app": "PitchBook",
        "category": "Finance and Fintech",
        "initial_claim": "Enterprise gated. Self-serve: No. No free trial. Buildability: Low.",
        "real_docs": "Confirmed. API is an add-on to enterprise subscriptions (starting $25k+/yr). Contact sales mandatory. No public trial.",
        "status": "Verified Hit",
        "verdict": "Low / Blocked",
        "lesson": "High-value financial data providers protect data moats with high minimum spends and sales gates."
    },
    {
        "id": 91,
        "app": "NotebookLM",
        "category": "AI, Research and Media-native",
        "initial_claim": "REST API. Self-serve: Yes. Google AI Studio integration.",
        "real_docs": "Consumer NotebookLM has NO public REST API. Google Cloud recently announced an Enterprise API waitlist for enterprise pilot customers only.",
        "status": "Caught Hallucination",
        "verdict": "Low / Blocked",
        "lesson": "Agent assumed that because Gemini has an API, NotebookLM must share that public endpoint."
    }
]

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

with open('results.json', 'r', encoding='utf-8') as f:
    apps = json.load(f)

html = template.replace('/* __APPS_DATA__ */', json.dumps(apps))
html = html.replace('/* __VERIFICATION_DATA__ */', json.dumps(verification_sample))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully generated index.html, size:', len(html), 'bytes')
