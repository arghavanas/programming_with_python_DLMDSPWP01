import os
from sqlalchemy import create_engine

# Use environment variables for paths (set in Dockerfile or docker-compose)
DATA_PATH = os.getenv("DATA_PATH", "./data")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "./output")

# File paths
TRAIN_FILE = os.path.join(DATA_PATH, "train.csv")
IDEAL_FILE = os.path.join(DATA_PATH, "ideal.csv")
TEST_FILE = os.path.join(DATA_PATH, "test.csv")

# Database connection
DATABASE_URI = "sqlite:///ideal_functions.db"
ENGINE = create_engine(DATABASE_URI, echo=False)
