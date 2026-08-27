*Project Title and Description 

This is a simple voting application where people can vote for different candidates using a web browser.
Each vote is recorded and the current vote totals can be viewed at any time.
The application also allows all votes to be cleared when needed.
It runs locally on your computer and provides simple web pages for voting and viewing results.

*Installation and Setup
1. Download the project

  Clone the GitHub repository:

  git clone https://github.com/gauravdevkar/Task.git

  Move into the project directory:

  cd YOUR_REPOSITORY

2. Install Flask

  Make sure Python is installed, then install Flask:
  
  pip install flask
  
3. Run the application

Start the Flask application:

python -m flask --app Task1 run --debug

The application will run on:

http://localhost:5000

4. Use the application

Open a browser and visit the endpoints listed below.

For example:

http://localhost:5000/vote/Alice

Then check the results:

http://localhost:5000/results


*API Endpoint Reference

<img width="257" height="621" alt="image" src="https://github.com/user-attachments/assets/87b7c669-b457-453e-8ba1-d3c5ad1c0f40" />


*Git Workflow

All new development was completed on the dev branch.

The project started with Version 1 on the dev branch. Version 1 was then merged into main.

For Version 2, the /reset feature was developed on dev, committed, and pushed to GitHub. The dev branch was then merged into main and the updated main branch was pushed to GitHub.

The workflow was:

Version 1
   |
   v
dev branch
   |
   | merge
   v
main branch
   |
   v
Version 1 released
   |
   v
dev branch
   |
   | Add /reset
   | Commit Version 2
   v
main branch
   |
   v
Version 2 released


*Version History

Version	Features

Version 1	Added the Flask application, /, /health endpoints.

Version 2	Added the /reset endpoint to clear all stored vote counts.

*Screenshots

Application Running in Browser

<img width="361" height="223" alt="image" src="https://github.com/user-attachments/assets/0977a3e3-812c-4e21-9c6a-38ef46027996" />


*GitHub Branches

The screenshot below shows the GitHub repository with both the dev and main branches.

<img width="577" height="436" alt="image" src="https://github.com/user-attachments/assets/7a6ba764-3415-4c2c-af1f-698776c670ac" />

*Version History 

The screenshot below shows the commit history for Version 1 and Version 2.

<img width="345" height="90" alt="image" src="https://github.com/user-attachments/assets/adbd0004-37ff-4065-8de1-55a04f19e55e" />
<img width="538" height="80" alt="image" src="https://github.com/user-attachments/assets/2ffe2dd6-0c70-4906-8e3f-047aef39998b" />


