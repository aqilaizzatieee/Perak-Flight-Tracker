Perak Flight Tracker

A real time flight tracking dashboard built using Python, Streamlit and SQLite with OpenSky API integration. This project collects live aircraft data within Perak airspace and displays it through an interactive dashboard.

Features

• Real time aircraft tracking
• Interactive flight map visualization
• Aircraft altitude and location monitoring
• SQLite database logging
• Automatic API data collection
• Live dashboard refresh

Tech Stack

• Python
• Streamlit
• Pandas
• SQLite
• Plotly
• OpenSky API

Project Structure

```bash
Perak-Flight-Tracker/
│
├── app.py
├── collector.py
├── perak_flights.db
├── requirements.txt
└── README.md
```

Installation

Clone the repository:

```bash
git clone https://github.com/aqilaizzzatiee/Perak-Flight-Tracker.git
cd Perak-Flight-Tracker
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Requirements

```txt
streamlit
pandas
plotly
requests
```

Run the Project

Start the data collector:

```bash
python collector.py
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

Future Improvements

• Add historical flight analytics
• Deploy application online
