# Wolf HTTP Client

## Description
The Wolf HTTP Client is a graphical user interface (GUI) application built using Tkinter for interacting with a backend API for the game "Loup-Garou" (Werewolf). The application allows users to view available game parties, subscribe to a party, and start solo games.

## Project Structure
```
wolf-http-client
├── src
│   ├── main.py                # Main entry point of the application
│   ├── gui
│   │   ├── __init__.py        # GUI package initializer
│   │   └── interface.py       # GUI logic and layout
│   ├── services
│   │   ├── __init__.py        # Services package initializer
│   │   └── api_service.py     # API interaction functions
│   └── utils
│       ├── __init__.py        # Utils package initializer
│       ├── constants.py       # Constants used in the application
│       └── helpers.py         # Utility functions for various tasks
├── README.md                  # Project documentation
└── requirements.txt           # Project dependencies
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd wolf-http-client
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. The GUI will open, allowing you to interact with the game API.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.