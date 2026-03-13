# LILA Player Journey Visualization Tool

## Overview

This project is a **web-based visualization tool** designed to help Level Designers understand how players move, fight, and interact with maps in **LILA BLACK**, an extraction shooter.

The tool converts raw gameplay telemetry into interactive visualizations that allow designers to analyze:

- Player movement patterns
- Combat hotspots
- Loot activity
- Storm deaths
- Map usage patterns

By visualizing player journeys directly on the game’s minimap, the tool makes it easier to identify areas of high activity, underutilized map regions, and gameplay bottlenecks.

---

# Live Demo

Live tool:

**<https://lila-player-journey-tool-cjlemsyn5edzaekfjylvqv.streamlit.app/>**

---

# Key Features

## Player Journey Visualization

Displays player movement paths directly on top of the map minimap.

---

## Human vs Bot Differentiation

Human players and bots are visually distinguished:

| Player Type | Visualization |
|-------------|--------------|
| Human | Blue path |
| Bot | Orange path |

This allows designers to analyze differences in movement behavior between AI and human players.

---

## Event Markers

Gameplay events are visualized using distinct markers:

| Event | Marker Color |
|------|--------------|
| Kill | Red |
| Death | Black |
| Loot | Yellow |
| Storm Death | Purple |

This makes it easy to identify combat zones and high-risk areas.

---

## Map Filtering

Users can filter gameplay data by:

- Map
- Date
- Match

This allows designers to isolate specific matches or analyze map-specific behavior.

---

## Timeline Replay

A timeline slider enables replaying a match chronologically.

This helps visualize how player movement and combat evolve throughout a match.

---

## Heatmap Analysis

Heatmaps highlight areas with high activity density:

- Kill heatmap
- Death heatmap
- Player traffic heatmap

These visualizations help identify:

- combat hotspots
- dangerous areas
- underutilized map regions

---

# Dataset

The dataset contains **5 days of gameplay telemetry from LILA BLACK**.

| Metric | Value |
|------|------|
| Date Range | Feb 10 – Feb 14, 2026 |
| Total Files | 1,243 |
| Total Events | ~89,000 |
| Unique Players | 339 |
| Unique Matches | 796 |
| Maps | AmbroseValley, GrandRift, Lockdown |

Each file represents **one player's journey within a match**.

---

# How the Tool Works

The system processes telemetry data through several steps:

### 1. Data Loading

Parquet telemetry files are loaded using PyArrow and combined into a unified dataset.

### 2. Event Processing

The event column is decoded from binary format into readable event types.

### 3. Player Classification

Bots and human players are distinguished based on the user ID format.

- Numeric IDs → Bots  
- UUIDs → Humans

### 4. Coordinate Mapping

World coordinates are converted to minimap coordinates using map-specific scale and origin values.


u = (x - origin_x) / scale
v = (z - origin_z) / scale

pixel_x = u * 1024
pixel_y = (1 - v) * 1024


This ensures player paths align correctly with the minimap.

### 5. Visualization

Plotly is used to render:

- player paths
- event markers
- heatmaps
- timeline replay

---

# Running the Project Locally

## Install Dependencies


pip install -r requirements.txt


---

## Run the Application


streamlit run app.py


The tool will open in your browser.

---

# Repository Structure


.
├── app.py
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── INSIGHTS.md
├── .gitignore
│
└── player_data
├── February_10
├── February_11
├── February_12
├── February_13
├── February_14
└── minimaps


---

# Documentation

Additional documentation included in the repository:

### ARCHITECTURE.md

Explains:

- technology stack
- system design
- data pipeline
- coordinate mapping
- design tradeoffs

### INSIGHTS.md

Contains gameplay insights derived from analyzing player behavior using the tool.

---

# Future Improvements

With additional development time, the tool could be extended to include:

- animated match replay
- storm progression visualization
- map usage analytics
- multi-match comparisons
- designer annotation tools

---

# Summary

This project transforms raw gameplay telemetry into an interactive visualization platform that helps designers:

- understand player movement patterns
- identify combat hotspots
- analyze map engagement
- improve level design decisions

The tool demonstrates how data visualization can support **better gameplay


**Author**

Shreya Shrivastava


