import smbus2

# Define the I2C address of the LSM6DSOX
I2C_ADDR = 0x6A  # Or 0x6B based on SA0 pin configuration

# Registers for accelerometer and gyroscope
ACCEL_X_L = 0x28
ACCEL_Y_L = 0x2A
ACCEL_Z_L = 0x2C
GYRO_X_L = 0x22
GYRO_Y_L = 0x24
GYRO_Z_L = 0x26

# Initialize the I2C bus
bus = smbus2.SMBus(1)  # Use I2C bus 1 on Raspberry Pi

def read_data(low, high):
    try:
        # Read low and high bytes from the sensor
        low_byte = bus.read_byte_data(I2C_ADDR, low)
        high_byte = bus.read_byte_data(I2C_ADDR, high)
        
        # Combine bytes into a single 16-bit signed value
        value = (high_byte << 8) | low_byte
        if value & (1 << 15):  # Convert to signed if necessary
            value -= (1 << 16)
        return value
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

def read_imu_data():
    accel_x = read_data(ACCEL_X_L, ACCEL_X_L + 1)
    accel_y = read_data(ACCEL_Y_L, ACCEL_Y_L + 1)
    accel_z = read_data(ACCEL_Z_L, ACCEL_Z_L + 1)
    gyro_x = read_data(GYRO_X_L, GYRO_X_L + 1)
    gyro_y = read_data(GYRO_Y_L, GYRO_Y_L + 1)
    gyro_z = read_data(GYRO_Z_L, GYRO_Z_L + 1)

    print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
    print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

# Read and display accelerometer and gyroscope data
read_imu_data()
