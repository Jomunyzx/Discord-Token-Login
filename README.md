# Discord Token Login Script

A Python script to login to a Discord account using a token, with support for multiple browsers (Chrome, Firefox, Edge, Safari) and cross-platform compatibility (Windows, macOS, Linux).

## Features
- **Login to Discord** using a token across different browsers and operating systems
- **Fetch token information** (username, email, etc.)
- Simple command-line interface for easy navigation
- Supports multiple operating systems:
  - Windows (Chrome, Edge)
  - macOS (Safari)
  - Linux (Firefox)

## Prerequisites

Before running this script, ensure that the following are installed:

- **Python 3.x**
- **Google Chrome**, **Firefox**, **Edge**, or **Safari**
- **ChromeDriver**, **GeckoDriver**, or **EdgeDriver**, depending on your browser and OS

### Browser-Specific Drivers:
- **ChromeDriver**: [Download here](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json)
- **GeckoDriver (Firefox)**: [Download here](https://github.com/mozilla/geckodriver/releases)
- **EdgeDriver**: [Download here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### Python Libraries:
- `requests`
- `selenium`
- `colorama`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/discord-token-login.git
   cd discord-token-login
