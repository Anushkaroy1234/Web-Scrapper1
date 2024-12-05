from db import get_connection
from logger_setup import set_logger

logger=set_logger()

"""
create table if not exists scrapper1(
	id int auto_increment primary key,
    url varchar(500) ,
    title varchar(500),
    inserted_at timestamp default current_timestamp
);
"""

def insert_news(url:str,title:str)->dict:
    try:
        con,cursor=get_connection()
        query="""
            Insert into scrapper1(url,title) values("%s","%s")
        """%(url,title) # --> parameterized query = sql injection safe
        cursor.execute(query)
        con.commit()
        return {
            "URL":url,
            "Title":title
        }
    except Exception as e:
        logger.error("insert_news() | "+str(e))
        con.rollback()
        return {}
    
if __name__=="__main__":
    res=insert_news("h1","d1")
    print(res)