# Example demonstrating Dependency Inversion Principle

# High-level module defining a Notifier interface
class Notifier:
    def __init__(self, messenger):
        self.messenger = messenger

    def send_notification(self, message):
        self.messenger.send(message)

# Low-level module defining a Messenger interface
class Messenger:
    def send(self, message):
        pass

# Concrete implementation of Messenger for email
class EmailMessenger(Messenger):
    def send(self, message):
        print(f"Sending email: {message}")

# Concrete implementation of Messenger for SMS
class SMSMessenger(Messenger):
    def send(self, message):
        print(f"Sending SMS: {message}")

# Usage
if __name__ == "__main__":
    # Creating instances of messengers
    email_messenger = EmailMessenger()
    sms_messenger = SMSMessenger()

    # Creating instances of notifier
    email_notifier = Notifier(email_messenger)
    sms_notifier = Notifier(sms_messenger)

    # Sending notifications
    email_notifier.send_notification("Hello, this is an email notification.")
    sms_notifier.send_notification("Hello, this is an SMS notification.")
