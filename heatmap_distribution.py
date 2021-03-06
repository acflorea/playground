import plotly
import plotly.graph_objs as go

z_netbeans = [[0.729, 0.742, 0.686, 0.531, 0.478, 0.423, 0.471, 0.435, 0.432],
              [0.839, 0.823, 0.789, 0.783, 0.727, 0.512, 0.557, 0.471, 0.460],
              [0.806, 0.827, 0.823, 0.804, 0.779, 0.738, 0.674, 0.528, 0.426],
              [0.835, 0.822, 0.821, 0.817, 0.776, 0.803, 0.762, 0.813, 0.654],
              [0.820, 0.821, 0.840, 0.804, 0.778, 0.821, 0.818, 0.790, 0.753],
              [0.830, 0.827, 0.845, 0.828, 0.806, 0.824, 0.768, 0.799, 0.794],
              [0.772, 0.785, 0.803, 0.820, 0.833, 0.798, 0.820, 0.793, 0.788],
              [0.776, 0.802, 0.795, 0.769, 0.800, 0.800, 0.797, 0.790, 0.799],
              [0.820, 0.801, 0.842, 0.804, 0.820, 0.833, 0.762, 0.815, 0.792]]

z_eclipse = [[0.523, 0.550, 0.441, 0.365, 0.344, 0.359, 0.368, 0.361, 0.317],
             [0.673, 0.658, 0.625, 0.595, 0.527, 0.414, 0.350, 0.376, 0.368],
             [0.634, 0.636, 0.658, 0.657, 0.625, 0.517, 0.504, 0.486, 0.408],
             [0.657, 0.658, 0.656, 0.658, 0.639, 0.653, 0.617, 0.605, 0.607],
             [0.639, 0.665, 0.624, 0.652, 0.625, 0.599, 0.650, 0.618, 0.590],
             [0.639, 0.652, 0.646, 0.656, 0.658, 0.631, 0.625, 0.641, 0.620],
             [0.643, 0.645, 0.654, 0.629, 0.677, 0.631, 0.653, 0.640, 0.594],
             [0.660, 0.628, 0.657, 0.648, 0.626, 0.638, 0.615, 0.618, 0.648],
             [0.628, 0.650, 0.656, 0.652, 0.660, 0.637, 0.635, 0.650, 0.613]]

z_firefox = [[0.527, 0.549, 0.506, 0.197, 0.314, 0.288, 0.237, 0.196, 0.189],
             [0.596, 0.592, 0.585, 0.559, 0.532, 0.302, 0.266, 0.198, 0.153],
             [0.582, 0.581, 0.587, 0.569, 0.387, 0.294, 0.348, 0.251, 0.164],
             [0.572, 0.613, 0.524, 0.410, 0.604, 0.573, 0.549, 0.544, 0.345],
             [0.578, 0.586, 0.528, 0.576, 0.582, 0.322, 0.563, 0.410, 0.384],
             [0.573, 0.553, 0.581, 0.587, 0.600, 0.351, 0.470, 0.394, 0.397],
             [0.572, 0.522, 0.519, 0.576, 0.563, 0.585, 0.572, 0.343, 0.535],
             [0.533, 0.537, 0.565, 0.453, 0.394, 0.568, 0.579, 0.578, 0.564],
             [0.549, 0.570, 0.555, 0.586, 0.488, 0.565, 0.577, 0.327, 0.579]]

data_netbeans = [
    go.Heatmap(
        z=z_netbeans,
        x=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_'],
        y=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_']
    )
]

data_eclipse = [
    go.Heatmap(
        z=z_eclipse,
        x=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_'],
        y=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_']
    )
]

data_firefox = [
    go.Heatmap(
        z=z_firefox,
        x=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_'],
        y=['_1_', '_5_', '_10_', '_25_', '_50_', '_75_', '_100_', '_125_', '_150_']
    )
]

plot_url_netbeans = plotly.offline.plot(data_netbeans, filename='netbeans')
plot_url_eclipse = plotly.offline.plot(data_eclipse, filename='eclipse')
plot_url_firefox = plotly.offline.plot(data_firefox, filename='firefox')
