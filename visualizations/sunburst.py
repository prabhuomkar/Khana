import os
import plotly.express as px
import pandas as pd


ROOT = "../khana"
OUTPUT_LOCATION = "../paper/figs"

df = pd.read_csv("../docs/files/taxonomy.csv")

for row in df.itertuples():
    dir = row.variety if not pd.isna(df.at[row.Index, "variety"]) else row.dish
    if os.path.isdir(f"{ROOT}/{dir}"):
        images = os.listdir(f"{ROOT}/{dir}")
        df.at[row.Index, "Count"] = len(images)

custom_color_scale = [
    [0.0, "#F8474A"],
    [1.0, "#4E4193"],
]

fig = px.sunburst(df, path=["category", "dish", "variety"],
                  values="Count",
                  color="Count",
                  color_continuous_scale=custom_color_scale)
fig.update_layout(
    font=dict(
        family="Fira Code"
    )
)
fig.update_traces(marker=dict(colorscale=custom_color_scale, showscale=False))
fig.write_image(f"{OUTPUT_LOCATION}/sunburst.pdf", scale=((130 / 25.4) / (700 / 720)))
