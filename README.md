# Motion Detection and Notification System

This system captures video feed from the default camera, detects object, captures images of the detected object, and sends an email notification with the captured image attached.

## Features
- Real-time video capture and motion detection.
- Email notification with an attached image of the detected motion.
- Periodic cleanup of captured images.

## Requirements

1. Python 3.x
2. OpenCV: Used for video capture and motion detection.
3. smtplib: Required for sending emails.

## Setup

1. **Clone this repository**:

2. **Install required packages**:

3. **Update the `emailing.py` file with your email credentials**:
Replace `YOUR EMAIL HERE` and `YOUR PASSWORD HERE` with your actual email and password.
```python
MY_EMAIL = "YOUR EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"
