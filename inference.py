import cv2
import os

def run_detection():
    # Load pre-trained face detector (OpenCV built-in)
    model_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    # face_cascade = cv2.namedWindow('test') # Just to check OpenCV init
    face_cascade = cv2.CascadeClassifier(model_path)

    # Load an image (make sure to add 'input.jpg' to your repo!)
    img = cv2.imread('faces.jpg')
    if img is None:
        print("Error: Could not find input.jpg")
        return

    print(f"Image Resolution: {img.shape[1]}x{img.shape[0]}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print(f"Detected {len(faces)} faces.")

    # Draw rectangles and save
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imwrite('output.jpg', img)
    print("Inference complete. Saved to output.jpg")

if __name__ == "__main__":
    run_detection()