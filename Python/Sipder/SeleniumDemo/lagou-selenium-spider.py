from selenium import webdriver
from lxml import etree
import time

class LagouSpider(object):
    def __init__(self):
        self.url="https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        self.driver = webdriver.Chrome()
        self.positions=[]

    def run(self):
        self.driver.get(self.url)
        body_btn = self.driver.find_element_by_class_name("body-btn")
        body_btn.click()
        while True:
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            #next_btn = self.driver.find_element_by_class_name("pager_next ")
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(5)
        time.sleep(10)
        
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
            
        
    def request_detail_page(self,url):
        #self.driver.get(url)
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//div[@class='job-name']/@title")[0]
        company_name = html.xpath("//h4[@class='company']/text()")[0]
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        position = {
            'name':position_name,
            'company_name':company_name,
            'detail':desc
        }
        print(position)
        self.positions.append(position)
        
        
def main():
    spider = LagouSpider()
    spider.run()

if __name__ == "__main__":
    main()