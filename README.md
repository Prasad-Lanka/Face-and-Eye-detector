# Face-and-Eye-detector
A Flask-based real-time face and eye detection web application using OpenCV Haar Cascade classifiers. The app captures live webcam video, detects faces and eyes, and streams the processed output directly to the browser.
# Face & Eye Detection Web Application

A real-time Face and Eye Detection Web Application built using Flask and OpenCV. The application captures live webcam video, detects faces and eyes using Haar Cascade Classifiers, and streams the processed output directly to a web browser.

## Features
- Real-time webcam streaming
- Face detection using OpenCV
- Eye detection within detected faces
- Browser-based interface using Flask
- Live bounding box visualization

## Technologies Used
- Python
- Flask
- OpenCV
- NumPy
- HTML

## Installation

```bash
pip install flask opencv-python numpy
python face_detect.py
```

Open:

```text
http://127.0.0.1:5005/
```

## Project Structure

```text
face-eye-detection/
├── face_detect.py
├── templates/
│   └── index_vid.html
└── Haarcascades/
```

## Future Improvements
- Face Recognition
- Attendance System
- Database Integration
- Cloud Deployment

## Author
**Prasad Lanka**  
CSE-AIML Student
