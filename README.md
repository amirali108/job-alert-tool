# Job Alert Tool

This project is a small Python automation tool that monitors job listings in Sweden and sends Telegram notifications when new matching jobs are published.

The tool automatically searches for jobs in Stockholm using predefined keywords and notifies the user when new opportunities appear.

The goal of this project is to simplify the job search process by automating the monitoring of job listings and providing instant alerts.

## How It Works

The program connects to the Swedish JobTech / Arbetsförmedlingen job search API and retrieves job listings.

Each job is filtered using the following conditions:

- The job must match one of the configured keywords.
- The job must be located in Stockholm.
- The job must have been published within the last 24 hours.
- The job must not have been previously processed.

If a job meets all conditions, the tool sends a notification to Telegram.

To prevent duplicate alerts, previously processed jobs are stored in a small SQLite database.

## Features

- Automatic job search
- Keyword-based filtering
- Location filtering (Stockholm)
- 24-hour job filtering
- Telegram notifications
- Duplicate protection using SQLite
- Scheduled execution with cron
- Docker support

## Technologies Used

The project uses a simple and lightweight technology stack:

- Python
- Requests
- SQLite
- Telegram Bot API
- Cron
- Docker

## Use Case

This tool helps users monitor job listings automatically without needing to manually check job websites multiple times per day.

When a new job that matches the defined criteria appears, the user receives a Telegram notification immediately.

Although this tool was originally created for personal job monitoring, it can easily be adapted for different roles, keywords, or locations.

## Future Improvements

Possible improvements for the project include:

- adding more job sources
- supporting multiple cities
- filtering remote jobs
- creating a small web dashboard
- deploying the tool on a server for continuous monitoring

## Author

Amirali Fatehi  
GitHub: https://github.com/amirali108
