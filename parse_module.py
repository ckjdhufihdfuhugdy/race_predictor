# parse_module.py
import pandas as pd
import re

def parse_racecard_text(text):
    lines = text.strip().split('\n')
    rows = []
    for line in lines:
        # Example: "1. BigHorse J. Smith T. Jones 5/1 32415 7"
        # You’ll likely need to tune this regex to your real output!
        m = re.match(r"^\s*(\d+)\.\s+([A-Za-z'\s]+)\s+([A-Z][a-z]+\s+[A-Z][a-z]+)\s+([A-Z][a-z]+\s+[A-Z][a-z]+)\s+([\d/]+)\s+([\d-]+)\s+(\d+)", line)
        if m:
            rows.append({
                'number': m.group(1),
                'horse': m.group(2).strip(),
                'jockey': m.group(3).strip(),
                'trainer': m.group(4).strip(),
                'odds': m.group(5).strip(),
                'form': m.group(6).strip(),
                'draw': m.group(7).strip()
            })
    df = pd.DataFrame(rows)
    return df
