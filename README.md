
# CIS 6930, Spring 2024 Assignment 2 - Data Augmentation

## Author
Name: [Srinivas Pavan Singh Runval]  
UFID: [93324706]

## Introduction
Assignment 2 focuses on data augmentation on police incident records extracted in Assignment 0. The objective is to enrich the dataset with additional information like the day of the week, time of day, weather conditions, etc., considering fairness and bias. This augmented data supports deeper analysis and serves as a prepared dataset for subsequent processes in a data pipeline.

## Running Instructions
To execute the data augmentation script (`assignment2.py`), follow the steps below. Ensure Python 3 and required libraries (`requests`, `pypdf`, `geopy`, etc.) are installed.

1. **Setup Environment:**  
   Ensure Python 3.6 or newer is installed along with `pipenv` for handling virtual environments and dependencies.
   ```bash
   pip install pipenv
   ```

2. **Install Dependencies:**  
   Navigate to the project directory and install dependencies using:
   ```bash
   pipenv install
   ```

3. **Activate Virtual Environment:**  
   Activate the virtual environment with:
   ```bash
   pipenv shell
   ```
   Alternatively, use `pipenv run` before commands to run them directly within the virtual environment.

4. **Execute the Script:**  
   Use the following command to run `assignment2.py`:
   ```bash
   pipenv run python assignment2.py --urls <Path to CSV file with URLs>
   ```
   Replace `<Path to CSV file with URLs>` with the actual file path. This CSV file should contain URLs to the PDFs of incident reports.

## Detailed Function Descriptions

- **`download_pdf(url)`:** Downloads a PDF file from a given URL and saves it to the `./docs` directory.

- **`extract_incidents(pdf_path)`:** Extracts incident records from a downloaded PDF file. Each record includes date/time, incident number, location, nature, and incident ORI.

- **`calculate_location_ranks(incidents)`:** Calculates and assigns ranks to incident locations based on their frequency of occurrence.

- **`get_day_of_week(date_time_str)`, `get_time_of_day(date_time_str)`:** Extract the day of the week and the hour of the day from the incident date/time string, respectively.

- **`weather_code(api_key, date_time_str)`:** Retrieves weather conditions for the incident's date/time and location using the OpenWeatherMap API, mapping the conditions to WMO codes.

- **`get_lat_lon_from_location(location_name)`, `calculate_bearing(...)`, `determine_side_of_town(bearing)`:** Determine the approximate side of town (N, S, E, W, etc.) for an incident location using geocoding and bearing calculations.

- **`calculate_incident_ranks(incidents)`:** Assigns ranks to incidents based on the frequency of their nature.

- **`check_emsstat(incident, incidents, current_index)`:** Checks whether an incident involves an EMS status, either directly or in closely subsequent records.

- **`augment_data(...)`:** Augments each incident record with additional derived information (day of the week, weather conditions, etc.) and prints the augmented data to stdout.

- **`get_urls_from_csv(file_path)`:** Parses a CSV file to extract URLs of incident PDFs.

## Testing
- **`test_get_time_of_day()`:** Validates the correctness of extracting the time of day from a date/time string.
- **`test_get_day_of_week()`:** Ensures the day of the week is accurately determined from a date/time string.

These test functions are located in the `tests/` directory and can be executed to verify the correctness of the respective functionalities.

## Bugs & Assumptions
- **Bugs:** Please detail any known issues or bugs in the script here, including limitations of the data extraction and augmentation processes.

- **Assumptions:** This section should outline any assumptions made during the development, such as the format of the incident PDFs, reliability of external APIs for weather data, or assumptions regarding the data's completeness and accuracy.

## Resources
- Model Cards and Data Sheets: [Link to resource]
- Historical Weather API: [Link to OpenWeatherMap API documentation]
- Geocoding API: [Link to Geopy documentation]

## License
This project is licensed under the MIT License - see the LICENSE file for details.
