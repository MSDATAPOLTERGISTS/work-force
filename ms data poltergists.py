
class Job:
    def __init__(self, title, company, location, description):
        self.title = title
        self.company = company
        self.location = location
        self.description = description

class EmploymentApp:
    def __init__(self):
        self.job_listings = []

    def add_job_listing(self, title, company, location, description):
        job = Job(title, company, location, description)
        self.job_listings.append(job)

    def display_job_listings(self):
        print("Job Listings:")
        for idx, job in enumerate(self.job_listings, start=1):
            print(f"{idx}. Title: {job.title}\n   Company: {job.company}\n   Location: {job.location}\n   Description: {job.description}\n")

    def apply_for_job(self, job_index):
        if 0 < job_index <= len(self.job_listings):
            job = self.job_listings[job_index - 1]
            print(f"Applied for job: {job.title} at {job.company}")
        else:
            print("Invalid job index")

# Creating an instance of the EmploymentApp
app = EmploymentApp()

# Adding some sample job listings
app.add_job_listing("Software Engineer", "ABC Inc.", "New York", "We are looking for a skilled software engineer to join our team.")
app.add_job_listing("Data Analyst", "XYZ Corp.", "San Francisco", "We are seeking a data analyst to analyze and interpret data.")
app.add_job_listing("Product Manager", "123 Co.", "Seattle", "We are hiring a product manager to oversee product development.")

# Displaying all job listings
app.display_job_listings()

# Applying for a job (index 1 in this case)
app.apply_for_job(1)