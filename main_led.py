import time
import math
import imu
from machine import LED

# ================= CONFIGURATION =================
WINDOW_SIZE = 20              # ~1 second window
VAR_THRESHOLD = 45000         # tuned threshold
DIR_THRESHOLD = 0.6           # directional inconsistency
DURATION_COUNT = 3            # sustained abnormal windows
# ================================================

# LED (Green LED on Nicla Vision)
led = LED("LED_GREEN")
led.off()

mag_window = []
dir_window = []
abnormal_counter = 0

print("===================================")
print(" NICLA VISION SAFETY BAND STARTED ")
print("===================================")
print("System running on-device...")

while True:
    # Read acceleration in mg
    ax, ay, az = imu.acceleration_mg()

    # Compute magnitude
    mag = math.sqrt(ax*ax + ay*ay + az*az)
    mag_window.append(mag)
    if len(mag_window) > WINDOW_SIZE:
        mag_window.pop(0)

    # Direction unit vector
    norm = mag + 1e-6
    ux, uy, uz = ax/norm, ay/norm, az/norm
    dir_window.append((ux, uy, uz))
    if len(dir_window) > WINDOW_SIZE:
        dir_window.pop(0)

    if len(mag_window) == WINDOW_SIZE:
        # Magnitude variance
        mean_mag = sum(mag_window) / WINDOW_SIZE
        var = sum((x - mean_mag) ** 2 for x in mag_window) / WINDOW_SIZE

        # Directional inconsistency
        avg_dir = (
            sum(d[0] for d in dir_window) / WINDOW_SIZE,
            sum(d[1] for d in dir_window) / WINDOW_SIZE,
            sum(d[2] for d in dir_window) / WINDOW_SIZE
        )
        dir_spread = sum(
            (d[0] - avg_dir[0]) ** 2 +
            (d[1] - avg_dir[1]) ** 2 +
            (d[2] - avg_dir[2]) ** 2
            for d in dir_window
        ) / WINDOW_SIZE

        # Decision logic
        if var > VAR_THRESHOLD and dir_spread > DIR_THRESHOLD:
            abnormal_counter += 1
        else:
            abnormal_counter = 0

        # Final classification
        if abnormal_counter >= DURATION_COUNT:
            led.on()     # ABNORMAL motion detected
        else:
            led.off()    # NORMAL motion

    time.sleep_ms(50)
