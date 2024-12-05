from controller import insert_news
from scrapper import Scrapper
from logger_setup import set_logger
import schedule
import time
logger=set_logger()

def scrape_and_insert():
    sc=Scrapper()
    news=sc.scrap()

    for index,n in enumerate(news):
        res=insert_news(
            url=n.get('URL'),
            title=n.get('Title')
        )
        logger.info(f"====== {index+1} DATA INSERTED ====== {res}")

def start_scheduler():
    schedule.every().day.at("04:00").do(scrape_and_insert)

    while True:
        schedule.run_pending()
        time.sleep(5)



if __name__=="__main__":
    scrape_and_insert()
    start_scheduler()