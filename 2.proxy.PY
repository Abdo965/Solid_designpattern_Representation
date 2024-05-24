class RealSubject:
  """The real object with functionality (protected resource)."""
  def __init__(self, data):
    self.data = data

  def get_sensitive_data(self):
    print("Accessing sensitive data:", self.data)

class SecurityProxy(RealSubject):
  """The security proxy controlling access to the real object."""
  def __init__(self, real_subject, username, password):
    super().__init__(real_subject.data)  # Inherit data
    self.real_subject = real_subject
    self.username = username
    self.password = password
    self.authenticated = False

  def authenticate(self, username, password):
    if username == self.username and password == self.password:
      self.authenticated = True
      print("Authentication successful.")
    else:
      self.authenticated = False
      print("Authentication failed.")

  def get_sensitive_data(self):
    if self.authenticated:
      return super().get_sensitive_data()  # Call parent's method
    else:
      print("Access denied: Not authenticated.")


# Usage
real_subject = RealSubject("Top Secret Information")
proxy = SecurityProxy(real_subject, "authorized_user", "secret_password")

# Try accessing data without authentication
proxy.get_sensitive_data()  # Output: Access denied: Not authenticated.

# Authenticate and then access data
proxy.authenticate("authorized_user", "secret_password")
proxy.get_sensitive_data()  # Output: Authentication successful. Accessing sensitive data: Top Secret Informa