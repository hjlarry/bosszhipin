import time

from app import db
from .Decorator import db_commit_decorator
from app.model.job import Job
from app.model.city import City
from app.model.company import Company
from common.config import uncrawl_job_des, crawled_job_des, uncrawl_com, crawled_com, REDIS_CONF



class DataProcess(object):
    def __init__(self, data_object):
        self.data = data_object

    @db_commit_decorator
    def update_job_main_content(self):
        for data in self.data:
            if self.has_crawled_job_main(data['boss_zhipin_id']):
                continue
            city_id = City.query.filter_by(name=data['city']).first().id
            new_job = Job(
                title=data['title'],
                city_id=city_id,
                work_year=data['work_year'],
                job_tag=','.join(data['job_tag']),
                company_id=data['company_zhipin_id'],
                salary=data['salary'],
                education=data['education'],
                boss_name=data['boss_name'],
                boss_job=data['boss_job'],
                created_day=data['created_day'],
                bosszhipin_jobid=data['boss_zhipin_id']
            )
            db.session.add(new_job)
            self.set_crawled_job_main(data['boss_zhipin_id'])
            self.send_crawl_com(data['company_zhipin_id'])
        db.session.commit()

    @staticmethod
    def has_crawled_job_main(job_id):
        return uncrawl_job_des.exists(job_id) or crawled_job_des.exists(job_id)

    @staticmethod
    def has_crawled_job_des(job_id):
        return uncrawl_job_des.exists(job_id)

    @staticmethod
    def has_crawled_job_all(job_id):
        return crawled_job_des.exists(job_id)

    @staticmethod
    def set_crawled_job_main(job_id):
        uncrawl_job_des.set(job_id, int(time.time()))

    @staticmethod
    def set_crawled_job_all(job_id):
        uncrawl_job_des.move(job_id, REDIS_CONF['crawled_job_des'])

    @staticmethod
    def get_uncrawl_job_des():
        return uncrawl_job_des.randomkey()

    @staticmethod
    def has_crawled_com(com_id):
        return uncrawl_com.exists(com_id) or crawled_com.exists(com_id)

    @staticmethod
    def set_crawled_com(com_id):
        uncrawl_com.move(com_id, REDIS_CONF['crawled_com'])

    @staticmethod
    def get_uncrawled_com():
        return uncrawl_com.randomkey()

    @staticmethod
    def send_crawl_com(com_id):
        uncrawl_com.set(com_id, int(time.time()))

    @db_commit_decorator
    def update_job_description(self):
        job = Job.query.get(self.data['job_id'])
        job.job_description = '\n'.join(self.data['job_description'])
        job.team_description = '\n'.join(self.data['team_description'])
        job.address = self.data['address']
        db.session.add(job)
        db.session.commit()

    @db_commit_decorator
    def update_city(self):
        for data in self.data:
            exist = City.query.get(data['city_id'])
            if exist:
                continue
            else:
                new_city = City(id=data['city_id'], name=data['city_name'])
                db.session.add(new_city)
        db.session.commit()

    @db_commit_decorator
    def update_company(self):
        new_company = Company(
            bosszhipin_companyid=self.data['bosszhipin_companyid'],
            name=self.data['name'],
            url=''.join(self.data['url']),
            finance_stage=self.data['finance_stage'],
            industry=self.data['industry'],
            size=self.data['size'],
            introduce=''.join(self.data['introduce'])
        )
        db.session.add(new_company)
        db.session.commit()