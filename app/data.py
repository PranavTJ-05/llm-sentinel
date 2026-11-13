# Synthetic fixtures only. Do not put real customer data here.
TENANT_USERS = {
    "alice": "acme",
    "bob": "globex",
}

DOCUMENTS = [
    {"id": "acme-001", "tenant_id": "acme", "content": "Acme quarterly revenue is 120000."},
    {"id": "acme-002", "tenant_id": "acme", "content": "Acme internal project codename is Cedar."},
    {"id": "globex-001", "tenant_id": "globex", "content": "Globex launch plan is scheduled for December."},
]
