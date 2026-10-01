# FutureSight_CAR:
FutureSight is an automotive dashcam built from scratch from Milk-V Duo S. It features hardware accelerated 1680p continuous loop recording with an 12c G-sensor for auto crash detection. Also I have prepared a custom 12 volt to 5 volt power converting board to handle the non sturdy vehicle(car) power.


## What makes it unique??
Unlike the commercial dashcams that lock footage behind their own apps. This project gives a person complete access and ownership of hardware and software stack. It runs a raw python on RISC-V Linux env. The hardware stack si built for extreme durability, utilizing a TPS54360DDA bulk converter and a 5.5V 4.0F supercapacitor for safe shutdown and giving time to save files before car switches off. Also it is designed to manage heat efficiently by using the large heat sync in the back panel and go-pro style mounting hinge so that it can be rotated to any angle. 

## Why i made it?
Recently my father's car got into an accident and he paid the damaged repairing cost although it wasn't his fault. So from that day i thought it would be cool if we get a dashcam(a good one). But after seeing the dashcams online the good ones were so expensive. So i thought why not make my own dashcam in home. Also i thought driving a car in those busy and chaotic roads of Kathmandu would be easier and feel confident because everything you and other person do is fully recorded and also helps us to be in discipline cause we think that this all is being recorded and we are bound to laws. 

## How to use it?
1. Mount+wire:
  Attach the dashcam module(assembled) to your car windshield using gopro compatible mount provided in 3d files of repo. Then wire 2 pin screw terminal on pcb directly to 12V power source in your car sing a cigarette lighter adapter for car.

2. Starting dashcam:
  Turn on your car. Then the system boots automatically and providing power to Milk-v-duo S. Then a background service immediately starts recording a video in 3 min. chunks.

3. Storage management:
  When the microsd card fills up, the software automatically deletes oldest normal driving footage.

4. Smart impact protection:
  If the MPU-6050 accelerometer chip detects a sudden G-force spike(triggered by eg:: hard braking, collision, car slipping etc.) , then the current video is instantly locked into `/events/` folder in sd card where it can't be overwritten. Otherwise if you press a button in the back of the dashcam it will be auto saved to `/events/` folder. Other normal recordings are saved to `/normal` folder.

## Assembly Instructions:
### 3d print enclosure:
All te 3d CAD files are provided in CAD folder of this repo. And especially 3d printable parts can be found on `/CAD/3d print/` folder in this repo. Use a high tempetrature resistant filament profile like ABS or ASA. Don't use PLA or PETG as they are not so resistant to heat and can melt on car interior temp. as it easily reaches about 70-80 °C in summer season. Also all the mounts have been pre defined in the CAD so there is no need to worry for screw fitting. 

### PCB and soldering:
Fabricate the custom matte black Kicad Pcb. Solder the SMD components first paying special attention to all components. Also before pcb printing check the 12v-5v power lines are of 1-1.5 mm width. Then solder the all the required parts to their respective footprints and places. Also snap the Milk-v-Duo S to its respective place J1 And J2 same as shown in 3d CAD model. Please ensure all the pins are arranged with the pcb otherwise it will not function. Also note that the upper black thing is completely optional because they are just a headers that are add in 3d model. 

### Flashing firmware:
Flash the official MIlk-V OS image into your SDcard. Then connect them via onboard micro sd adapter  and install the required dependencies. Create `/mnt/sdcard/dashcam/normal/` and
`/mnt/sdcard/dashcam/events/` Then. 




