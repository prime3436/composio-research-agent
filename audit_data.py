import json
import sys

with open('results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

errors = []

# 1. Total Count
if len(data) != 100:
    errors.append(f"Expected 100 items, got {len(data)}")

# 2. Continuous IDs
ids = [d.get('id') for d in data]
if ids != list(range(1, 101)):
    errors.append(f"IDs not continuous 1..100: missing {[i for i in range(1, 101) if i not in ids]}")

# 3. Exactly 10 Categories with 10 apps each
cats = {}
for d in data:
    c = d.get('category')
    cats[c] = cats.get(c, 0) + 1

if len(cats) != 10:
    errors.append(f"Expected 10 categories, got {len(cats)}: {list(cats.keys())}")

for c, cnt in cats.items():
    if cnt != 10:
        errors.append(f"Category '{c}' has {cnt} apps, expected 10")

# 4. Fields and validation per app
for d in data:
    i = d.get('id')
    name = d.get('app', '')
    if not name or name.startswith('Unknown'):
        errors.append(f"App {i} invalid name: '{name}'")
    if not d.get('description') or len(d.get('description', '')) < 10:
        errors.append(f"App {i} ({name}) missing/short description: '{d.get('description')}'")
    if not d.get('auth_methods') or not isinstance(d.get('auth_methods'), list):
        errors.append(f"App {i} ({name}) missing/invalid auth_methods")
    if d.get('self_serve') not in ('yes', 'partial', 'no'):
        errors.append(f"App {i} ({name}) invalid self_serve: '{d.get('self_serve')}'")
    if d.get('buildability') not in ('high', 'medium', 'low'):
        errors.append(f"App {i} ({name}) invalid buildability: '{d.get('buildability')}'")
    if d.get('buildability') in ('medium', 'low') and not d.get('blocker'):
        errors.append(f"App {i} ({name}) buildability is '{d.get('buildability')}' but blocker is empty/null")
    if not d.get('evidence_url') or not d.get('evidence_url').startswith('http'):
        errors.append(f"App {i} ({name}) invalid evidence_url: '{d.get('evidence_url')}'")

print(f"=== STRICT DATA AUDIT SUMMARY ===")
print(f"Total apps audited: {len(data)}")
print(f"Categories count: {len(cats)}")
print(f"Detected errors: {len(errors)}")

if errors:
    print("\n[FAIL] Found the following issues:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("\n[PASS] All 100 apps passed 100% of strict structural and content checks.")
