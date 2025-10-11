import os 
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s:%(module)s: %(message)s]"

log_dir = 'logs'

log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath), # Sends messages to disk files.
        logging.StreamHandler(sys.stdout) # Sends messages to streams (file-like objects- it prints the log on my terminal too).
    ]
)


logger = logging.getLogger('cnnClassifierLogger')