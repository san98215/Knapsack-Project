import glob

alg = "ls2" # Modify for ls1 or ls2
small_files = ["small_{}".format(i) for i in range(1,11)]
large_files = ["large_{}".format(i) for i in range(1,22)]
files = small_files + large_files
lines = []

for file in files:
    paths = glob.glob("../output/our_trace_files/{}_{}*".format(file, alg))
    instances = [path.replace("\\", "/") for path in paths]

    avg_time = 0
    avg_value = 0
    for instance in instances:
        with open(instance, "r") as f:
            last_line = f.readlines()[-1]
            time, value = map(float, last_line.split(","))
            avg_time += time
            avg_value += value

    lines.append("{}:\t{}, {}\n".format(file, avg_time/10, avg_value/10))

with open("{}_averages.trace".format(alg), "w") as f:
    f.writelines(lines)