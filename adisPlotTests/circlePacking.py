# from adisPlot.charts import 
from adisPlot.charts import Circle_Packing
data = [
    {
        "id": "World",
        "datum": 6964195249,
        "children": [
            {
                "id": "North America",
                "datum": 450448697,
                "children": [
                    {"id": "United States", "datum": 308865000},
                    {"id": "Mexico", "datum": 107550697},
                    {"id": "Canada", "datum": 34033000},
                ],
            },
            {
                "id": "South America",
                "datum": 278095425,
                "children": [
                    {"id": "Brazil", "datum": 192612000},
                    {"id": "Colombia", "datum": 45349000},
                    {"id": "Argentina", "datum": 40134425},
                ],
            },
            {
                "id": "Europe",
                "datum": 209246682,
                "children": [
                    {"id": "Germany", "datum": 81757600},
                    {"id": "France", "datum": 65447374},
                    {"id": "United Kingdom", "datum": 62041708},
                ],
            },
            {
                "id": "Africa",
                "datum": 311929000,
                "children": [
                    {"id": "Nigeria", "datum": 154729000},
                    {"id": "Ethiopia", "datum": 79221000},
                    {"id": "Egypt", "datum": 77979000},
                ],
            },
            {
                "id": "Asia",
                "datum": 2745929500,
                "children": [
                    {"id": "China", "datum": 1336335000},
                    {"id": "India", "datum": 1178225000},
                    {"id": "Indonesia", "datum": 231369500},
                ],
            },
        ],
    }
]

#         # adisPlot/network_plot.py
circle_packing_chart = Circle_Packing(data)
circle_packing_chart.compute_circle_positions()
circle_packing_chart.plot_network_visualization()