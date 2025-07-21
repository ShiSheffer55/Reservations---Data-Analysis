import pandas as pd
import matplotlib.pyplot as plt

# טוענים את הקובץ
df = pd.read_csv(r"C:\Users\Administrator\Downloads\reservationsN.csv")

import plotly.express as px

# ממירים את עמודת 'cancel' ל-0/1
df['cancel_numeric'] = df['cancel'].str.lower().map({'yes': 1, 'no': 0, 'y': 1, 'n': 0})

# מסירים שורות עם ערכים חסרים בעמודות 'country' ו-'cancel_numeric'
df_clean = df.dropna(subset=['country', 'cancel_numeric'])

# מחשבים ממוצע ביטולים לפי מדינה
cancel_by_country = df_clean.groupby('country')['cancel_numeric'].mean().reset_index()

# יוצרים את מפת הביטולים
fig = px.choropleth(
    cancel_by_country,
    locations='country',
    color='cancel_numeric',
    locationmode='ISO-3',
    color_continuous_scale='Reds',
    title='Cancellation Rate by Country',
    labels={'cancel_numeric': 'Cancellation Rate'}
)

# שומרים את הגרף כקובץ PNG (מציינים את מנוע הייצוא kaleido)
fig.write_image("cancellation_rate_map.png", engine="kaleido")

# מציגים את הגרף (אופציונלי)
fig.show()
