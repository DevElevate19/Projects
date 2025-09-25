# Nutrition and Fitness Tracker

A Python-based application that helps users track their nutrition intake and calculate BMI using the API Ninjas nutrition API.

## Overview

This project was developed when my class tests were going on so might have more number of problems than my earlier projects.The application allows users to input their physical information and food consumption to get detailed nutritional analysis.

## Features

- BMI calculation based on height and weight
- Nutritional information retrieval for consumed foods
- Support for multiple food items analysis
- Query specific nutritional components (fat, carbohydrates, protein, fiber, sugar)
- Error handling for API requests

## Requirements

- Python 3.x
- numpy
- requests

## Installation

1. Clone this repository
2. Install required dependencies:
   ```
   pip install numpy requests
   ```
3. Run the application:
   ```
   python nutrition_tracker.py
   ```

## Usage

The application will prompt you for the following information:

1. Age
2. Height (in cm)
3. Weight (in kg)
4. Activities performed
5. Duration of activities
6. Food consumed (with portions)
7. Nutritional component to query

The program will then calculate your BMI and provide nutritional information for the specified food items.

## API Integration

This project uses the API Ninjas nutrition API to fetch nutritional data. The free tier provides access to basic nutritional information including fat, carbohydrates, protein, fiber, and sugar content.

## Limitations

- Uses a personal API key (may be removed in future versions)
- Calorie burn calculation feature is commented out due to API limitations
- Free API tier has limited query capabilities

## Development Notes

This project was created during academic test periods, which explains the rapid development approach and some commented-out features. The calorie burn functionality was partially implemented but disabled due to API constraints requiring specific activity naming conventions.

## Future Improvements

- Implement proper API key management
- Add calorie burn calculation with alternative methods
- Enhance error handling and user input validation
- Add data persistence features

## Author

Created by DevElevate19.
