# Computer_Vision_Detect_Video
A simple video player using OpenCV

SIMPLE BREAKDOWN:

1). The line  -- cap = cv2.VideoCapture(0) -- captures the videousing openCV, and stores in cap. 

2). The below code then rune while the boolean is True (which is always is).

    Then, it reads for cap object and emits 2 variables, a. ref (a boolean) and b. single video frame (an image)
3). if the ref is true, meaning if there is another frame in wait after the current one, then read the current one. else break the loop (stop the video).

4). The k variable is assigned a value of the 'q' key, and if the q key is pressed while the  video is being played, then it will break the frame loop, and the program will stop running, and the line -- cv2.destroyAllWindows() -- will be executed, and close the video window.
