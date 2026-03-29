import requests
import sqlite3
import time

# --- CONFIGURATION ---
# Perak Bounding Box coordinates (Corrected for Malaysia)
LAMIN, LOMIN, LAMAX, LOMAX = 3.6, 100.0, 6.1, 101.7


def main():
    # 1. Database Setup
    conn = sqlite3.connect('perak_flights.db')
    curr = conn.cursor()
    curr.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            icao24 TEXT, 
            callsign TEXT, 
            lat REAL, 
            lon REAL, 
            alt REAL, 
            time INT
        )
    ''')
    conn.commit()

    print(f"System Status: IoT Collector is STANDBY (Authenticated as {USER})...")
    
    while True:
        # 2. API Request with Authentication
        url = "https://opensky-network.org/api/states/all"
        payload = {
            'lamin': LAMIN, 
            'lomin': LOMIN, 
            'lamax': LAMAX, 
            'lomax': LOMAX
        }
        
        try:
            # bypass the shared University IP limit
            r = requests.get(url, params=payload, auth=(USER, PASS), timeout=15)
            
            # Handle status codes
            if r.status_code == 429:
                print("Status: Rate limit hit. Sleeping for 2 minutes...")
                time.sleep(120)
                continue
            elif r.status_code == 401:
                print("Error: Authentication Failed! Check your Username/Password.")
                break
            
            data = r.json()
            states = data.get('states')
            
            # Data Storage Logic
            if states:
                for s in states:
                    # Column Mapping from OpenSky:
                    # s[0]=ICAO, s[1]=Callsign, s[6]=Lat, s[5]=Lon, s[7]=Alt, s[4]=Time
                    curr.execute("INSERT INTO flights VALUES (?,?,?,?,?,?)", 
                                 (s[0], s[1].strip(), s[6], s[5], s[7], s[4]))
                
                conn.commit()
                print(f"Log: {time.strftime('%H:%M:%S')} - Saved {len(states)} aircraft records in Perak.")
            else:
                print(f"Log: {time.strftime('%H:%M:%S')} - No aircraft detected in Perak right now.")
        
        except Exception as e:
            # This keeps the script running even if the internet flickers
            print(f"Notice: Waiting for server/network... (Retrying in 60s)")
        
        # Sampling rate: Wait 5 mins before next check
        time.sleep(300)

if __name__ == "__main__":
    main()