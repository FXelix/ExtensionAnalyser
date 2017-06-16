"""
extension analyser for folders
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

endings = {}


def extension_analyser(start):
    for root, folders, filenames in os.walk(start):
        for file in filenames:
            end = os.path.splitext(os.path.abspath(file))  # absolute path into tuple of dirname and extension
            end = end[1]  # get extension
            if end not in endings.keys():
                endings.setdefault(end, 1)
            else:
                endings[end] += 1

    max_value = max(endings.values())
    maximum = [i for i in endings if endings[i] == max_value]
    min_value = min(endings.values())
    minimum = [i for i in endings if endings[i] == min_value]

    print("The extenstion(s) \"{}\" are the most common with {} uses each.".format(", ".join(maximum), max_value))
    print("The extension(s) \"{}\" are the least common with {} use(s) each.".format(", ".join(minimum), min_value))

    s = pd.Series(endings, index=endings.keys()).sort_values()  # sorted series to display results
    s = s[::-1]  # from highest count to lowest
    print(s)
    s.plot.bar()
    plt.show()

if __name__ == "__main__":
    while True:
        start_folder = input("Enter a valid foldername: ")
        if os.path.isdir(start_folder):
            extension_analyser(start_folder)
        else:
            print("Could not find folder.")
            continue
