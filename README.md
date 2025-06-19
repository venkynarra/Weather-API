# Weather-API

**Tech Stack:** Python, Flask, Pandas, HTML

## Description
A lightweight Flask-based weather API server that serves historical temperature data for various global weather stations. The app reads CSV files and exposes data through several REST endpoints.

## Key Features
- 🌐 View a list of all weather stations
- 📆 Get temperature data for a specific station on a specific date
- 📊 Fetch all available temperature data for a station
- 📅 Retrieve yearly temperature data per station

## Project Structure
- `main.py` – Flask server with multiple routes
- `templates/` – Contains the HTML homepage (renders station table)
- `static/` – Public assets (optional)
- `data_small/` – CSV weather datasets for different stations

## API Endpoints
- `/` – Homepage with table of stations
- `/api/v1/<station>/<date>` – Temperature for a station on a specific date
- `/api/v1/<station>` – All available data for a station
- `/api/v1/yearly/<station>/<year>` – All data for a given year

## How to Run
```bash
pip install flask pandas
python main.py
