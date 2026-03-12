import os
import pandas as pd
import pyarrow.parquet as pq

def load_data(base_folder="player_data"):

    frames = []

    for root, dirs, files in os.walk(base_folder):

        for file in files:

            if file.endswith(".nakama-0"):

                path = os.path.join(root, file)

                try:
                    table = pq.read_table(path)
                    df = table.to_pandas()

                    # decode event column
                    if "event" in df.columns:
                        df["event"] = df["event"].apply(
                            lambda x: x.decode("utf-8") if isinstance(x, bytes) else x
                        )

                    frames.append(df)

                except Exception as e:
                    print("Skipping:", path)

    if len(frames) == 0:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)