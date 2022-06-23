from perlin_noise import PerlinNoise
import json

size = 24
num_sensors = 2

shape = (1024,1024)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

# noise = PerlinNoise(octaves=1, seed= 123)

noise1 = PerlinNoise(octaves=6)
noise2 = PerlinNoise(octaves=12)
noise3 = PerlinNoise(octaves=24)
noise4 = PerlinNoise(octaves=48)
data = {
    "sensors": [],
}

for j in range(num_sensors):
    values = []
    for i in range(size):
        noise_val = noise1([i/size, j/num_sensors])
        noise_val += 0.5 * noise2([i/size, j/num_sensors])
        noise_val += 0.25 * noise3([i/size, j/num_sensors])
        noise_val += 0.125 * noise4([i/size, j/num_sensors])
        values.append(
            {
                "timestamp": 1653322292 + i*900,
                "value": (noise_val + 0.5) * 20
            }
        )
    data["sensors"].append({
        "id": j,
        "type": "pm_10",
        "time_series": values
    })

with open('db.json', 'w') as f:
    json.dump(data, f, indent=4)

