# UKOL 1: Vytvoreni vizualizace z ukazkoveho souboru
# Martin Filipek, filipek.martin@gmail.com

# Import libraries
import pandas as pd
import plotly.graph_objects as go

# Data experiment 01
PATH = "datasets\cnc_mill_tool_wear\experiment_01.csv"
print("Vycteni dat 1.grafu:", PATH)
dataset = pd.read_csv(PATH)
dataset.rename(
    columns={
        r"X1_ActualPosition": "X_pos",
        r"Y1_ActualPosition": "Y_pos",
        r"Z1_ActualPosition": "Z_pos",
            },
    inplace=True,
)
fig = go.Figure()
fig.add_trace(
    go.Scatter3d(
        x=dataset["X_pos"],
        y=dataset["Y_pos"],
        z=dataset["Z_pos"],
        mode="lines",
        line=dict(color="red", width=3),
        name="CNC Experiment 01",
    )
)

# Data experiment 02
PATH = "datasets\cnc_mill_tool_wear\experiment_02.csv"
print("Vycteni dat 2.grafu:", PATH)
dataset = pd.read_csv(PATH)
dataset.rename(
    columns={
        r"X1_ActualPosition": "X_pos",
        r"Y1_ActualPosition": "Y_pos",
        r"Z1_ActualPosition": "Z_pos",
            },
    inplace=True,
)
fig.add_trace(
    go.Scatter3d(
        x=dataset["X_pos"],
        y=dataset["Y_pos"],
        z=dataset["Z_pos"],
        mode="lines",
        line=dict(color="blue", width=3),
        name="CNC Experiment 02",
    )
)


# Data experiment 03
PATH = "datasets\cnc_mill_tool_wear\experiment_03.csv"
print("Vycteni dat 3.grafu:", PATH)
dataset = pd.read_csv(PATH)
dataset.rename(
    columns={
        r"X1_ActualPosition": "X_pos",
        r"Y1_ActualPosition": "Y_pos",
        r"Z1_ActualPosition": "Z_pos",
            },
    inplace=True,
)
fig.add_trace(
    go.Scatter3d(
        x=dataset["X_pos"],
        y=dataset["Y_pos"],
        z=dataset["Z_pos"],
        mode="lines",
        line=dict(color="green", width=3),
        name="CNC Experiment 03",
    )
)

print("Vykresluji")
fig.show()