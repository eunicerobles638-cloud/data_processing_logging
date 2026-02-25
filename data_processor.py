import logging

logging.basicConfig(filename='process.log', level=logging.INFO, 
format='%(asctime)s - %(levelname)s - %(message)s')

print("Starting the Black Sheep Data Processor...")
logging.info("Script started successfully.")

print("Proccessing data...")
logging.info("Task: Cleaning CSV data - Status: In Progress")

print("Done! Check progress.log for details.")
logging.info("Script Finished Work.")
