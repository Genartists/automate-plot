import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file = "sample_data2.xlsx"

df = pd.read_excel(file)

mili = df["Milliseconds"]
value = df["Value"]


plt.plot(mili, value, color="orange")
# plt.scatter(mili, value, color="black")

plt.xlabel("Milisecond")
plt.ylabel("Value")
plt.title("Scatter Plot")


plt.show()
