
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

def load_csv(name: str) -> pd.DataFrame:
    p = DATA_DIR / name
    return pd.read_csv(p)

def load_all():
    return {
        "financial": load_csv("financial.csv"),
        "hr": load_csv("hr.csv"),
        "security": load_csv("security.csv"),
        "rd": load_csv("rd.csv"),
        "supply": load_csv("supply.csv"),
    }
