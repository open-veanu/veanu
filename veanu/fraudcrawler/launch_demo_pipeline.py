import logging
import os

from dotenv import load_dotenv

from veanu import LOG_FMT
from veanu.fraudcrawler.settings import LOG_LEVEL
from veanu.fraudcrawler.src.client import FraudCrawlerClient

logging.basicConfig(
    level=LOG_LEVEL.upper(), format=LOG_FMT, datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
_SERPAPI_KEY = os.getenv("SERPAPI_KEY")
_ZYTEAPI_KEY = os.getenv("ZYTEAPI_KEY")
_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Instantiate the client
client = FraudCrawlerClient(
    serpapi_key=_SERPAPI_KEY,
    zyteapi_key=_ZYTEAPI_KEY,
    openai_api_key=_OPENAI_API_KEY,
    location="Switzerland",
)

# Perform sequential search
df = client.run("sildenafil", num_results=10)
print(df.head())
