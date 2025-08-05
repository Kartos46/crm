import os
from dotenv import load_dotenv

load_dotenv()
print("ENV_TYPE:", os.environ.get("ENV_TYPE"))