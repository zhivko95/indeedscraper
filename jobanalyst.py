import sys
import os
from collections import Counter

class JobAnalyst:

    def __init__(self, jobpostings, dump=False):

        self.jobpostings = jobpostings
        self.dump = dump

        with open('skills.csv') as skills_file:
            self.all_skills = skills_file.read().splitlines()

    # Go through all given job postings and find the most frequently mentioned skills.
    def top_skills(self):

        self.skill_counts = Counter()

        for posting in self.jobpostings:

            self.skill_counts += Counter({skill for skill in self.all_skills if skill in posting.description})

        if self.dump:

            os.makedirs(os.path.dirname('indeedscraper/skills/top_skills.txt'), exist_ok=True)
            with open('indeedscraper/skills/top_skills.txt', 'w+') as d_file:
                
                d_file.writelines('{}\n'.format(skill) for skill in self.skill_counts.most_common())

        else:

            return self.skill_counts.most_common()

    # Create a simple graph to visually represent the most frequently mentioned skills.
    def graph_top_skills(self):

        self.top_skills()

        if self.dump:

            orig_stdout = sys.stdout
            os.makedirs(os.path.dirname('indeedscraper/skills/skills_graph.txt'), exist_ok=True)
            d_file = open('indeedscraper/skills/skills_graph.txt', 'w+')
            sys.stdout = d_file

        print('-----------------------------------------')
        print('||| TOP SKILLS GRAPH BASED ON {} JOBS |||'.format(len(self.jobpostings)))
        print('-----------------------------------------')
        
        for skill_name, frequency in self.skill_counts.most_common():

            print('{:>12} |'.format(skill_name) + '+' * int(frequency/sum(self.skill_counts.values()) * 20))

        if self.dump:

            sys.stdout = orig_stdout
            d_file.close()

