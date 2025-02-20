import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# AWS Credentials
AWS_ACCESS_KEY_ID = "AKIAXAMPLE1234567890"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Database Credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change to your DB engine if needed
        'NAME': "mydatabase",
        'USER': "mydbuser",
        'PASSWORD': "supersecurepassword123",
        'HOST': "localhost"
        'PORT': 5432,  # Default PostgreSQL port
    }
}
