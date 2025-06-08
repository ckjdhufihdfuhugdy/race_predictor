"""Utilities to parse racecard text into structured data."""

import re
import pandas as pd

# Example regex pattern. Adjust to match the actual format of your racecard text.
_ROW_PATTERN = re.compile(
    r"^\s*(\d+)\.\s+([A-Za-z'\s]+)\s+([A-Za-z\.]+\s+[A-Za-z'\-]+)\s+([A-Za-z\.]+\s+[A-Za-z'\-]+)\s+([\d/]+)\s+([\d-]+)\s+(\d+)"
)


def parse_racecard_text(text: str) -> pd.DataFrame:
    """Parse OCR text of a racecard into a DataFrame."""
    rows = []
    for line in text.splitlines():
        match = _ROW_PATTERN.match(line)
        if match:
            rows.append(
                {
                    "number": match.group(1),
                    "horse": match.group(2).strip(),
                    "jockey": match.group(3).strip(),
                    "trainer": match.group(4).strip(),
                    "odds": match.group(5).strip(),
                    "form": match.group(6).strip(),
                    "draw": match.group(7).strip(),
                }
            )
    return pd.DataFrame(rows)
