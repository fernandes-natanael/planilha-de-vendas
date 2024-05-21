import os
from google.oauth2.service_account import Credentials

def get_credentials():
  scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    ]
  return Credentials.from_service_account_info({
      "type": os.getenv("SERVICE_ACCOUNT_TYPE"),
      "project_id": os.getenv("PROJECT_ID"),
      "private_key_id": os.getenv("PRIVATE_KEY_ID"),
      "private_key": os.getenv("PRIVATE_KEY"),
      "client_email": os.getenv("CLIENT_EMAIL"),
      "client_id": os.getenv("CLIENT_ID"),
      "auth_uri": os.getenv("AUTH_URI"),
      "token_uri": os.getenv("TOKEN_URI"),
      "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_CERT_URL"),
      "client_x509_cert_url": os.getenv("CLIENT_CERT_URL")
    }, scopes=scopes)