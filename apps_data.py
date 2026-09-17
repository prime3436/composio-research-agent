"""
All 100 apps from the Composio research assignment.
Structured as a list of dicts for the research agent to process.
"""

APPS = [
    # 1. CRM and Sales
    {"id": 1,  "app": "Salesforce",                "category": "CRM and Sales",                      "url": "salesforce.com"},
    {"id": 2,  "app": "HubSpot",                   "category": "CRM and Sales",                      "url": "hubspot.com"},
    {"id": 3,  "app": "Pipedrive",                 "category": "CRM and Sales",                      "url": "pipedrive.com"},
    {"id": 4,  "app": "Attio",                     "category": "CRM and Sales",                      "url": "attio.com"},
    {"id": 5,  "app": "Twenty",                    "category": "CRM and Sales",                      "url": "twenty.com"},
    {"id": 6,  "app": "Podio",                     "category": "CRM and Sales",                      "url": "podio.com"},
    {"id": 7,  "app": "Zoho CRM",                  "category": "CRM and Sales",                      "url": "zoho.com/crm"},
    {"id": 8,  "app": "Close",                     "category": "CRM and Sales",                      "url": "close.com"},
    {"id": 9,  "app": "Copper",                    "category": "CRM and Sales",                      "url": "copper.com"},
    {"id": 10, "app": "DealCloud",                 "category": "CRM and Sales",                      "url": "api.docs.dealcloud.com"},

    # 2. Support and Helpdesk
    {"id": 11, "app": "Zendesk",                   "category": "Support and Helpdesk",               "url": "zendesk.com"},
    {"id": 12, "app": "Intercom",                  "category": "Support and Helpdesk",               "url": "intercom.com"},
    {"id": 13, "app": "Freshdesk",                 "category": "Support and Helpdesk",               "url": "freshdesk.com"},
    {"id": 14, "app": "Front",                     "category": "Support and Helpdesk",               "url": "front.com"},
    {"id": 15, "app": "Pylon",                     "category": "Support and Helpdesk",               "url": "usepylon.com"},
    {"id": 16, "app": "LiveAgent",                 "category": "Support and Helpdesk",               "url": "liveagent.com"},
    {"id": 17, "app": "Plain",                     "category": "Support and Helpdesk",               "url": "plain.com"},
    {"id": 18, "app": "Help Scout",                "category": "Support and Helpdesk",               "url": "helpscout.com"},
    {"id": 19, "app": "Gorgias",                   "category": "Support and Helpdesk",               "url": "gorgias.com"},
    {"id": 20, "app": "Gladly",                    "category": "Support and Helpdesk",               "url": "gladly.com"},

    # 3. Communications and Messaging
    {"id": 21, "app": "Slack",                     "category": "Communications and Messaging",       "url": "slack.com"},
    {"id": 22, "app": "Twilio",                    "category": "Communications and Messaging",       "url": "twilio.com"},
    {"id": 23, "app": "Zoho Cliq",                 "category": "Communications and Messaging",       "url": "zoho.com/cliq"},
    {"id": 24, "app": "Lark (Larksuite)",           "category": "Communications and Messaging",       "url": "open.larksuite.com"},
    {"id": 25, "app": "Pumble",                    "category": "Communications and Messaging",       "url": "pumble.com"},
    {"id": 26, "app": "Discord",                   "category": "Communications and Messaging",       "url": "discord.com"},
    {"id": 27, "app": "Telegram",                  "category": "Communications and Messaging",       "url": "core.telegram.org"},
    {"id": 28, "app": "WhatsApp Business",          "category": "Communications and Messaging",       "url": "developers.facebook.com/docs/whatsapp"},
    {"id": 29, "app": "Aircall",                   "category": "Communications and Messaging",       "url": "aircall.io"},
    {"id": 30, "app": "Vonage",                    "category": "Communications and Messaging",       "url": "developer.vonage.com"},

    # 4. Marketing, Ads, Email and Social
    {"id": 31, "app": "Google Ads",                "category": "Marketing, Ads, Email and Social",   "url": "developers.google.com/google-ads"},
    {"id": 32, "app": "Meta Ads",                  "category": "Marketing, Ads, Email and Social",   "url": "developers.facebook.com/docs/marketing-apis"},
    {"id": 33, "app": "LinkedIn Ads",              "category": "Marketing, Ads, Email and Social",   "url": "learn.microsoft.com/linkedin/marketing"},
    {"id": 34, "app": "GoHighLevel",               "category": "Marketing, Ads, Email and Social",   "url": "highlevel.stoplight.io"},
    {"id": 35, "app": "Mailchimp",                 "category": "Marketing, Ads, Email and Social",   "url": "mailchimp.com/developer"},
    {"id": 36, "app": "Klaviyo",                   "category": "Marketing, Ads, Email and Social",   "url": "developers.klaviyo.com"},
    {"id": 37, "app": "systeme.io",                "category": "Marketing, Ads, Email and Social",   "url": "systeme.io"},
    {"id": 38, "app": "Pinterest",                 "category": "Marketing, Ads, Email and Social",   "url": "developers.pinterest.com"},
    {"id": 39, "app": "Threads (Meta)",            "category": "Marketing, Ads, Email and Social",   "url": "developers.facebook.com/docs/threads"},
    {"id": 40, "app": "SendGrid",                  "category": "Marketing, Ads, Email and Social",   "url": "sendgrid.com"},

    # 5. Ecommerce
    {"id": 41, "app": "Shopify",                   "category": "Ecommerce",                          "url": "shopify.dev"},
    {"id": 42, "app": "WooCommerce",               "category": "Ecommerce",                          "url": "woocommerce.com/document/woocommerce-rest-api"},
    {"id": 43, "app": "BigCommerce",               "category": "Ecommerce",                          "url": "developer.bigcommerce.com"},
    {"id": 44, "app": "Salesforce Commerce Cloud", "category": "Ecommerce",                          "url": "developer.salesforce.com/docs/commerce"},
    {"id": 45, "app": "Magento (Adobe Commerce)",  "category": "Ecommerce",                          "url": "developer.adobe.com/commerce"},
    {"id": 46, "app": "Squarespace",               "category": "Ecommerce",                          "url": "developers.squarespace.com"},
    {"id": 47, "app": "Ecwid",                     "category": "Ecommerce",                          "url": "api-docs.ecwid.com"},
    {"id": 48, "app": "Gumroad",                   "category": "Ecommerce",                          "url": "gumroad.com/api"},
    {"id": 49, "app": "Amazon Selling Partner",    "category": "Ecommerce",                          "url": "developer-docs.amazon.com/sp-api"},
    {"id": 50, "app": "fanbasis",                  "category": "Ecommerce",                          "url": "fanbasis.com"},

    # 6. Data, SEO and Scraping
    {"id": 51, "app": "DataForSEO",                "category": "Data, SEO and Scraping",             "url": "docs.dataforseo.com"},
    {"id": 52, "app": "SE Ranking",                "category": "Data, SEO and Scraping",             "url": "seranking.com/api"},
    {"id": 53, "app": "Ahrefs",                    "category": "Data, SEO and Scraping",             "url": "ahrefs.com/api"},
    {"id": 54, "app": "MrScraper",                 "category": "Data, SEO and Scraping",             "url": "docs.mrscraper.com"},
    {"id": 55, "app": "Apify",                     "category": "Data, SEO and Scraping",             "url": "docs.apify.com"},
    {"id": 56, "app": "Firecrawl",                 "category": "Data, SEO and Scraping",             "url": "firecrawl.dev"},
    {"id": 57, "app": "Bright Data",               "category": "Data, SEO and Scraping",             "url": "brightdata.com"},
    {"id": 58, "app": "Sherlock",                  "category": "Data, SEO and Scraping",             "url": "github.com/sherlock-project/sherlock"},
    {"id": 59, "app": "Waterfall.io",              "category": "Data, SEO and Scraping",             "url": "waterfall.io"},
    {"id": 60, "app": "Clay",                      "category": "Data, SEO and Scraping",             "url": "clay.com"},

    # 7. Developer, Infra and Data Platforms
    {"id": 61, "app": "GitHub",                    "category": "Developer, Infra and Data Platforms","url": "docs.github.com/rest"},
    {"id": 62, "app": "Vercel",                    "category": "Developer, Infra and Data Platforms","url": "vercel.com/docs/rest-api"},
    {"id": 63, "app": "Netlify",                   "category": "Developer, Infra and Data Platforms","url": "docs.netlify.com/api"},
    {"id": 64, "app": "Cloudflare",                "category": "Developer, Infra and Data Platforms","url": "developers.cloudflare.com/api"},
    {"id": 65, "app": "Supabase",                  "category": "Developer, Infra and Data Platforms","url": "supabase.com/docs"},
    {"id": 66, "app": "PostHog",                   "category": "Developer, Infra and Data Platforms","url": "posthog.com/docs"},  # verified (screenshot seam)
    {"id": 67, "app": "Snowflake",                 "category": "Developer, Infra and Data Platforms","url": "docs.snowflake.com"},
    {"id": 68, "app": "MongoDB Atlas",             "category": "Developer, Infra and Data Platforms","url": "mongodb.com/docs/atlas/api"},
    {"id": 69, "app": "Datadog",                   "category": "Developer, Infra and Data Platforms","url": "docs.datadoghq.com/api"},
    {"id": 70, "app": "Sentry",                    "category": "Developer, Infra and Data Platforms","url": "docs.sentry.io/api"},

    # 8. Productivity and Project Management
    {"id": 71, "app": "Notion",                    "category": "Productivity and Project Management","url": "developers.notion.com"},
    {"id": 72, "app": "Airtable",                  "category": "Productivity and Project Management","url": "airtable.com/developers"},
    {"id": 73, "app": "Linear",                    "category": "Productivity and Project Management","url": "developers.linear.app"},
    {"id": 74, "app": "Jira",                      "category": "Productivity and Project Management","url": "developer.atlassian.com"},
    {"id": 75, "app": "Asana",                     "category": "Productivity and Project Management","url": "developers.asana.com"},
    {"id": 76, "app": "Monday.com",                "category": "Productivity and Project Management","url": "developer.monday.com"},
    {"id": 77, "app": "ClickUp",                   "category": "Productivity and Project Management","url": "clickup.com/api"},
    {"id": 78, "app": "Coda",                      "category": "Productivity and Project Management","url": "coda.io/developers"},
    {"id": 79, "app": "Smartsheet",                "category": "Productivity and Project Management","url": "smartsheet.com/developers"},
    {"id": 80, "app": "Harvest",                   "category": "Productivity and Project Management","url": "help.getharvest.com/api-v2"},

    # 9. Finance and Fintech
    {"id": 81, "app": "Stripe",                    "category": "Finance and Fintech",                "url": "stripe.com/docs/api"},
    {"id": 82, "app": "Plaid",                     "category": "Finance and Fintech",                "url": "plaid.com/docs"},
    {"id": 83, "app": "Binance",                   "category": "Finance and Fintech",                "url": "binance-docs.github.io"},
    {"id": 84, "app": "Paygent Connect",           "category": "Finance and Fintech",                "url": "paygent.com"},
    {"id": 85, "app": "iPayX",                     "category": "Finance and Fintech",                "url": "ipayx.ai/docs"},
    {"id": 86, "app": "QuickBooks",                "category": "Finance and Fintech",                "url": "developer.intuit.com"},
    {"id": 87, "app": "Xero",                      "category": "Finance and Fintech",                "url": "developer.xero.com"},
    {"id": 88, "app": "Brex",                      "category": "Finance and Fintech",                "url": "developer.brex.com"},
    {"id": 89, "app": "Ramp",                      "category": "Finance and Fintech",                "url": "docs.ramp.com"},
    {"id": 90, "app": "PitchBook",                 "category": "Finance and Fintech",                "url": "pitchbook.com"},

    # 10. AI, Research and Media-native
    {"id": 91, "app": "NotebookLM",                "category": "AI, Research and Media-native",      "url": "cloud.google.com/gemini"},
    {"id": 92, "app": "Otter AI",                  "category": "AI, Research and Media-native",      "url": "help.otter.ai"},
    {"id": 93, "app": "Fathom",                    "category": "AI, Research and Media-native",      "url": "fathom.video"},
    {"id": 94, "app": "Consensus",                 "category": "AI, Research and Media-native",      "url": "consensus.app"},
    {"id": 95, "app": "Reducto",                   "category": "AI, Research and Media-native",      "url": "reducto.ai"},
    {"id": 96, "app": "Devin",                     "category": "AI, Research and Media-native",      "url": "docs.devin.ai"},
    {"id": 97, "app": "higgsfield",                "category": "AI, Research and Media-native",      "url": "higgsfield.ai/cli"},
    {"id": 98, "app": "Mermaid CLI",               "category": "AI, Research and Media-native",      "url": "github.com/mermaid-js/mermaid-cli"},
    {"id": 99, "app": "YouTube Transcript",        "category": "AI, Research and Media-native",      "url": "transcriptapi.com"},
    {"id": 100,"app": "Grain",                     "category": "AI, Research and Media-native",      "url": "grain.com"},
]

CATEGORIES = [
    "CRM and Sales",
    "Support and Helpdesk",
    "Communications and Messaging",
    "Marketing, Ads, Email and Social",
    "Ecommerce",
    "Data, SEO and Scraping",
    "Developer, Infra and Data Platforms",
    "Productivity and Project Management",
    "Finance and Fintech",
    "AI, Research and Media-native",
]
