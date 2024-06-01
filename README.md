
# Collatz Conjecture Calculator

This is a Flask web application that calculates and visualizes the Collatz sequence for a given integer. The application allows users to input a number, compute the Collatz sequence, and display the path of the sequence along with the maximum value and the number of steps.

## Features

- Input a number to compute its Collatz sequence.
- Visualize the Collatz sequence path using a plot.
- Display the maximum value in the sequence.
- Display the number of steps to reach 1.

## Requirements

- Python 3.x
- Flask
- Matplotlib

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nskath/collatz.git
   ```
2. Navigate to the project directory:
   ```sh
   cd collatz
   ```
3. Install the required dependencies:
   ```sh
   pip install matplotlib
   pip install -U Flask
   ```

## Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter a number in the input field and click "Calculate" to see the results.

## Code Overview

- `collatz_sequence(n)`: Computes the Collatz sequence for a given integer `n`.
- `index()`: Handles the main route of the application. It processes user input, computes the sequence, generates the plot, and renders the template.

## Template

The application uses an inline HTML template to render the form, results, and any error messages.

