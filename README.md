# OneNoteSyncScheduler

OneNoteSyncScheduler is a Python-based tool designed to facilitate the synchronization and backup of your notes and schedules, particularly with Google services. This tool uses various scripts to automate the synchronization process and make it more seamless.

## Features

- **Google Services Integration**: The `Google.py` script allows for easy integration with Google APIs for authentication and access to services like Google Sheets.

- **OAuth Handling**: The `OAuth.py` script handles OAuth authentication with the Google Calendar API and retrieves events from the user's primary calendar.

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository.

2. Install required dependencies:


3. Configure your `credentials.json` file for Google API access.

4. Run the main script:


## Usage

The `main.py` script launches OneNote and creates a schedule for the year 2023.

## Code Files

### `Google.py`

This script provides a helper function for creating Google API services and managing authentication tokens. It facilitates integration with Google services like Google Sheets.

### `OAuth.py`

This script uses the functions from `Google.py` to handle OAuth authentication and retrieve events from the user's primary Google Calendar.

### `main.py`

This script uses the `subprocess` and `typer` modules to open OneNote and create a schedule for the year 2023.

### `typer.py`

A module for handling command-line interfaces with the `typer` library.

## Contributing

Contributions are welcome! Please create an issue or pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
