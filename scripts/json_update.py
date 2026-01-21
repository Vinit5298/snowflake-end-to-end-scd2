import json
import random
import hashlib
from datetime import date, datetime

OUTPUT_FILE = "customer_cdc_day2.json"

TOTAL_UPDATES = 100_000
TOTAL_INSERTS = 30_000
TOTAL_DELETES = 20_000

cities = [f"City_{i}" for i in range(1, 101)]
states = [f"State_{i}" for i in range(1, 51)]
segments = ["Retail", "Corporate", "SME"]
ratings = ["A", "B", "C"]

records = []

def generate_hash(record):
    hash_string = (
        record["CUSTOMER_ID"]
        + record.get("EMAIL_ID", "")
        + record.get("PHONE_NUMBER", "")
        + record.get("CITY", "")
        + record.get("STATE", "")
        + record.get("CUSTOMER_SEGMENT", "")
        + record.get("CREDIT_RATING", "")
    )
    return hashlib.sha256(hash_string.encode()).hexdigest()

# UPDATE records
for _ in range(TOTAL_UPDATES):
    cid = random.randint(1, 1_500_000)
    record = {
        "CUSTOMER_ID": f"CUST{cid:07d}",
        "CUSTOMER_NAME": f"Customer_{cid}",
        "EMAIL_ID": f"cust{cid}_updated@mail.com",
        "PHONE_NUMBER": f"9{random.randint(100000000,999999999)}",
        "CITY": random.choice(cities),
        "STATE": random.choice(states),
        "COUNTRY": "USA",
        "CUSTOMER_SEGMENT": random.choice(segments),
        "CUSTOMER_STATUS": "Active",
        "CREDIT_RATING": random.choice(ratings),
        "SOURCE_SYSTEM": "CRM",
        "OPERATION": "UPDATE",
        "LOAD_DATE": date.today().isoformat(),
        "LOAD_TIMESTAMP": datetime.utcnow().isoformat()
    }
    record["RECORD_HASH"] = generate_hash(record)
    records.append(record)

# INSERT records
for i in range(1_600_001, 1_600_001 + TOTAL_INSERTS):
    record = {
        "CUSTOMER_ID": f"CUST{i:07d}",
        "CUSTOMER_NAME": f"Customer_{i}",
        "EMAIL_ID": f"cust{i}@mail.com",
        "PHONE_NUMBER": f"9{random.randint(100000000,999999999)}",
        "CITY": random.choice(cities),
        "STATE": random.choice(states),
        "COUNTRY": "USA",
        "CUSTOMER_SEGMENT": random.choice(segments),
        "CUSTOMER_STATUS": "Active",
        "CREDIT_RATING": random.choice(ratings),
        "SOURCE_SYSTEM": "CRM",
        "OPERATION": "INSERT",
        "LOAD_DATE": date.today().isoformat(),
        "LOAD_TIMESTAMP": datetime.utcnow().isoformat()
    }
    record["RECORD_HASH"] = generate_hash(record)
    records.append(record)

# DELETE records (Soft delete)
for _ in range(TOTAL_DELETES):
    cid = random.randint(1, 1_500_000)
    record = {
        "CUSTOMER_ID": f"CUST{cid:07d}",
        "OPERATION": "DELETE",
        "SOURCE_SYSTEM": "CRM",
        "LOAD_DATE": date.today().isoformat(),
        "LOAD_TIMESTAMP": datetime.utcnow().isoformat()
    }
    record["RECORD_HASH"] = generate_hash(record)
    records.append(record)

# Write file
with open(OUTPUT_FILE, "w") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")

print(f"CDC file generated: {OUTPUT_FILE}")
print(f"Total records: {len(records)}")
