

---

# Avocado Shiny App

This repository contains the code and necessary files to deploy a Shiny web application. The application is designed to provide a dashboard of California avocado insights.

## Requirements

To run this application locally or deploy it on a server, you need the following:

- Python 3.x
- Pip (Python package manager)
- Shiny server or a compatible deployment environment

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/RobinMillford/Avocado-Shiny-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Avocado-Shiny-App
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

To run the Shiny app locally:

1. Ensure all dependencies are installed (see Installation above).
   
2. Start the Shiny app using Uvicorn:

   ```bash
   shiny run --reload --launch-browser app.py 
   ```

### Deployment

Here is my Deployed app on Shiny server - [Avocado Dashboard](https://robinmillford.shinyapps.io/avocado-app/)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request in this repository.
