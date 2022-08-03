#change attribute

class Email:
    def __init__(self):
        self.send = False
    def send_email(self):
        self.send = True

my_email = Email()

#print(my_email.send)
my_email.send_email()
print(my_email.send)