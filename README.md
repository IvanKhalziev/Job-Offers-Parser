# Job-Offers-Parser
A Python script to parse job offers for the position of "Fachinformatiker Anwendungsentwicklung" from a website **"https://www.azubiyo.de/"** and save the data into an Excel file.

## Prerequisites
Before running the script, make sure you have the following libraries installed:

* **requests**
* **pandas**
* **beautifulsoup4**
You can install these dependencies using pip:

```bash
pip install requests pandas beautifulsoup4
```

## Usage
1. Open the script **file job_offers_parser.py** in a text editor or an integrated development environment (IDE).
2. Set the desired parameters at the beginning of the script:
  * **PATH**: Path to the Excel file where the job offers will be saved.
  * **HOST**: The base URL of the website.
  * **URL**: The specific URL of the job offers page.
  * **HEADERS**: HTTP headers used in the requests.
3. Run the script using the following command:
```bash
python job_offers_parser.py
```
4. When prompted, enter the number of pages you want to parse.
5. The script will start parsing each page, retrieve the job offers information, and save it into the specified Excel file.
Please note that the script assumes a specific structure of the target website's HTML. Any changes to the website's structure may require modifications to the script.

##Output
The script will generate an Excel file (**Job_offers.xlsx**) containing the following information for each job offer:

* Name of job: The title of the job offer.
* Company: The name of the company offering the job.
* Location: The location of the job.
* Date of start: The start date of the job.
You can customize the output by modifying the **get_content** function according to your needs.

##Disclaimer
This script is for educational purposes only. Use it responsibly and respect the website's terms of service.
