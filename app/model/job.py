from app import db


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    bosszhipin_jobid = db.Column(db.Integer, index=True, doc=u'在BOSS直聘上的ID')
    title = db.Column(db.String(64), doc=u'职位标题')
    work_year = db.Column(db.SmallInteger, doc=u'工作年限要求')
    city_id = db.Column(db.Integer, doc=u'城市 id')
    job_tag = db.Column(db.String(128), doc=u'职位标签')
    company_id = db.Column(db.Integer, doc=u'公司 id')
    salary = db.Column(db.String(32), doc=u'薪水')
    education = db.Column(db.SmallInteger, doc=u'教育背景要求')
    job_description = db.Column(db.Text(), doc=u'职位描述')
    team_description = db.Column(db.Text(), doc=u'团队介绍')
    address = db.Column(db.String(128), doc=u'工作地址')
    boss_name = db.Column(db.String(32), doc=u'招聘者姓名')
    boss_job = db.Column(db.String(32), doc=u'招聘者职位')
    created_day = db.Column(db.String(32), doc=u'职位发布日期')