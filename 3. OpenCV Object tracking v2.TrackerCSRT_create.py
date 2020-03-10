import time
import cv2
tracker = cv2.TrackerKCF_create()

OPENCV_OBJECT_TRACKERS = { "csrt": cv2.TrackerCSRT_create, "kcf": cv2.TrackerKCF_create, "boosting": cv2.TrackerBoosting_create, "mil": cv2.TrackerMIL_create,
"tld": cv2.TrackerTLD_create, "medianflow": cv2.TrackerMedianFlow_create,"mosse": cv2.TrackerMOSSE_create}
tracker = cv2.TrackerCSRT_create()

initBB = None 
vs = cv2.VideoCapture(0) 
while True:
 (grabbed, frame) = vs.read()
 if initBB is not None:
  (success, box) = tracker.update(frame)  

  if success:
   (x, y, w, h) = [int(v) for v in box]
   cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 1)

  info = [("Type of tracking", str(tracker)),("Object was Found", "Yes" if success else "No")]
  cv2.putText(frame, str(info[0]), (10, 360), cv2.FONT_ITALIC, 0.3, (0, 255, 0), 1)
  cv2.putText(frame, str(info[1]), (10, 340), cv2.FONT_ITALIC, 0.3, (0, 255, 0), 1)
 cv2.imshow("Frame", frame)
 key = cv2.waitKey(1) & 0xFF

 if key == ord("s"):
  initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True) #  1 showCrosshair - ?
  tracker.init(frame, initBB) 
 elif key == ord("q"):
  break
cv2.destroyAllWindows()
