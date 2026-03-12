Architecture Overview

Tech                 Stack
Layer	             Technology
Frontend	         Streamlit
Data Processing	     Pandas + PyArrow
Visualization	     Plotly
Deployment	         Streamlit Cloud


Data Pipeline

Parquet telemetry files are loaded using PyArrow.
Files are converted into Pandas DataFrames.
Event bytes are decoded into readable event names.
Data is filtered based on user selection (date, map, match).
Coordinates are converted from world space to minimap coordinates.
Visualizations are rendered using Plotly and displayed through Streamlit.


Coordinate Mapping

Game coordinates are mapped to minimap pixels using the following formula:

u = (x - origin_x) / scale
v = (z - origin_z) / scale

pixel_x = u * 1024
pixel_y = (1 - v) * 1024

Each map has unique scale and origin values which align the world coordinates with the minimap image.


Visualization Layers

The tool renders multiple layers on top of the minimap:
Player movement paths
Kill events
Death events
Loot pickups
Storm deaths
Designers can toggle these layers to focus on specific gameplay patterns.


Tradeoffs
Decision	                Reason
Streamlit instead of React	Faster development and deployment
Plotly for visualization	Interactive and easy integration
Local parquet processing	Dataset size small enough


Future Improvements

Match replay animation
Multi-player match reconstruction
Map area usage analytics
Storm path visualization
