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
```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. The video feed from the default camera will be displayed. When motion is detected, an image will be saved in the `images/` directory, and an email notification with the image attached will be sent.

3. Press `q` to exit the script.


## Notes

- **Email Provider:** The system is currently configured to work with Gmail. If you're using this setup, make sure you're sending notifications with a Gmail account.
  
- **Email Credentials:** Hardcoding email credentials in the script is not a secure practice. It's strongly recommended to use environment variables, a configuration file, or another secure method to store and retrieve your credentials. If you choose to use this script as-is, ensure it's kept in a secure environment and isn't shared or stored in a public place.

- **Less Secure Apps:** For Gmail to work with this script, you might need to allow [less secure apps](https://support.google.com/accounts/answer/185833?hl=en) to access your account. However, be aware that this can make your Gmail account more vulnerable. Consider creating a dedicated Gmail account for this purpose or exploring other email providers or services that offer more secure methods of sending emails programmatically.
