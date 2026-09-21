# WhatsApp Horizontal Spam Script

A robust, lightweight Python automation script for sending dynamic, scheduled WhatsApp messages to a target list of phone numbers using WhatsApp Web automation.

## Overview

This utility automates outreach workflows by leveraging browser control tools to sequentially send messages via WhatsApp Web. It natively includes anti-spam protections—such as rotation pools for text bodies and dynamically generated delay padding—to help prevent automated distribution flags or account restrictions.

## Features

- **Automated Instant Messaging:** Leverages browser control pipelines to execute immediate, hands-free message routing (`pywhatkit.sendwhatmsg_instantly`).
- **Dynamic Message Rotation:** Cycles through an array of message texts continuously, ensuring adjacent recipients receive unique text patterns to reduce spam indicators.
- **Global Asset Appending:** Standardized tracking links, operational assets, or landing links can be universally attached to all dynamic messages.
- **Anti-Spam Delay Engine:** Utilizes a random intervals matrix (e.g., 70–100 seconds) between successive transfers to mirror organic human typing behaviors.
- **Automatic Session Cleanup:** Closes active messaging tabs automatically (`tab_close=True`) to maintain minimal system resource usage during mass tasks.
- **Integrated Error Resilience:** Wraps transmissions inside an independent try-catch architecture so single-number connection failures do not disrupt the remaining deployment queue.

## Project Structure

```bash
whatsapp-horizontal-spam-script/
├── main.py              # Core execution automation script
├── requirements.txt     # Python environment package list
└── README.md            # Usage and architectural documentation
```

## Setup & Execution

### Prerequisites

- Python 3.7 or higher installed on your local host.
- An active browser logged into **WhatsApp Web** on your default machine account before execution.

### Installation

- Clone or download the automation workspace locally:

  ```bash
  git clone https://github.com
  ```

- Navigate into the root path and install dependencies using pip:
  ```bash
  pip install -r requirements.txt
  ```

### Usage Configuration

1. Open `main.py` in your preferred editor.
2. Edit the `phone_numbers` array using complete international formats (e.g., `+964xxxxxxxxxx`).
3. Customize the text variants inside the `messages` list and optionally include a link or invitation text in `message_asset`.
4. Launch the automation framework from your console interface:
   ```bash
   python main.py
   ```

## Author

H2SO4-1191 – Software Engineer
