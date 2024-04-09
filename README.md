# CIS 6930, Spring 2024 Assignment 2 - Data Augmentation

## Author
Name: Sai Krishna Anugu 
UFID: 42266064


## Introduction
Assignment 2 focuses on data augmentation on police incident records extracted in Assignment 0. The objective is to  extracting incident data from those PDFs, and augmenting that data with additional information such as the day of the week, time of day, weather conditions, location ranks, and incident nature ranks, considering fairness and bias. This augmented data supports deeper analysis and serves as a prepared dataset for subsequent processes in a data pipeline.


## Running Instructions
To execute the data augmentation script (`assignment2.py`), follow the steps below. Ensure Python 3 and required libraries (`requests`, `pypdf`, `geopy`, etc.) are installed.


1. **Setup Environment:**  
  
   pip install pipenv
   

2. **Install Dependencies:**  
  
   pipenv install
   

3. **Activate Virtual Environment:**  
   
   pipenv shell
   
   Alternatively, use `pipenv run` before commands to run them directly within the virtual environment.

4. **Execute the Script:**  
   
   pipenv run python assignment2.py --urls <Path to CSV file with URLs>
   ```
   Replace `<Path to CSV file with URLs>` with the actual file path. This CSV file should contain URLs to the PDFs of incident reports.


## Detailed Function Descriptions

 **`download_pdf(url)`:** This function takes a URL as input and performs a web request to download the content located at that URL, assumed to be a PDF document. The function creates a directory (if it doesn't already exist) to store the downloaded PDF and saves the file with a predefined name in the specified path. This setup is useful for automating the retrieval and local storage of PDF documents from online sources.

 **`extract_incidents(pdf_path)`:** After downloading the PDF, this function opens and reads the document, extracting text from each page. It processes the text to identify and organize data related to incidents reported within the document. The function employs text analysis to determine the start indices of columns and ensures data is correctly segmented, addressing challenges posed by varying formats and layouts in PDF documents.

 **`calculate_location_ranks(incidents)`:** Utilizing the data extracted from the PDF, this function focuses on the locations associated with each incident. It counts how frequently each location appears in the dataset and assigns ranks based on this frequency. Locations that appear more often are given higher priority. This ranking system can help in identifying areas with higher incidences of events, valuable for analysis and resource allocation.

 **`get_day_of_week(date_time_str)`, `get_time_of_day(date_time_str)`:** These functions parse the datetime strings from the incident data, converting them into more useful formats. get_day_of_week calculates which day of the week the incident occurred, and get_time_of_day extracts the hour of the day. This temporal data is crucial for analyzing trends and patterns in incident occurrences over time.

 **`weather_code(api_key, date_time_str)`:** By interfacing with the OpenWeatherMap API, this function retrieves historical weather conditions for the time and location of each incident. It maps the weather data to a simplified code system for easy analysis, providing insights into how weather conditions may influence incident rates.

 **`get_lat_lon_from_location(location_name)`:** This geocoding function converts location names into geographical coordinates (latitude and longitude). It uses the Nominatim service to resolve location names to coordinates, essential for geographical analyses and mapping incidents to specific locations.

 **`calculate_bearing(...)`, `determine_side_of_town(bearing)`:** These functions calculate the directional bearing from a central point to the incident location and categorize the incident's location in terms of the cardinal and intercardinal directions (e.g., N, NE, E). This is useful for spatially analyzing where incidents occur relative to a central point of interest

 **`calculate_incident_ranks(incidents)`:** Similar to calculate_location_ranks, but focuses on the nature or type of incidents. It ranks each incident type based on occurrence frequency, aiding in identifying the most common types of incidents.

 **`check_emsstat(incident, incidents, current_index)`:** Examines whether an incident record or subsequent records (for a similar time and location) indicate an EMS status, providing insights into the response or severity associated with incidents.

 **`augment_data(...)`:**  Integrates all the previously defined functions to enrich the incident data with additional attributes like day of the week, weather conditions, location and incident ranks, and more. This augmented dataset is more comprehensive and can support deeper analysis.

 **`get_urls_from_csv(file_path)`:**  Extracts URLs from a given CSV file. This utility function is designed to feed the download_pdf function with sources for PDF documents


## Testing
 **`test_get_time_of_day()`:** The function test_get_time_of_day_additional() is designed to verify the accuracy of the get_time_of_day function, which extracts the hour from a given datetime string. It includes three specific test cases: early morning before sunrise, noon, and early evening, to ensure the function correctly identifies various times of the day. Each test case asserts that the function returns the expected hour, based on 24-hour format input, demonstrating the function's reliability across different times. The message printed confirms the successful passing of all additional test scenarios.
 **`test_get_day_of_week()`:**  The test_get_day_of_week_additional() function is designed to validate the accuracy of the get_day_of_week function by using specific dates with known weekdays. It tests the function's ability to correctly identify the day of the week from a given date string, ensuring the function's reliability across various days. This includes verifying that the function accurately maps dates to their corresponding day of the week, with Sunday as 1 and Saturday as 7, through assertions that compare expected outcomes with actual function outputs.


## Bugs & Assumptions
- **Bugs:** 1. The accuracy of text extraction from PDFs can vary based on the document's formatting. Complex layouts might not be accurately parsed, leading to potential data loss or misinterpretation.
2.Historical weather data retrieval is based on timestamps which may not perfectly align with the incident times, possibly affecting the accuracy of weather conditions associated with incidents.

- **Assumptions:** The geocoding function assumes that location names are unique and can be resolved to a single set of coordinates. In reality, duplicate names or insufficient detail can lead to incorrect geolocations.




