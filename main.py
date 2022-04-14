import cv2
import handTracker as ht
import fingerCounter as fc

hand_tracker = ht.handTracker()
finger_counter = fc.FingerCounter()

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.rectangle(frame, (10,10), (250,30), (255,255,255), cv2.FILLED)
    cv2.putText(frame, 'Project Finger Counting', (15,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
    if ret:
        hands = hand_tracker.findHands(frame)
        if hands:
            oneHand = hands[0]
            first_five = finger_counter.fingerOrientation(oneHand)

            if (len(hands) == 2):
                secondHand = hands[1]
                second_five = finger_counter.fingerOrientation(secondHand)
                cv2.rectangle(frame, (10,50), (245,200), (55,245,10), cv2.FILLED)
                cv2.putText(frame, str(first_five + second_five), (65,175), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 20)
            else:
                cv2.rectangle(frame, (40,50), (200,200), (55,245,10), cv2.FILLED)
                cv2.putText(frame, str(first_five), (75,175), cv2.FONT_HERSHEY_COMPLEX, 4, (0,0,0), 20)
        cv2.imshow("Framing", frame)

    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()