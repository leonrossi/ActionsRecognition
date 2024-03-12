import os
import time
from pathlib import Path
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

def generate_file_name():
    dir_path = '/'
    count_files = 0
    
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count_files += 1
    
    file_name = f"collected_data_" + str(count_files) + ".csv"

    return file_name

def read_data(start_time):
    acel = mpu.readAccelerometerMaster()
    gyro = mpu.readGyroscopeMaster()

    end_time = time.monotonic()
    time_now = end_time - start_time

    line = str(time_now)
    line += ',' + str(acel[0]) + ',' + str(acel[1]) + ',' + str(acel[2]) + ',' + str(gyro[0]) + ',' + str(gyro[1]) + ',' + str(gyro[2])

    return line

def write_results(path, file_name, start_time):
    # Check if the file already exist
    if not Path(path + file_name).is_file():
        file_ = open(path + file_name, 'w')
        header = "Time,Ax,Ay,Az,Gx,Gy,Gz\n"
        file_.write(header)
        file_.close()

    # Read and write the data
    file_ = open(path + file_name, 'a')
    data_line = read_data(start_time)
    data_line += '\n'
    file_.write(data_line)
    file_.close()


if __name__ == '__main__':

    mpu = MPU9250(
        address_ak=AK8963_ADDRESS, 
        address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
        address_mpu_slave=None, 
        bus=1,
        gfs=GFS_1000, 
        afs=AFS_8G, 
        mfs=AK8963_BIT_16, 
        mode=AK8963_MODE_C100HZ)

    mpu.calibrate() # Calibrate the sensor metrics
    mpu.configure() # Apply the settings to the registers

    f = generate_file_name()
    start = time.monotonic()
    while True:
        write_results('', f, start)
