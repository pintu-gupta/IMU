import smbus2
import time

# I2C address of the LSM6DSOX
I2C_ADDR = 0x6A  # Or 0x6B based on your setup

# Register Addresses
CTRL1_XL = 0x10  # Accelerometer control register
CTRL2_G = 0x11   # Gyroscope control register
ACCEL_X_L = 0x28  # Accelerometer X-axis data (low byte)
GYRO_X_L = 0x22   # Gyroscope X-axis data (low byte)

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Initialize the sensor
def initialize_sensor():
    # Enable accelerometer (ODR = 104 Hz, FS = ±2g)
    bus.write_byte_data(I2C_ADDR, CTRL1_XL, 0x50)
    # Enable gyroscope (ODR = 104 Hz, FS = ±250 dps)
    bus.write_byte_data(I2C_ADDR, CTRL2_G, 0x40)
    print("Sensor initialized.")

# Read accelerometer and gyroscope data
def read_imu_data():
    def read_data(low, high):
        low_byte = bus.read_byte_data(I2C_ADDR, low)
        high_byte = bus.read_byte_data(I2C_ADDR, high)
        value = (high_byte << 8) | low_byte
        if value & (1 << 15):  # Handle 2's complement for negative numbers
            value -= (1 << 16)
        return value

    accel_x = read_data(ACCEL_X_L, ACCEL_X_L + 1)
    accel_y = read_data(ACCEL_X_L + 2, ACCEL_X_L + 3)
    accel_z = read_data(ACCEL_X_L + 4, ACCEL_X_L + 5)
    gyro_x = read_data(GYRO_X_L, GYRO_X_L + 1)
    gyro_y = read_data(GYRO_X_L + 2, GYRO_X_L + 3)
    gyro_z = read_data(GYRO_X_L + 4, GYRO_X_L + 5)

    print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
    print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

# Main program
initialize_sensor()
time.sleep(1)  # Wait for sensor to stabilize
read_imu_data()
