import smtplib
import imghdr

from email.message import EmailMessage


MY_EMAIL = "MY EMAIL"
MY_PASSWORD = "password"
def send_email(image_path):
    print("send_email function started")

    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")


    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(MY_EMAIL,MY_PASSWORD)
    gmail.sendmail(MY_EMAIL, "satvik.ahuja2004@gmail.com", email_message.as_string())
    gmail.quit()
    print("clean_folder function ended")



if __name__ == "__main__":
    send_email(image_path="images/6.png")
