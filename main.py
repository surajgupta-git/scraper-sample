# https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=2&startPage=1
import bs4 as bs
import requests
import pandas as pd
import numpy as np

pages = np.arange(1,4)
job_entry = []
comp_name_entry = []
skills_entry = []
date_entry = []


for page in pages:

    urlPath = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0' \
              '&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate' \
              '=I&sequence='+str(page)+'&startPage=1 '

    html_text = requests.get(urlPath).text
    soup = bs.BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            jobName = job.find('h2').a.text.replace(' ','')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            job_entry.append(jobName.strip())
            comp_name_entry.append(company_name.strip())
            skills_entry.append(skills.strip())
            date_entry.append(published_date.strip())
            # print("Company Name: " + company_name.strip())
            # print("required_skills: "+ skills.strip())
            # print(' ')

    jobsTable = pd.DataFrame({
        'Job Title': job_entry,
        'Company Name': comp_name_entry,
        'Skills Required': skills_entry,
        'Published Date' : date_entry
    })

    jobsTable.to_csv('jobsOutput.csv')