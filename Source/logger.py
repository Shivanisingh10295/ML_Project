
import logging
import os
from datetime import datetime

# Generate the log file name
Log_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the 'logs' directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Define the path for the log file
LOG_FILE_PATH = os.path.join(log_dir, Log_File)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Use logging.INFO instead of logging.info
)

