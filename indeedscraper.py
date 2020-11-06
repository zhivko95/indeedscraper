import argparse
from jobscraper import JobScraper
from jobanalyst import JobAnalyst

# COMMAND LINE ARGUMENTS
argparser = argparse.ArgumentParser(description='Data scraper used to find the top skills for a search term on Indeed.')
argparser.add_argument('-s', '--search', action='store', dest='search_term', required=True, nargs='*', help='The search term to be used on Indeed.')
argparser.add_argument('-l', '--location', action='store', dest='location', default='Toronto, ON', nargs='*', help='The location to be used for the Indeed search.')
argparser.add_argument('-n', '--num', action='store', dest='num_postings', default=100, type=int, help='Specifies how many job postings to use for the analysis.')
argparser.add_argument('-d', '--dump', action='store', dest='dump_flag', type=bool, default=False, help='Boolean flag used to dump output to text files.')
cmd_args = argparser.parse_args()

js = JobScraper(' '.join(cmd_args.search_term), ''.join(cmd_args.location), num_postings=cmd_args.num_postings,)

analyst = JobAnalyst(js.scrape(), dump=cmd_args.dump_flag)

if cmd_args.dump_flag:

    js.dump()

analyst.graph_top_skills()
