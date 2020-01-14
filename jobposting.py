class JobPosting:

    def __init__(self, posting_id, title, company, location, description):

        self.id = posting_id
        self.title = title
        self.company = company
        self.location = location
        self.description = description

    def __str__(self):

        return self.title + ' at ' + self.company + ', ' + self.location