from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

import pandas as pd


# Crear DataFrame vacío
df = pd.DataFrame({
    "name": ["Alba", "JJ", "Chucho", "Luis Vega", "Adrian Jímenez", "Axel Luna"],
    "range": ["B", "A", "S", "S", "B", "A"],
    "car_available": [True, False, False, True, False, False],
    "location": [
        (20.645641086365778, -100.46695813152238),
        (20.616403529503508, -100.45903379018829),
        (20.608727534315317, -100.40140971274049),
        (20.594247370019197, -100.38028735889583),
        (20.616403529503508, -100.45903379018829),
        (20.645641086365778, -100.46695813152238)
    ],
    "cocktails": [[], ["Margarita", "Mojito"], ["Margarita", "Mojito", "Perla negra", "Cantarito"], [], [], ["Perla negra", "Cantarito"]],
    "events": 0
})
df["car_available"] = df["car_available"].astype(bool)
for waiter in df[3:].iloc():
    for att in waiter:
        print (att)
    data = supabase.table("waiters").insert({"name":waiter["name"],"tier": waiter['range'], "car_available": False, "location": f"{waiter['location']}",
    "cocktails": waiter['cocktails'], "events": 1}).execute()
    print(data)
