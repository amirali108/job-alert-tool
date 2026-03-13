# Job Alert Tool

Job Alert Tool is a small Python automation project that monitors job listings in Sweden and sends Telegram notifications when new jobs appear.

The tool searches for jobs in Stockholm using predefined keywords and automatically sends a Telegram message when a matching job is published.

## How It Works

The program connects to the Swedish JobTech / Arbetsförmedlingen job search API.

Each job is filtered using these rules:
- The job must match one of the keywords
- The job must be located in Stockholm
- The job must be published within the last 24 hours
- The job must not already exist in the database

If a job passes all checks, a Telegram message is sent.

Processed jobs are stored in a small SQLite database to prevent duplicate notifications.

## Features
- Automatic job monitoring
- Keyword filtering
- Stockholm location filtering
- 24-hour job filtering
- Telegram notifications
- SQLite database for duplicate protection
- Cron automation support
- Docker support

## Technologies Used
- Python
- Requests
- SQLite
- Telegram Bot API
- Cron
- Docker

## Author
Amirali Fatehi
GitHub: https://github.com/amirali108
