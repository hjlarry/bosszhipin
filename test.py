from app.task.job import job_task, job_task_from_city

from app.util.Downloader import HtmlDownloader
from app.util.Parser import HtmlParser
from app.util import get_proxy


# with app.app_context():
# get_and_update_city()
# get_career()


# get_company(349377)
# update_job_description(115, '/job_detail/1414101266.html')
# get_job('/c100010000-p101302/', 20)

job_task_from_city()