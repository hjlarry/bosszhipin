from app.util.Downloader import HtmlDownloader
from app.util.Parser import HtmlParser
from app.util.DataProcess import DataProcess
from common import constants


class SpiderWorker(object):
    def __init__(self, url=constants.HOME_URL):
        self.url = url
        self.download = HtmlDownloader(self.url).make_request()
        self.parser = HtmlParser(self.download)

    def career_spider(self):
        careers = self.parser.career_parser()
        return careers

    def job_spider(self):
        self.parser.job_parser()
        data = DataProcess(self.parser.job)
        data.update_job_main_content()

    def job_des_spider(self):

        job_id = DataProcess.get_uncrawl_job_des()
        self.url = constants.HOME_URL+'/job_detail/'+job_id+'.html'
        self.parser.job_description_parser()
        self.parser.job_des['job_id'] = job_id

        data = DataProcess(self.parser.job_des)
        data.update_job_description()
        DataProcess.set_crawled_job_all(job_id)

    def city_spider(self, update_db=True):
        self.parser.city_parser()
        if not update_db:
            return self.parser.city
        data = DataProcess(self.parser.city)
        data.update_city()

    def company_spider(self):
        com_id = DataProcess.get_uncrawled_com()
        self.url = constants.HOME_URL+'/gongsi/'+com_id+'.html'
        self.parser.company_parser()
        self.parser.company['bosszhipin_companyid'] = com_id

        data = DataProcess(self.parser.company)
        data.update_company()
        DataProcess.set_crawled_com(com_id)
