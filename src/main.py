import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sample_data.xlsx")

mili = df["Millisecond"]
value = df["Value"]


plt.scatter(mili, value, color="orange")
plt.title("Scatter Plot with Matplotlib")
plt.show()
