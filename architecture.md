# Player Journey Visualization Tool – Architecture

## Tech Stack

Frontend + Visualization:
Streamlit

Data Processing:
Python, Pandas, PyArrow

Visualization:
Plotly

Deployment:
Streamlit Cloud

Why this stack:
Streamlit allows rapid development of interactive data tools without complex frontend frameworks. Plotly provides interactive visualizations, while Pandas efficiently processes telemetry data.

---

## Data Flow

Raw parquet files → Python ingestion → data cleaning → coordinate transformation → visualization

1. Parquet files are loaded using PyArrow.
2. Files are combined into a single Pandas DataFrame.
3. Event bytes are decoded into readable strings.
4. Player world coordinates (x,z) are converted into minimap pixel coordinates using the provided map configuration.
5. Data is filtered by map, match, and timeline.
6. Events are visualized on the minimap using Plotly.

---

## Key Features

• Player movement visualization  
• Combat event markers  
• Human vs bot distinction  
• Match filtering  
• Timeline playback  
• Heatmap of kill zones  

These allow level designers to quickly identify combat hotspots, player routes, and underutilized areas.

---

## Tradeoffs

Streamlit was chosen instead of a full React + API architecture to prioritize speed of development.

This means:
• Less frontend flexibility
• But faster iteration and easier deployment.

---

## Future Improvements

With more time, the tool could include:

• Map overlay heatmaps instead of separate charts  
• Event layer toggles (kills, loot, movement)  
• Player path trajectories  
• Multi-match aggregated heatmaps  
• Performance optimization for large datasets