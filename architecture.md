**Overview**

The Player Journey Visualization Tool converts raw gameplay telemetry into an interactive browser-based visualization that allows Level Designers to analyze how players navigate maps, where combat occurs, and which areas of the map receive the most activity.

The system ingests parquet telemetry files, processes them into a unified dataset, maps world coordinates to minimap coordinates, and renders interactive visualizations directly on top of map images.

The primary goal of the architecture was to optimize for rapid iteration, clarity of visualization, and ease of deployment.

**Tech Stack**
| Layer | Technology | Reason |
|------|-------------|------|
| Frontend + UI | Streamlit | Fast development and easy deployment |
| Data Processing | Pandas + PyArrow | Efficient handling of parquet telemetry |
| Visualization | Plotly | Interactive charts and map overlays |
| Image Handling | Pillow | Load and render minimap images |
| Deployment | Streamlit Cloud | Simple hosting with GitHub integration |

This stack allowed the entire tool to be implemented quickly while still providing interactive visual exploration.

**Data Flow**

The system processes data through four stages.

**1. Data Ingestion**

Telemetry files are stored in parquet format and organized by date.

Each file represents one player’s journey within a match.

The loader iterates through all folders:

player_data/
  
  February_10/
  
  February_11/
  
  February_12/
 
  February_13/
  
  February_14/

Each file is read using PyArrow, converted to Pandas DataFrames, and concatenated into a unified dataset.

**2. Data Preprocessing**

Several transformations are applied during preprocessing.

**Event decoding**

The event column is stored as binary and decoded into readable event names.

**Bot vs Human classification**

Bots are identified by numeric user IDs while humans use UUIDs.

Bot → numeric ID
Human → UUID

This classification enables visual differentiation in the map.

**Match timeline construction**

Timestamps are normalized so match events can be replayed using a timeline slider.


**3. Coordinate Mapping**

Gameplay telemetry records world coordinates, but the visualization requires 2D minimap coordinates.

Each map has a different scale and origin.

The conversion formula:

u = (x - origin_x) / scale
v = (z - origin_z) / scale

pixel_x = u * 1024
pixel_y = (1 - v) * 1024

This maps 3D game coordinates to the 2D minimap image space.

The Y-axis is flipped because image coordinate systems start at the top-left corner.

This step is critical for ensuring player paths align correctly with the minimap.

**4. Visualization Layer**

The final stage renders multiple visualization layers on top of the map:

**Player paths**

- Humans shown in blue

- Bots shown in orange

**Event markers**

- Kill events

- Death events

- Loot pickups

- Storm deaths

**Heatmaps**

- Kill density

- Death density

- Player movement density

**Timeline replay**
- A slider allows designers to replay match progression chronologically.

**System Design Choices**

Several design decisions were made to balance performance and simplicity.

**Decision	Reason**
Streamlit instead of React	Faster prototyping and simpler deployment
Pandas in-memory processing	Dataset small enough (~89k rows)
Plotly visualization	Rich interactive plotting capabilities
Local dataset loading	Simplifies architecture for prototype

This approach minimizes infrastructure complexity while enabling fast iteration.

**Tradeoffs**
| Tradeoff | Explanation |
|----------|-------------|
| In-memory processing | Works for current dataset size (~89k rows) |
| Single-node architecture | Simplifies deployment but limits scalability |
| Streamlit UI flexibility | Less customizable than a full frontend framework |

These tradeoffs were acceptable for a prototype tool focused on visualization and exploration.

**Future Improvements**

With additional development time, the system could be extended to support:

**Match replay animation**
Animated playback of player movement over time.

**Multi-player match reconstruction**
Visualizing entire matches with all players simultaneously.

**Map usage analytics**
Automatically identifying underutilized regions of the map.

**Storm progression visualization**
Overlay storm movement to analyze rotation behavior.

**Summary**

This architecture prioritizes:

- simplicity

- interactive exploration

- rapid deployment

The resulting system transforms raw telemetry into actionable insights that help Level Designers understand player behavior and improve map design.


