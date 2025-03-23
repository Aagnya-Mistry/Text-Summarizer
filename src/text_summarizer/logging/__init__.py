import os
import sys
import logging

# Corrected logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s - %(message)s]"

# Directory for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Logger instance
logger = logging.getLogger("text_summarizer_logger")

