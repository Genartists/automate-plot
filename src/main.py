import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    fileName = input("Please input file name to generate plot: ") + '.xlsx'
    genPlot(fileName)

def genPlot(file):

    df = pd.read_excel(file)

    mili = df["Milliseconds"]
    value = df["Value"]


    plt.plot(mili, value, color="orange")

    plt.xlabel("Milisecond")
    plt.ylabel("Value")
    plt.title("Laser CNC plot")


    plt.show()

main()




