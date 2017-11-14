from .. import db


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    bosszhipin_companyid = db.Column(db.Integer, index=True, doc=u'在BOSS直聘上的ID')
    name = db.Column(db.String(64), doc=u'公司名称')
    url = db.Column(db.String(64), doc=u'公司网址')
    finance_stage = db.Column(db.Integer, doc=u'融资阶段')
    industry = db.Column(db.Integer, doc=u'所属行业')
    size = db.Column(db.SmallInteger, doc=u'公司规模')
    introduce = db.Column(db.Text(), doc=u'公司简介')
    manager_list = db.Column(db.Text(), doc=u'高管介绍')
