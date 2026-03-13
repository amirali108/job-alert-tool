from dotenv import load_dotenv
load_dotenv()

import requests
from datetime import datetime, timedelta, timezone
from config import JOB_API_URL, KEYWORDS, CITY


def parse_datetime(value):
    if not value:
        return None

    try:
        if value.endswith("Z"):
            value = value.replace("Z", "+00:00")
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def is_within_last_24_hours(job):
    published_at = parse_datetime(job.get("publication_date"))

    if not published_at:
        published_at = parse_datetime(job.get("publication_datetime"))

    if not published_at:
        published_at = parse_datetime(job.get("published"))

    if not published_at:
        return False

    now = datetime.now(timezone.utc)
    return published_at >= now - timedelta(hours=24)


def get_jobs():
    jobs_dict = {}

    for keyword in KEYWORDS:
        params = {
            "q": keyword,
            "limit": 20
        }

        response = requests.get(JOB_API_URL, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        hits = data.get("hits", [])

        for job in hits:
            municipality = job.get("workplace_address", {}).get("municipality")

            if not municipality:
                continue

            if CITY.lower() not in municipality.lower():
                continue

            if not is_within_last_24_hours(job):
                continue

            job_id = job.get("id")
            if not job_id:
                continue

            if job_id not in jobs_dict:
                jobs_dict[job_id] = {
                    "id": job_id,
                    "keywords": [keyword],
                    "title": job.get("headline", "No title"),
                    "company": job.get("employer", {}).get("name", "Unknown"),
                    "location": municipality,
                    "link": job.get("webpage_url", "")
                }
            else:
                if keyword not in jobs_dict[job_id]["keywords"]:
                    jobs_dict[job_id]["keywords"].append(keyword)

    return list(jobs_dict.values())


if __name__ == "__main__":
    jobs = get_jobs()
    print(f"Found {len(jobs)} jobs from the last 24 hours\n")

    for job in jobs[:10]:
        print(job)
