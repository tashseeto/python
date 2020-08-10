import plotly.express as px
import pandas as pd


df = pd.read_csv("austpop.csv")


# fig = px.line(
#     df, 
#     x="year",
#     y="Aust",
#     title="Australian Population"
# )

fig = px.line(
    df, 
    x="year",
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    title="Australian Population by State"
)

fig = px.scatter(
    df,
    # y="year",
    y=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],
    x=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
)

fig = px.bar(
    df,
    x="year",
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    barmode="group"
)

# will need this for project

df = {
    "our_data": [123, 876, 982, 234, 122, 954, 934],
    "more_data": [34, 87, 91, 78, 21, 29, 33],
    "columns": ["a", "b", "c", "d", "e", "f", "g"]
}
fig = px.line(
    df,
    y="our_data",
    x="columns"
)
fig.show()

fig = px.line(
    df,
    y=["our_data", "more_data"],
    x="columns"
)
fig.show()

# fig.write_html("cats.html")