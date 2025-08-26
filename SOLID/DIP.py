from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send_email(self):
        ...
        
class GmailClient(EmailClient):
    def send_email(self):
        print("Sent email using gmail")
        
class EmailService:
    def __init__(self, email_client:EmailClient):
        self.email_client = email_client
        
    def send_email(self):
        self.email_client.send_email()
        
if __name__ == "__main__":
    gmail = GmailClient()
    email_service = EmailService(gmail)
    email_service.send_email()
        
    