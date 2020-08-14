import smtplib
class deliver:
    def deliver_process(id):
        print("ID",id)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("yassataiseer@gmail.com", "FILE.exe123")
        server.sendmail(
            "yassataiseer@gmail.com",id,"thank you for signing up for Codnect we will send you daily emails of players you may want to play with")
        print("email sent")