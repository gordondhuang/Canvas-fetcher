# Canvas-Scraper
This project was created to aid students in organizing their course information to optimize productivity.

## Variables
To function correctly the **canvas-token.txt** must be modified.
The first line entered into the .txt file should be your Canvas API token key(refer to token generation)
The second line should be your Canvas User_Id(refer to user_id)

## Canvas API Token key generation
1. Log into your Canvas account
2. Select the Account >> Settings
3. Under Approved Integrations create a New Access Token

## Retrieving User_id
1. Go to https://canvas/api/v1/users/self(replace canvas)
2. The id is within the json object

## Documentation
- [CanvasLMS - REST API and Extensions](https://canvas.instructure.com/doc/api/index.html)
- [UW Canvas Policies](https://itconnect.uw.edu/tools-services-support/teaching-learning/canvas/canvas-policies/)