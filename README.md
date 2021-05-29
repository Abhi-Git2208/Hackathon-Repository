# Python Image Processing To Solve Animal Attacks in Farm Lands

This program uses the OpenCV module in Python.
It gives a good solution to safe guard farm lands from animals and imposters and KEEP THE FARMERS PRODUCE SAFE. 

NOTE : This program is just to show how the idea works efficiently. It is not suitable to implement this as such in any farm land without addition of required hardware and software components that are necessary.

It basically makes use of the web cameras available presently and uses them to detect movement. The program is made in such a way that the number of cameras can be extended according to the requirement.

The cameras are initially set up in a manner such that they remain still without movement of any sort.

# How To Run the Program

Download the ALARM and the PROGRAM FILE in the same folder.
Make sure that the library openCV is installed in the system before running this program.

Initially when the program is run, it will ask for the number of cameras to be operated with. The user has to give the number of webcams which is presently connected to their PC.
Once this is given the Program opens up as many cameras given by the user and reads the frames through them.

If there is movement of any sort, the part of movement immediately gets covered by RED CONTOURS and the ALARM goes ON.

To exit the program the user can press the 'c' button in the keyboard to close the cameras one by one.

# How The Code Functions

The capture of each camera is taken and 2 consecutive frames are extracted. The absolute difference of the frmaes is taken and is edited to intensify the difference to make it significant enough to be detected.
If the difference between the frame contributes to a significant amount, the x and y co-ordinates of the movements are taken and a RED RECTANGULAR CONTOUR is drawn around it and sounds the ALARM to signify the movement.

This ALARM is supposed to alert the Farmers and scare the animal simulataneously. If the animal has not yet run away, the farmer can immediately check that in the monitor and do the needful before his crops get damaged. 

The code has a SENSITIVITY measure which ignores insignificant movements like movement of trees and plants or movement of any animal or bird very far away from the survey zone of the camera.
