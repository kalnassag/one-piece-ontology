"""
Configuration file for One Piece Scraper
"""

# Scraping Configuration
BASE_URL = "https://onepiece.fandom.com/wiki/"
CANON_CHARACTERS_URL = "https://onepiece.fandom.com/wiki/List_of_Canon_Characters"

# Rate Limiting
DEFAULT_DELAY = 3  # seconds between requests
DEFAULT_BATCH_SIZE = 50  # characters per batch file

# Paths
DATA_DIR = "data"
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
OUTPUT_DIR = "output"
PROGRESS_DIR = "output/progress"

# File Names
CHARACTER_LIST_FILE = "data/raw/canon_character_list.txt"
OUTPUT_FILE = "output/characters.json"
FAILURES_FILE = "output/scraping_failures.json"

# Scraper Settings
USE_SELENIUM = False  # Set to True to use Selenium by default
HEADLESS_MODE = True  # Run browser in headless mode
MAX_RETRIES = 3  # Number of retry attempts per character
REQUEST_TIMEOUT = 30  # seconds

# User Agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Target Sections (which infobox sections to scrape)
TARGET_SECTIONS = ['Statistics', 'Portrayal']

# Devil Fruit Configuration
DEVIL_FRUIT_CATEGORIES = [
    "https://onepiece.fandom.com/wiki/Category:Paramecia",
    "https://onepiece.fandom.com/wiki/Category:Zoan",
    "https://onepiece.fandom.com/wiki/Category:Logia",
]
DEVIL_FRUIT_TARGET_SECTIONS = ['Statistics']
DEVIL_FRUIT_LIST_FILE = "data/raw/canon_devil_fruit_list.txt"
DEVIL_FRUIT_OUTPUT_FILE = "output/devil_fruits.json"
DEVIL_FRUIT_PROGRESS_DIR = "output/devil_fruit_progress"
DEVIL_FRUIT_FAILURES_FILE = "output/devil_fruit_scraping_failures.json"
