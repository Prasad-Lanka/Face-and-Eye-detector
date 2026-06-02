from flask import Flask,render_template,Response
import cv2
app=Flask(__name__)
camera=cv2.VideoCapture(0)

detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade=cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
def generate_frames():
    while True:
        #read the cam frame
        success,frame=camera.read()
        if not success: #if cam not working break 
            break
        else:
         
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=detector.detectMultiScale(gray,1.1,7)

            #draw the rectangle around each face
            for (x,y,w,h) in  faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=frame[y:y+h,x:x+w]
                #for eyes
                eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



            ret,buffer=cv2.imencode('.jpg',frame)#encoding to jpg format
            frame=buffer.tobytes()
        yield (b'--frame\r\n'
       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    



@app.route("/")
def index():
    return render_template("index_vid.html")

@app.route("/video")
def video():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

if __name__ == "__main__":
    app.run(debug=True, port=5005)