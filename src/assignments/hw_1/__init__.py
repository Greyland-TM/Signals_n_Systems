import matplotlib.pyplot as plt
import numpy as np
import math

def evaluate_y(current_time: float) -> float:
    sign = math.copysign(1.0, current_time)
    mod = (current_time - sign) % 3 if sign < 0 else (current_time + sign) % 3
    time_step = int(current_time)
    correction_factor = 0 if sign < 0 else 1

    if mod > 0 and mod <= 1:
        time_step = time_step - (1 - correction_factor)
        y_value = (-2 * (current_time - (time_step))) + 2
    elif mod > 1 and mod <= 2:
        time_step = time_step - (2 - correction_factor )
        y_value = (-2 * (current_time - (time_step))) + 2
    elif mod > 2 and mod <= 3:
        time_step = time_step - (1 - correction_factor)
        y_value = (3 * (current_time - (time_step))) - 2
        if 3 - mod < 0.1:
            y_value = np.nan
    else:
        y_value = (-2 * (current_time - (time_step)))
    print(current_time, mod, time_step, y_value)
    return y_value

time = np.linspace(-30, 30, 2000)
y_values = np.vectorize(evaluate_y, otypes=[float])(time)

fig, ax = plt.subplots()
ax.plot(time, y_values)
plt.xticks(np.arange(-30, 30, 2))
x_discont = 0

plt.show()

