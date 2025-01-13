def read_imu_data():
    ACCEL_X_L = 0x28  # Replace with actual register addresses
    ACCEL_Y_L = 0x2A
    ACCEL_Z_L = 0x2C
    GYRO_X_L = 0x22
    GYRO_Y_L = 0x24
    GYRO_Z_L = 0x26

    def read_data(low, high):
        low_byte = bus.read_byte_data(I2C_ADDR, low)
        high_byte = bus.read_byte_data(I2C_ADDR, high)
        value = (high_byte << 8) | low_byte
        if value & (1 << 15):  # Check if negative (2's complement)
            value -= (1 << 16)
        return value

    accel_x = read_data(ACCEL_X_L, ACCEL_X_L + 1)
    accel_y = read_data(ACCEL_Y_L, ACCEL_Y_L + 1)
    accel_z = read_data(ACCEL_Z_L, ACCEL_Z_L + 1)
    gyro_x = read_data(GYRO_X_L, GYRO_X_L + 1)
    gyro_y = read_data(GYRO_Y_L, GYRO_Y_L + 1)
    gyro_z = read_data(GYRO_Z_L, GYRO_Z_L + 1)

    print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")
    print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

read_imu_data()
