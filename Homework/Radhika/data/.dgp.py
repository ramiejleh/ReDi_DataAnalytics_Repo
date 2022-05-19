import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
N = 1000
p = 3
Theta = np.diag([0.7, 0.8])
Theta[(0, 1), (1, 0)] = 0.2

Y = np.ones([p - 1, N])
Y[:, 0] = np.random.normal(10, 2, 2)
intercept = np.array([0.5, 0.5]).reshape([p - 1, 1])

for t in range(1, N):
    Y[:, [t]] = intercept + Theta @ Y[:, [t - 1]]
    Y[:, [t]] += np.random.normal(0, 1, [p - 1, 1])

cos_series = (10 + 5 * np.cos(2 * np.pi * np.arange(N) / 500)).reshape(1, N)
cos_series += np.random.normal(0, 2, [1, N])
Y = np.concatenate([Y, cos_series])


Y = np.round(Y, 4)
temp_col = [f"temp{i}" for i in range(1, p+1)]
df = pd.DataFrame(data=Y.T , columns=temp_col)
df["time"] = pd.date_range(start="05-04-2021 17:10:01", periods=N, freq="1S")
df = df[["time"] + temp_col]


missing_values_mask = np.random.binomial(1, 0.05, size=[N, p - 1])
for i, col in enumerate(["temp1", "temp2"]):
    idx = missing_values_mask[:, i].astype(bool)
    df.loc[idx, col] = np.nan

df.loc[650: 800, "temp3"] = np.nan

fig, ax = plt.subplots()
df[temp_col].plot(ax=ax)
plt.show()

df.to_csv("temperature_signals.csv", index=False)