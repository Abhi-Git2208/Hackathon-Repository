import cv2 as cv
import winsound as ws
import concurrent.futures as cf

def show_cam(cam_id):
    cam = cv.VideoCapture(cam_id)
    while cam.isOpened():
        ret, frame0 = cam.read()
        ret, frame1 = cam.read()                # We read 2 consecutive frames and take the
        diff = cv.absdiff(frame0, frame1)       # difference between the frames to detect movement
        
        # We edit the difference between the frames stored in the variable "diff" and make it more clear and solid to detect easily
        gray = cv.cvtColor(diff, cv.COLOR_RGB2GRAY)
        blur = cv.GaussianBlur(gray, (7,7), 0)
        _, thresh = cv.threshold(blur,30,1000,cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations = 3)
        contours, cp = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # We add contours around the part where the difference occured between the two frames 
        for c in contours:
            # This is the sensitivity measure used to filter out minor movements
            if cv.contourArea(c) < 500:
                continue

            # We get the x and y coordinates of the movement occurance and bound it with an additional width of w and height h
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(frame1, (x,y), (x+w,y+h), (100,100,255), 2)

            # This is a Beep sound inbuilt in the python library which is best used for testing as u don't wanna be testng with such loud sound as the alarm.wav file given
            # ws.Beep(500,200)   
            ws.PlaySound('alarm.wav',ws.SND_ASYNC)

        if cv.waitKey(1) == ord('c'):
            cv.destroyAllWindows()
            return("Camera Closed")
        cv.imshow(f"Camera{cam_id}",frame1)

# MULTIPROCESSING PART

a = int(input("ENTER THE NO. OF CAMERAS TO OPERATE : ")) # Enter only the no. of cameras ur system possesses

with cf.ProcessPoolExecutor() as exe:
    if __name__ == '__main__':
        # Make each call of the function into a process to call the processes concurrently
        processes = [exe.submit(show_cam, i) for i in range(a)]

        for p in processes:
            p.result()
