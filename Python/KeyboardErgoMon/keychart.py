import matplotlib.pyplot as plt
import numpy as np
import json

keyfile = open("C:\\Users\\natha\\Documents\\keyfile.json", "r")
key_dict = json.load(keyfile)
sort_dict = {k: v for k, v in sorted(key_dict.items(), key=lambda x: x[1])}


print(sort_dict)

keys = sort_dict.keys()
values = sort_dict.values()
y_pos = np.arange(len(keys))

plt.bar(y_pos, values, align="center", alpha=0.5)
plt.xticks(y_pos, keys, rotation=45)
plt.title("Key usage")
plt.show()
