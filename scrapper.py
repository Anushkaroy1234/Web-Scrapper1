import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self) -> None:
        self.url="https://timesofindia.indiatimes.com/sports"
        self.data=[]
    
    def __hit_endpoint(self):
        try:
            req=requests.get(self.url)
            return req.content
        
        except Exception as e :
            print('hit_endpoint',str(e))

    def scrap(self):
        try:
            content=self.__hit_endpoint()
            b=BeautifulSoup(content,'html.parser')
            for div in b.find_all(class_='iN5CR'):
                if div!=None:
                    a_tag = div.find('a', href=True)
                    url = a_tag['href'] if a_tag else 'No URL'
                    #print(url)
                    title_div = div.find('div', class_='WavNE undefined')
                    title = title_div.text.strip() if title_div else 'No Title'
                    #print(title)
                    self.data.append({
                        'URL':url,
                         "Title":title,
                    })

                else:
                    print("Method did't work properly")
    
           
        except Exception as e:
            print(' scrap()',str(e))

        return self.data
   


if __name__ == "__main__":
    s=Scrapper() 
    print(s.scrap())
    print("Scheduler is running. Waiting for the next scheduled job...")
   