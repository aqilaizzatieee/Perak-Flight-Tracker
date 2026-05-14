<img width="1440" height="824" alt="Screenshot 2026-05-14 at 1 15 00 PM" src="https://github.com/user-attachments/assets/56c962c8-b490-492f-968d-09ce72d8f3de" />Perak Flight Tracker

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

Preview!
[Uploading Screenshot 2026-05-14 at 1.15.00 PM.png…]()
<img width="1440" height="824" alt="Screenshot 2026-05-14 at 1 15 06 PM" src="https://github.com/user-attachments/assets/4a3a51fc-be97-4932-8f2c-dd23e0f43a06" />




Future Improvements

• Add historical flight analytics
• Deploy application online
