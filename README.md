**LILA Player Journey Visualization Tool**

**Overview**

This project is a web-based visualization tool designed to help Level Designers analyze player behavior in LILA BLACK, an extraction shooter game.

The tool converts raw gameplay telemetry into interactive visualizations showing player movement, combat hotspots, and map usage patterns.

It allows designers to understand:
- Player movement paths
- Combat locations
- Loot collection patterns
- Storm deaths
- Heatmaps of player activity


**Features**
- Interactive minimap visualization
- Player movement tracking
- Human vs Bot visualization
- Kill, Death, Loot, and Storm event markers
- Kill and Death heatmaps
- Match timeline playback
- Filtering by date, map, and match
- Visualization layer toggles


**Tech Stack**
- Frontend / UI
- Streamlit
- Data Processing
- Pandas
- PyArrow


**Visualization**
- Plotly
- Deployment
- Streamlit Cloud


__**How to Run Locally**__

_**Clone the repository:**_

git clone <repo-url>
cd lila-player-visualizer

_**Install dependencies:**_

pip install -r requirements.txt

_**Run the app:**_

streamlit run app.py

_**Open in browser:**_

http://localhost:8501


**Deployment**

The tool is deployed using Streamlit Cloud.

**Live URL:**

**<https://lila-player-journey-tool-cjlemsyn5edzaekfjylvqv.streamlit.app/>**


**Data Source**

The dataset contains 5 days of gameplay telemetry from LILA BLACK.
Each file represents one player’s journey within a single match.

Data fields include:
- player ID
- match ID
- map ID
- coordinates
- event types
- timestamps


**Author**

Shreya Shrivastava

