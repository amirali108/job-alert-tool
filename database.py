import sqlite3

DB_NAME = "jobs.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT
        )
    """)

    conn.commit()
    conn.close()


def job_exists(job_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM jobs WHERE id = ?", (job_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


def save_job(job):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jobs (id, title, company, location, link)
        VALUES (?, ?, ?, ?, ?)
    """, (
        job["id"],
        job["title"],
        job["company"],
        job["location"],
        job["link"]
    ))

    conn.commit()
    conn.close()
