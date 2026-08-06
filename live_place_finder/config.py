import os
import logging

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "")


    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    @classmethod
    def setup_logging(cls):
        logging.basicConfig(level=cls.LOG_LEVEL, 
                            format=cls.LOG_FORMAT,
                            force=True  # Overrides any default handlers set by dependencies
                            )

        logger = logging.getLogger(__name__)
        logger.info("Logging initialized at %s level", cls.LOG_LEVEL)
   

