from dotenv import load_dotenv
load_dotenv()

from job_scraper import get_jobs
from notifier import send_message
from database import init_db, job_exists, save_job


def format_job_message(job):
    keywords = ", ".join(job["keywords"])

    message = (
        "🚀 New Job Alert\n\n"
        f"Keywords: {keywords}\n"
        f"Title: {job['title']}\n"
        f"Company: {job['company']}\n"
        f"Location: {job['location']}\n"
        f"Link: {job['link']}"
    )

    return message


def main():
    init_db()

    jobs = get_jobs()

    new_jobs = 0

    for job in jobs:

        if not job_exists(job["id"]):

            save_job(job)

            message = format_job_message(job)

            send_message(message)

            new_jobs += 1

    print(f"Checked {len(jobs)} jobs")
    print(f"New jobs sent: {new_jobs}")


if __name__ == "__main__":
    main()
