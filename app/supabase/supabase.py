# imports
import os
from supabase import create_client, Client

# Get the Environment Variables
url: str = os.getenv("SUPABASE_URL")
api_key: str = os.getenv("SUPABASE_KEY")

# Initialize the supabase client for the project
supabase: Client = create_client(url, api_key)