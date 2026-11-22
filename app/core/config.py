
import os
from dotenv import load_dotenv

# Load environment variables from the project root .env file
load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "ManufactureFlow AI")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Zoho configuration
    ZOHO_ACCOUNTS_URL: str = os.getenv(
        "ZOHO_ACCOUNTS_URL",
        "https://accounts.zoho.in"
    )

    ZOHO_CRM_API_DOMAIN: str = os.getenv(
        "ZOHO_CRM_API_DOMAIN",
        "https://www.zohoapis.in"
    )

    # AI configuration
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")


settings = Settings()
