from common import constants
import time
from copy import deepcopy
from .Decorator import parse_decorator


class HtmlParser(object):
    def __init__(self, etree):
        self.tree = etree
        self.job = []
        self.career = set()
        self.job_des = dict()
        self.city = []
        self.company = dict()

    @parse_decorator([])
    def job_parser(self):
        content = self.tree.xpath('//div[@class="job-primary"]')
        for c in content:
            detail_url = c.xpath('.//a[contains(@href, "job_detail")]/@href')[0]
            boss_zhipin_id = detail_url.split('.')[0].split('/')[-1]
            title = c.xpath('.//a[contains(@href, "job_detail")]/text()')[0]
            city = c.xpath('./div/p/text()')[0]
            work_year = c.xpath('./div/p/text()')[1]
            education = c.xpath('./div/p/text()')[2]
            job_tag = c.xpath('./following-sibling::*[1]/span/text()')
            boss_name = c.xpath('./following-sibling::*[1]/div/p/text()')[0]
            boss_job = c.xpath('./following-sibling::*[1]/div/p/text()')[1]
            salary = c.xpath('.//a[contains(@href, "job_detail")]/span/text()')[0]
            company_url = c.xpath('.//div[@class="company-text"]/h3/a/@href')[0]
            company_zhipin_id = company_url.split('.')[0].split('/')[-1]

            # 通过处理得到job正确的发布日期
            created_day = c.xpath('./following-sibling::*[2]/span/text()')
            created_day = created_day[0] if created_day else '发布于unknown'
            if ":" in created_day:
                created_day = time.strftime('%m月%d日', time.localtime())
            elif "昨天" in created_day:
                created_day = time.strftime('%m月%d日', time.localtime(time.time() - 60 * 60 * 24))
            else:
                created_day = created_day.strip('发布于')
            job = {
                'boss_zhipin_id': boss_zhipin_id,
                'title': title,
                'city': city,
                'work_year': constants.WORK_YEARS_REQUEST_DICT[work_year],
                'education': constants.EDUCATION_REQUEST_DICT[education],
                'job_tag': job_tag,
                'salary': salary,
                'boss_name': boss_name,
                'boss_job': boss_job,
                'company_zhipin_id': company_zhipin_id,
                'created_day': created_day,
                'url': detail_url
            }

            self.job.append(job)
        return self.job

    @parse_decorator(())
    def career_parser(self):
        # 通过获取首页的职业列表，进而去分发爬取任务
        content = self.tree.xpath('//a[contains(@ka, "cpc_side")]')
        for c in content:
            self.career.add(c.xpath('@href')[0])
        return self.career

    @parse_decorator({})
    def job_description_parser(self):
        content = self.tree.xpath('//div[@class="job-sec"]')
        self.job_des['job_description'] = content[0].xpath('./div/text()')
        self.job_des['team_description'] = content[1].xpath('./div/text()') if len(content) == 3 else ''
        self.job_des['address'] = self.tree.xpath('//div[@class="location-address"]/text()')[0]
        return self.job_des

    @parse_decorator([])
    def city_parser(self):
        content = self.tree.xpath('//div[@class="dorpdown-city"]/ul/li')
        new_city = dict()
        for c in content:
            new_city['city_id'] = c.xpath('./@data-val')[0]
            new_city['city_name'] = c.xpath('./text()')[0]
            self.city.append(deepcopy(new_city))
        return self.city

    @parse_decorator({})
    def company_parser(self):
        info = self.tree.xpath('//div[@class="info-primary"]')
        self.company['name'] = info[0].xpath('./h3/text()')[0]
        p = info[0].xpath('./p')
        self.company['url'] = p[-1].xpath('./text()')
        # 有的公司介绍页中没有填是第几轮
        if len(p[0].xpath('./text()')) == 3:
            finance_stage = p[0].xpath('./text()')[-3]
            self.company['finance_stage'] = constants.FINANCE_STAGE_DICT['unknown'] if finance_stage not in constants.FINANCE_STAGE_DICT.keys() else constants.FINANCE_STAGE_DICT[finance_stage]
        else:
            self.company['finance_stage'] = constants.FINANCE_STAGE_DICT['unknown']
        size = p[0].xpath('./text()')[-2]
        self.company['size'] = constants.COMPANY_SIZE_DICT['unknown'] if size not in constants.COMPANY_SIZE_DICT.keys() else constants.COMPANY_SIZE_DICT[size]
        industry = p[0].xpath('./text()')[-1]
        self.company['industry'] = constants.INDUSTRY_DICT['unknown'] if industry not in constants.INDUSTRY_DICT.keys() else constants.INDUSTRY_DICT[industry]
        self.company['introduce'] = self.tree.xpath('//div[@class="text fold-text"]/text()')
        return self.company
