# english_extra

A Streamlit-based interactive quiz application for testing reading comprehension and understanding of text.

## Description

This application provides a series of exercises to test understanding of a story involving characters like Bridget, John, Hector, and Annie. The quiz includes various question types to engage users and assess their comprehension.

## Features

- **Multiple Question Types:**
  - Fill in the Blanks
  - Multiple Choice Questions
  - True or False Questions
  - Matching Exercises

- **Session State Management:**
  - Tracks score across all questions
  - Provides immediate feedback (Good!/Bad!)
  - Shows correct answers when responses are incorrect

- **User-Friendly Interface:**
  - Clean, organized layout with clearly labeled exercises
  - Submit buttons for each exercise
  - Total score display
  - Reset functionality to restart the quiz

## Exercises

The quiz contains 17 exercises covering:
- Character relationships (Bridget, John, Hector, Annie, Charley)
- Plot details (phone calls, flowers, visits)
- Character descriptions and traits
- Story timeline and events

## Requirements

- Python 3.x
- Streamlit

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd english_extra
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run quiz01.py
```

The application will open in your default web browser at `http://localhost:8501`.

## How to Use

1. Read through each exercise carefully
2. Select or type your answer
3. Click the "Submit" button for each exercise to receive immediate feedback
4. Track your progress as you complete each question
5. Click "Show Results" to see your total score
6. Click "Reset Quiz" to start over

## Project Structure

```
english_extra/
├── README.md       # This file
├── quiz01.py       # Main Streamlit application
└── .devcontainer/  # Development container configuration
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.