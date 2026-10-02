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
Flash the official MIlk-V OS image into your SDcard. Then connect them via onboard micro sd adapter and install the required dependencies(ffmpeg,python3,py3-smbus2). Create `/mnt/sdcard/dashcam/normal/` and `/mnt/sdcard/dashcam/events/` folder/directories inside the sd card. Drop the firmware files in the root folder and enable it as a startup service. 

### Getting the data:
For now you can extract your dashcam videos by unplugging the Sd-card from the dashcam and plugging it in the sd card reader in pc,mobile or any other mountable device. And also you can directly connect your milk v type c port into your pc and access your data. But in future i plan to make a native app for the dashcam and use the inbuilt wifi antenna thing to sync the data. Also i plan to make the app fully run locally in users’ devices, protecting the privacy of the user.  

## Future changes:
I have kept the ipex connector cable with wifi+bluetooth antenna in the pcb,BOM and CAD but that is completely optional for now as the app and the wifi setup hasnt been added in the firmware yet. In future it will be added. Also the app for the dashcam isnt functional yet and will be updated in future.


## Assets:
### CAD screenshots:
<img width="798" height="600" alt="Screenshot 2026-10-02 at 6 51 13 PM" src="https://github.com/user-attachments/assets/158d9307-d3dd-4206-948f-2ca37e280d22" />
<img width="414" height="531" alt="Screenshot 2026-10-02 at 6 51 52 PM" src="https://github.com/user-attachments/assets/3fa75e5a-99b2-4c89-8798-0fbc24636da7" />
<img width="776" height="588" alt="Screenshot 2026-10-02 at 6 51 38 PM" src="https://github.com/user-attachments/assets/2564826d-31c9-4363-8c14-a66a70480a7b" />
<img width="864" height="543" alt="Screenshot 2026-10-02 at 6 53 03 PM" src="https://github.com/user-attachments/assets/f98d7599-c96d-43a3-bf29-dd71ff2db2ab" />
<img width="727" height="639" alt="Screenshot 2026-10-02 at 6 53 45 PM" src="https://github.com/user-attachments/assets/70d2ebd5-3d2b-4da9-be3f-e0e5178438a2" />




### CAD link:
[Fusion Link](https://a360.co/47AANnS)


### PCB screenshots:
<img width="1045" height="536" alt="Screenshot 2026-10-02 at 6 42 15 PM" src="https://github.com/user-attachments/assets/c155f6a4-0e33-41c7-bf8f-f2ad3fa92d6a" />
<img width="671" height="450" alt="Screenshot 2026-10-02 at 6 46 31 PM" src="https://github.com/user-attachments/assets/793f0c19-2b28-4be1-adcb-33df0abc25c6" />
<img width="622" height="347" alt="Screenshot 2026-10-02 at 6 46 49 PM" src="https://github.com/user-attachments/assets/ce54e2de-db3a-4f18-9b74-1cefbd538119" />





### Schematic:
1. Power Control:
<img width="1333" height="496" alt="Screenshot 2026-10-02 at 6 48 12 PM" src="https://github.com/user-attachments/assets/ba0b66d7-09e5-4471-95de-67fcb52c66f8" />

2. Safe shut
<img width="901" height="607" alt="Screenshot 2026-10-02 at 6 49 03 PM" src="https://github.com/user-attachments/assets/9739240b-6eea-4d34-a64b-ca96ecbdbd79" />

3. Duos_interface:
<img width="1150" height="682" alt="Screenshot 2026-10-02 at 6 50 06 PM" src="https://github.com/user-attachments/assets/a49aa986-8406-4b93-9f8d-e2b44016ac58" />







