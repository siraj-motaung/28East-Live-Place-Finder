import live_place_finder.config as config
import pymysql


config = config.Config()

def get_connection(database: str):

    # return pymysql.connect(
    #     host=config.DB_HOST,
    #     port=config.DB_PORT,
    #     user=config.DB_USER,
    #     password=config.DB_PASSWORD,
    #     database=database,
    #     cursorclass=pymysql.cursors.DictCursorb

    # )

    return pymysql.connect(
    host="127.0.0.1",  # Localhost (your own machine)
    port=3306,
    user="root",
    password="moraj",
    database=database,
    cursorclass=pymysql.cursors.DictCursor  # Optional: returns dictionary rows instead of tuples
)
