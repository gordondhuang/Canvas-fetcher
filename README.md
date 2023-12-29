# Canvas-Scraper
This project was created to aid students in organizing their course information to optimize productivity.

## Instructions
To function correctly **canvas-key.txt** must be modified.
1. Use the python environment command in the terminal **py -m venv env** with the project open
2. The first line entered into the .txt file should be your Canvas API token key(refer to token generation)
3. The second line should be your Canvas User_Id(refer to user_id)
4. The third line should be your university's url(ex. canvas.uw.edu)

## Canvas API Token key generation
1. Log into your Canvas account
2. Select the Account >> Settings
3. Under Approved Integrations create a New Access Token (refer to your university's policies)

## Retrieving User_id
1. Go to https://**canvas**/api/v1/users/self (**replace canvas**)
2. The id is within the json object

## Documentation
- [CanvasLMS - REST API and Extensions](https://canvas.instructure.com/doc/api/index.html)
- [UW Canvas Policies](https://itconnect.uw.edu/tools-services-support/teaching-learning/canvas/canvas-policies/)
