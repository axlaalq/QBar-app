import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import math
import random
from faker import Faker
faker = Faker()

from scipy.stats import lognorm
# Definir el rango de fechas
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

# Lista para almacenar las fechas
dates = []
counts = []
day_probs = np.array([0.05, 0.07, 0.06, 0.1, 1.1, 1.9, 1])  # Probabilidades por día (lunes a domingo)
month_increase = np.array([0.7, 0.4, 0.6, 0.71, 0.79, 0.88, 0.89, 0.92, 1.42, 1.1, 1.2, 1.5])  # Incremento mensual
# Recorrer cada día entre start_date y end_date
current_date = start_date

# Define head waiters and assign them the 'S' tier
assistance=[]
head_waiters = [
    "Marce Vega", "JJ", "Chucho", "Luis Vega",
    "Adrian Jímenez", "Axel Luna", "Vane B.", "Caro", "Vicky Reyna"
]

# Expand list of waiters with 50 random names from Faker
waiters = head_waiters + [faker.name() for _ in range(50)]

# Create DataFrame with tiers
data = {
    "id": range(1, len(waiters) + 1),
    "name": waiters,
    "tier": ["S" if waiter in head_waiters else random.choice(["D", "C", "B", "A"]) for waiter in waiters]
}

waiters_df = pd.DataFrame(data)

latitude_range = (20.5, 20.8)  # Ejemplo: latitud de 20.5 a 20.8
longitude_range = (-100.5, -100.2)  # Ejemplo: longitud de -100.5 a -100.2

waiters_df['coordinates'] = [
    (round(random.uniform(*latitude_range), 6), round(random.uniform(*longitude_range), 6))
    for _ in range(len(waiters_df))
]

#venue list
salones =  pd.DataFrame({
    "id": range(1, 11),
    "name": [
        "Salón Imperial", "Gran Salón Victoria", "Hacienda Las Campanas",
        "Jardín Encantado", "Salón Las Fuentes", "Quinta Real Querétaro",
        "Jardines de San Juan", "Casa Blanca Eventos", "La Estancia Jardín",
        "Terraza Real"
    ],
    "location": [
        (20.5936, -100.3927), (20.6094, -100.4037), (20.6224, -100.4256),
        (20.5768, -100.3729), (20.6067, -100.4101), (20.6151, -100.4337),
        (20.6048, -100.4065), (20.5931, -100.3956), (20.6193, -100.4245),
        (20.6027, -100.4012)
    ]
})



while current_date <= end_date:
    available_captains = list(head_waiters)
    available_waiters = list(waiters)
    current_odd = day_probs[current_date.weekday()] * month_increase[current_date.month-1]
    day_count=math.floor(current_odd)
    # Añadir la fecha al DataFrame en el formato "día, mes, año"
    if current_odd-math.floor(current_odd) >random.random():
        day_count=day_count+1
        dates.append(current_date.strftime('%d,%m,%Y'))
        counts.append(day_count)
    for event in range(0,day_count):
#Pick a random captain
        waiters_list=[]
        captain=random.choice(available_captains)
        available_waiters.remove(captain)
        available_captains.remove(captain)
        waiters_list.append(captain)


#Add the closest waiters to the event
        w_request=int(lognorm.rvs(0.8, scale=(4/ np.exp(0.5 * 0.8 ** 2))))
        selected_venue=random.choice(salones['name'])
        venue_location = salones[salones['name'] == selected_venue]['location'].iloc[0]
        waiters_df['distance'] = waiters_df['coordinates'].apply(lambda x: math.dist(x, venue_location))
        sorted_waiters = waiters_df.sort_values(by='distance')
        closest_waiters = sorted_waiters.head(w_request-1)
        waiters_list.append(closest_waiters['name'].tolist())
        assistance.append(waiters_list)
    current_date += timedelta(days=1)
print(len(assistance))
print(len(dates))
# Crear el DataFrame con la lista de fechas
df = pd.DataFrame({'date':dates,'event_count':counts})
# Convertir la columna 'Date' de string a datetime para facilitar el filtrado
df['date'] = pd.to_datetime(df['date'], format='%d,%m,%Y')
# Filtrar las fechas correspondientes
for month in range(1,13):
    df_2023 = df[(df['date'].dt.month == month) & (df['date'].dt.year == 2023)]
    df_2024 = df[(df['date'].dt.month == month) & (df['date'].dt.year == 2024)]






# Extract the month and year from the 'date' column
df['month'] = df['date'].dt.month
df['Año'] = df['date'].dt.year

# Group by month and year, then sum the event counts
monthly_event_counts = df.groupby(['Año', 'month'])['event_count'].sum().reset_index()
# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.set_style("whitegrid")
month_map = {
    1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"
}

# Cambia los números por los nombres de meses
monthly_event_counts['month'] = monthly_event_counts['month'].map(month_map)
print(monthly_event_counts)
sns.set(font_scale=2)
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
ax = sns.barplot(x = 'month',
            y = 'event_count',
            hue = 'Año',
            data = monthly_event_counts)


plt.title('Eventos por mes', fontsize=26)

#add axis titles
plt.xlabel('Mes')
plt.ylabel('Numero de eventos')
plt.xticks(rotation=45)
# Show the plot
plt.show()
