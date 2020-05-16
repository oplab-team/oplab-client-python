class Error(Exception):
  pass

class WrongCredentialsError(Error):
  """Exception raised for when the login credentials are wrong.

  Attributes:
      message -- explanation of the error
  """

  def __init__(self, message = 'You must use valid credentials to login!'):
    super().__init__(message)
    self.message = message

class NotLoggedInError(Error):
  """Exception raised for login errors.

  Attributes:
      message -- explanation of the error
  """

  def __init__(self, message = 'You must first login with a valid email and password using method login(email, password).'):
    super().__init__(message)
    self.message = message
