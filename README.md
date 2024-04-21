# Steps for setting up and using venv for backend:

## Terminal Commands to run from within backend folder:
`python -m venv venv`  
`venv\Scripts\activate`  
`pip install -r requirements.txt`  

To exit the venv:
`deactivate`

## Running our app from terminal:
I use two different terminal windows for this: one to run the frontend and one to run the backend.  
1. Make sure all requirements are installed (`npm i` for frontend requirements and instructions above for backend)  
2. From the folder `backend`, enter `flask run` to launch the backend  
3. From the root folder, enter `npm run dev` to launch the frontend  