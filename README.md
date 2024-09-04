# Canvas-Scraper
This project was created to aid students in organizing their course information to optimize productivity.

## Usage
To function correctly **canvas-key.txt** must be modified.
1. Use these sequences of commands in the terminal with the folder of the project open as the directory:

   ```bash
   # For mac / Linux: 
   python3 -m venv env

   # For Windows:
   python -m venv env 

   # Activate the virtual environment
   source env/Scripts/activate
   # Other options: env/Scripts/activate or env/Scripts/activate.bat

   # Installs dependencies
   pip install -r requirements.txt
   
   ```
**(Double-check Python interpreter path to make sure it's within the environment)**  
3. The first line entered into the .txt file should be your Canvas API token key(refer to token generation)  
4. The second line should be your Canvas User_Id(refer to user_id)  
5. The third line should be your university's URL (ex. canvas.uw.edu)  

```text
mycanvastoken123456 
123456 
canvas.uw.edu
```

Finally run this command in your terminal:
```bash
python webscraper.py
```
This should produce several csv files that contain course information and assignments.

## Canvas API Token key generation
1. Log into your Canvas account
2. Select the Account >> Settings
3. Under Approved Integrations create a New Access Token (refer to your university's policies)

## Retrieving User_id
1. Go to https://**canvas**/api/v1/users/self (**replace canvas with your university's URL**)
2. The id is within the JSON object

## Documentation
- [CanvasLMS - REST API and Extensions](https://canvas.instructure.com/doc/api/index.html)
- [UW Canvas Policies](https://itconnect.uw.edu/tools-services-support/teaching-learning/canvas/canvas-policies/)
