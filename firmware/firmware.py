import math
import os
import time
import subprocess
from smbus2 import SMBus
import threading
import glob

##configs for firmware

# create two directories to save the recordings::
# 1. normal- to save the normal recordings(to keep recordings temporary)
# 2. event- to save the emergency recordings and recordings when pressed the button....(to keep the recording permanent)
normal_dir="/mnt/sdcard/dashcam/normal/"
event_dir="/mnt/sdcard/dashcam/events/"

# mpu6050 config
mpu6050_addr = 0x68
i2c_bus= 1
crash_thresh=1.7



# storage handle datas
duration_chunk= 180 #3mins
max_storage_mb= 4000 # 4gigs max payload for normal footages 

# global ststes:
event_happ=False
curr_file=""



# ensure dirs exist
os.makedirs(normal_dir, exist_ok=True)
os.makedirs(event_dir, exist_ok=True)

def read_i2c(bus,addr,reg):
    # read 2 bytes and convert to 16-bit int
    high = bus.read_byte_data(addr,reg)
    low= bus.read_byte_data(addr,reg+1)

    # combine those bytes
    val= (high << 8) | low

    # Convert unsigned 16-bit to signed 16-bit (2's complement)

    if val >= 0x8000:
        return val-65536 #confused with calc. so fixed with AI
    

    else:
        return val



def see_sensors():
    global event_happ
    bus=SMBus(i2c_bus)

    # wake mpu6050 (write 0x0 to pwr mgmt reg 0x6B)
    bus.write_byte_data(mpu6050_addr, 0x6B, 0)

    # start loopfor data read...
    while True:
        try:
            # read acclerr. data
            accel_x=read_i2c(bus,mpu6050_addr,0x3B)
            accel_y=read_i2c(bus,mpu6050_addr,0x3D)
            accel_z=read_i2c(bus,mpu6050_addr,0x3F)

            # convert these raw vals to standard values (g-force) +/- 2g (sc-factor 16384)
            x_gf= accel_x/16384
            y_gf= accel_y/16384
            z_gf= accel_z/16384
            
            #calc total magnitude(root(x2+y2+z2)) 
            mag_tot= math.sqrt(x_gf**2+y_gf**2+z_gf**2)

            if mag_tot > crash_thresh:
                print(f"CRASH DETECTED!!!!!!!! G-Force:{mag_tot:.2f}g")
                event_happ=True
                time.sleep(2)   #helps prevent multiple rapid trigger

        except Exception as e:
            print(f"I2c read error:{e}")

        time.sleep(0.05)


# storage loop and management logic func. 
def manage_sto():
    while True:
        files= sorted(glob.glob(f"{normal_dir}*.mp4"))
        size= sum(os.path.getsize(f) for f in files) /(1024*1024)

        if size>max_storage_mb:
            # >1 cause it can make the active recording file deleted which would make system crashed
            if len(files)>1:
                old=files[0]
                os.remove(old)
                print(f"Storage limit reached... Deleted oldest file:{old}")

        time.sleep(60)


# record video logic:
def record():
    global event_happ,curr_file
    while True:
        timestamp=time.strftime("%Y%m%d_%H%M%S")
        curr_file=f"{normal_dir}video_{timestamp}.mp4"

        # milkv ffmpeg cmd(done from ai)(cause i got confused)
        cmd = [
            "ffmpeg", "-y", "-f", "v4l2", "-framerate", "30", "-video_size", "1920x1080",
            "-i", "/dev/video0", "-c:v", "h264_cvi", "-t", str(duration_chunk), curr_file
        ]
        
        # wait for chunk to finish so that to prevent data loss
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if event_happ:
            safe_file = f"{event_dir}LOCKED_{timestamp}.mp4"
            try:
                os.rename(curr_file, safe_file)
                print(f"Footage locked successfully: {safe_file}")
            except Exception as e:
                print(f"Failed to lock file: {e}")
            event_happ = False






# main function 
if __name__=='__main__':
    # use daemon so that process becomes bg and auto stops when main program exits
    thread_1=threading.Thread(target=record,daemon=True)
    thread_2=threading.Thread(target=see_sensors,daemon=True)
    thread_3=threading.Thread(target=manage_sto,daemon=True)


    # start these threads
    thread_1.start()
    thread_2.start()
    thread_3.start()


    # keep thread alive
    while True:
        time.sleep(1)


