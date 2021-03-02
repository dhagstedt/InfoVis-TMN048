import pandas as pd

df_co2 = pd.read_csv(
    "/Users/danielhagstedt/Documents/Skola/infovis/Labs/project/data/co2_emission.csv"
)

df_coord = pd.read_csv(
    "/Users/danielhagstedt/Documents/Skola/infovis/Labs/project/data/world_coordinates.csv"
)

df_merge = df_co2.merge(df_coord, on="Country", how="left")

df_merge.dropna(subset=["latitude"], inplace=True)

df_merge.to_csv("mergedData.csv")