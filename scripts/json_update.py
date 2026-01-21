import json
import random
from datetime import date

OUTPUT_FILE = "customer_cdc_day2.json"

TOTAL_UPDATES = 100_000
TOTAL_INSERTS = 30_000
TOTAL_DELETES = 20_000

cities = [f"City_{i}" for i in range(1, 101)]
states = [f"State_{i}" for i in range(1, 51)]
segments = ["Retail", "Corporate", "SME"]
ratings = ["A", "B", "C"]

records = []

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
        "LOAD_DATE": date.today().isoformat()
    }
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
        "LOAD_DATE": date.today().isoformat()
    }
    records.append(record)

# DELETE records (Soft delete)
for _ in range(TOTAL_DELETES):
    cid = random.randint(1
