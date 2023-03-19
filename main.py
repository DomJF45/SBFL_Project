import os

file_count = 0
line_count = 0

dir_path = os.getcwd() + "/CoverageData"
print(dir_path)

#O(n^2) run time, can we optimize this?

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        file_count += 1
        with open(r"{}".format(dir_path + "/" + path), "r") as fp:
            for count, line in enumerate(fp):
                if line != "\n":
                    line_count += 1
                pass




print("File count: ", file_count)
print("Total Lines: ", line_count)
