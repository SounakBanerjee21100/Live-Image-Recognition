import tkinter as tk
from PIL import Image, ImageTk
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

window = tk.Tk()
window.title("Face Detection")
window.geometry("680x500")
window.resizable(0,0)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

label = tk.Label(window)
label.pack()

def update_frame():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(10, update_frame)

update_frame()
quit_btn = tk.Button(window, text="Quit", command=window.destroy)
quit_btn.pack()
window.mainloop()
cap.release()
cv2.destroyAllWindows()
