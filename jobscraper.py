import time
import os
from bs4 import BeautifulSoup
from jobposting import JobPosting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode

class JobScraper:

    def __init__(self, search_term, location, num_postings=1000, sortby='date'):

        self.search_term = search_term
        self.location = location
        self.num_postings = num_postings
        self.sortby = sortby
        self.job_postings = []

    # Scrape all of the job postings for the specified search term.
    def scrape(self):

        search_params = {'q': self.search_term, 'l': self.location, 'sort': self.sortby, 'start': 0}
        desc_params = {'q': self.search_term, 'l': self.location, 'sort': self.sortby, 'vjk': None}

        # Create a new Selenium Chrom webdriver and identify ourselves.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--user-agent="Python"')
        chrome_options.add_argument('log-level=2')
        driver = webdriver.Chrome(chrome_options=chrome_options)

        posting_count = 0

        driver.get('https://ca.indeed.com/jobs?' + urlencode(search_params))

        full_job_count = int(driver.find_element_by_id('searchCountPages').text.split(' ')[3].replace(',', ''))

        # Each serach result page contains 10 postings, so loop accordingly.
        for job_count in range(0, full_job_count, 10):

            # Add the posting cound to the search page parameters to browse through pages.
            search_params['start'] = posting_count

            driver.get('https://ca.indeed.com/jobs?' + urlencode(search_params))

            # Store page source in a BeautifulSoup object to avoid stale references when loading other pages.
            searchresult_soup = BeautifulSoup(driver.page_source, 'html.parser')

            time.sleep(10)

            # For each job posting in the search results page.
            for job_card in searchresult_soup.find_all(class_='jobsearch-SerpJobCard'):

                max_jobs = full_job_count if self.num_postings > full_job_count else self.num_postings
                print('{}/{} jobs'.format(posting_count, max_jobs), end='\r', flush=True)

                if posting_count == max_jobs:

                    return self.job_postings

                else:
                    
                    posting_count += 1

                # Scrape the parameters required for each job posting.

                job_id = job_card.get('data-jk')
                title = job_card.find(class_='jobtitle').text.replace('/', ' ')
                company = job_card.find(class_='company').text.strip()
                location = job_card.find(class_='location').text.strip()

                # Append the newly found job posting id to the parameters for the job description page.
                desc_params['vjk'] = job_id

                # Get the full job description page.
                driver.get('https://ca.indeed.com/jobs?' + urlencode(desc_params))

                description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'jobDescriptionText'))).text

                job_posting = JobPosting(job_id, title, company, location, description)

                time.sleep(10)

                self.job_postings.append(job_posting)

        return self.job_postings

    # Dump all of the job postings into text files.
    def dump(self):

        # Create directory if it doesn't already exist.
        os.makedirs(os.path.dirname('indeedscraper/jobs/'), exist_ok=True)

        for job in self.job_postings:

            with open('indeedscraper/jobs/{} ({}).txt'.format(job.title, job.id), 'w') as job_file:

                job_file.write('ID: {}\n'.format(job.id))
                job_file.write('TITLE: {}\n'.format(job.title))
                job_file.write('COMPANY: {}\n'.format(job.company))
                job_file.write('LOCATION: {}\n'.format(job.location))
                job_file.write('DESCRIPTION: {}\n'.format(job.description))