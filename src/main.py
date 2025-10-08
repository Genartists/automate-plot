# import pandas as pd
# import matplotlib.pyplot as plt
# from gui import MyUI
# import os

# def main():
#     name = MyUI.sayHello
#     fileName = name + ".xlsx"
#     genPlot(fileName)


# def genPlot(file):

#     df = pd.read_excel(file)

#     mili = df["Milliseconds"]
#     value = df["Value"]

#     plt.plot(mili, value, color="orange")

#     plt.xlabel("Milisecond")
#     plt.ylabel("Value")
#     plt.title("Laser CNC plot")

#     plt.show()


# main()
