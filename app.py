import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import os
from PIL import Image
import plotly.express as px

st.set_page_config(layout="wide")

st.title("LILA BLACK Player Journey Visualization Tool")
st.write("Explore player movement, combat events, and heatmaps on the map.")

# -------------------------
# MAP SELECTION
# -------------------------

map_choice = st.selectbox(
    "Select Map",
    ["AmbroseValley", "GrandRift", "Lockdown"]
)

map_images = {
    "AmbroseValley": "minimaps/AmbroseValley_Minimap.png",
    "GrandRift": "minimaps/GrandRift_Minimap.png",
    "Lockdown": "minimaps/Lockdown_Minimap.jpg"
}

img = Image.open(map_images[map_choice])

st.image(img, caption=f"{map_choice} Minimap", use_container_width=True)

# -------------------------
# MAP CONFIGURATION
# -------------------------

MAP_CONFIG = {
    "AmbroseValley": {"scale": 900, "origin_x": -370, "origin_z": -473},
    "GrandRift": {"scale": 581, "origin_x": -290, "origin_z": -290},
    "Lockdown": {"scale": 1000, "origin_x": -500, "origin_z": -500}
}

# -------------------------
# WORLD → MINIMAP FUNCTION
# -------------------------

def world_to_minimap(x, z, map_id):

    cfg = MAP_CONFIG[map_id]

    u = (x - cfg["origin_x"]) / cfg["scale"]
    v = (z - cfg["origin_z"]) / cfg["scale"]

    px = u * 1024
    py = (1 - v) * 1024

    return px, py


# -------------------------
# LOAD DATA
# -------------------------

@st.cache_data
def load_data(folder):

    frames = []

    for root, dirs, files in os.walk(folder):
        for f in files:

            if f.endswith(".nakama-0"):

                path = os.path.join(root, f)

                try:
                    table = pq.read_table(path)
                    df = table.to_pandas()
                    frames.append(df)

                except:
                    continue

    data = pd.concat(frames, ignore_index=True)

    data["event"] = data["event"].apply(
        lambda x: x.decode("utf-8") if isinstance(x, bytes) else x
    )

    return data


data = load_data("player_data")

# -------------------------
# FILTER BY MAP
# -------------------------

filtered = data[data["map_id"] == map_choice]

# -------------------------
# MATCH SELECTOR
# -------------------------

match_choice = st.selectbox(
    "Select Match",
    filtered["match_id"].unique()
)

filtered = filtered[filtered["match_id"] == match_choice]

# -------------------------
# HUMAN VS BOT
# -------------------------

filtered["is_bot"] = filtered["user_id"].astype(str).str.isnumeric()

# -------------------------
# TIMELINE SLIDER
# -------------------------

filtered["time_seconds"] = filtered["ts"].astype("int64") // 1_000_000_000

max_time = int(filtered["time_seconds"].max())

time_value = st.slider(
    "Match Timeline",
    0,
    max_time,
    max_time
)

filtered = filtered[filtered["time_seconds"] <= time_value]

# -------------------------
# COORDINATE CONVERSION
# -------------------------

coords = filtered.apply(
    lambda r: world_to_minimap(r["x"], r["z"], r["map_id"]),
    axis=1
)

filtered["px"] = coords.apply(lambda c: c[0])
filtered["py"] = coords.apply(lambda c: c[1])

# -------------------------
# HEATMAP TOGGLE
# -------------------------

show_heatmap = st.checkbox("Show Kill Heatmap")

# -------------------------
# VISUALIZATION
# -------------------------

if show_heatmap:

    kill_events = filtered[
    filtered["event"].isin(["Position","BotPosition"])
]

    fig = px.density_heatmap(
        kill_events,
        x="px",
        y="py",
        nbinsx=50,
        nbinsy=50
    )

else:

    fig = px.scatter(
        filtered,
        x="px",
        y="py",
        color="is_bot",
        hover_data=["user_id","event","ts"],
        color_discrete_map={
            True: "orange",
            False: "blue"
        }
    )

fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)