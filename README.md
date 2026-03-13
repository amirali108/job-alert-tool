Job Alert Tool

This project is a small automation tool written in Python that monitors job listings in Sweden and sends notifications when new matching jobs appear.

The goal of this project is to simplify the job search process by automatically checking job listings and notifying the user when relevant opportunities are published.

Instead of manually visiting job websites multiple times a day, this tool checks for new listings periodically and sends a Telegram alert when a matching job is found.

How It Works

The program queries the Swedish JobTech / Arbetsförmedlingen job search API and retrieves the latest job listings.

Each job is filtered using the following conditions:

The job must match one of the configured keywords

The job must be located in Stockholm

The job must be published within the last 24 hours

The job must not have been sent before

When a new job passes these filters, the tool sends a notification to the configured Telegram chat.

To avoid duplicate alerts, the program stores previously processed jobs in a small SQLite database.

Why This Project Was Built

This tool was created for two main reasons:

To automate the process of monitoring job listings.

To practice building a small real-world automation tool using Python.

The project demonstrates how a simple script can integrate APIs, automation, messaging services, and scheduled tasks to solve a practical problem.

Technologies Used

The project uses a lightweight and simple stack:

Python

Requests (API communication)

SQLite (local storage)

Telegram Bot API (notifications)

Cron (automation / scheduling)

Docker (optional containerization)

Use Case

This tool is useful for people who want to:

monitor specific job roles

receive alerts immediately when new jobs are published

avoid manually checking job websites multiple times per day

Although the tool was originally created for personal use, it can easily be adapted to monitor other roles, locations, or job sources.

Possible Future Improvements

Some potential improvements for the project include:

adding more job sources (for example LinkedIn or other job boards)

supporting multiple cities

adding remote job filtering

building a small web dashboard to view collected jobs

deploying the tool on a server for continuous monitoring

Author

Amirali Fatehi
GitHub: https://github.com/amirali108
