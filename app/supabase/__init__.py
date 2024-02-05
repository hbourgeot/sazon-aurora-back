# imports
import os
from supabase import create_client, Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Get the Environment Variables
url: str = os.getenv("SUPABASE_URL")
api_key: str = os.getenv("SUPABASE_KEY")

# Initialize the supabase client for the project
supabase: Client = create_client(url, api_key)

