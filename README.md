# indeedscraper
With this tool, you can easily gather information about the most wanted skills relating to every Indeed job search query.  

# Getting Started

First, make sure to have Python installed as well as all of the third party python libraries listed in the requirements file.

It is reccommended to source your own skills list as the one which comes included in the source is not exhaustive and lacks some important skills (original list can be found at https://www.onetonline.org/search/hot_tech/). It is mainly provided just as an example for testing. If you use your own skills list, ensure it follows the same format and naming convention as the example.

Next, simply run the script from the command line and provide a search query command line argument (-s). For a list of all available arguments to customize the user experience refer to the arguments section of the readme.

# Arguments

- ## Search Term (required)

  `(-s / --search) [search term]` => Used to specify the search term which yields all of the job postings. Search terms can be multiple words.
  
  **_USAGE:_** `-s office admin` **OR** `--search office admin`

- ## Location (optional)

  `(-l / --location) [location]` => Can be used to specify the location for the search query. This argument is optional and can contain spaces.
  
  **_USAGE:_** `-l Toronto ON` **OR** `--location Toronto ON`

- ## Number of Job Postings (optional)

  `(-n / --num) [num_postings]` => Specifies the number of job postings to scrape. This argument is optional and defaults to 1000. However, most search queries will have less postings and essentially all of them will be used.
  
  **_USAGE:_** `-n 50` **OR** `--num 50`

- ## Output Dump (optional)

  `(-d / --dump) [True/False]` => Boolean flag to specify whether an output dump is required. This arguement is optional and defaults to False. Output file directory structure can be seen below.
  
  **_USAGE:_** `-d True` **OR** `--dump True`
  
  ```
  .
  +-- indeedscraper
  |     +-- jobs
  |           +-- job1.txt
  |           +-- job2.txt
  |           +-- ...
  |     +-- skills
  |           +-- top_skills.txt
  |           +-- skills_graph.txt
  +-- jobposting.py
  +-- jobscraper.py
  +-- jobanalyst.py
  +-- indeedscraper.py
  +-- skills.csv
  ```
