import sys
from pathlib import Path

# Add the path to your Flask application
app_path = Path(__file__).parent.absolute()
sys.path.insert(0, str(app_path))

# Import your Flask application object
from scraper import app as application
