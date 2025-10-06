import pandas as pd
from pathlib import Path
import os
print(os.getcwd())

script_dir = Path(__file__).resolve().parent
file_path = script_dir / "data" / "agents_stats.csv"


df = pd.read_csv(file_path)
print(df.head(200))

# agent_stats =
