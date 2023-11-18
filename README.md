Setting up the Django backend 

1. Clone the project to your computer 

2. Switch to the most updated branch, pull request if needed 

3. Create and switch to your new branch before you make any change 

4. Open command prompt 

5. Change directory to the virtual environment 

6. Activate the virtual environment 

7. Install the required library in the virtual environment by running pip install requirements.txt using "pip install -r requirements.txt"

8. Change directory to (directory of your repository)/Capstone_project/backend, run python manage.py runserver 

9. Open browser, enter the link “127.0.0.1:8000/admin”, you are expected to see the administrator interface of Django 

 

Setting up the React frontend 

1. Install node 

2. Use node –v in command prompt to check if node correctly installed 

3. Change directory to (directory of your repository)/Capstone_project/frontend 

4. Run command “npm install” 

5. Run command “npm start” 

6. The frontend would pop up automatically on your browser, if not, enter the link” 127.0.0.1:3000”, you are expected to see the user 
   interface of our application 

Current functionality 

I. Image uploading interface that could get response from backend which tells the name of object in image, to try: 

    1. Click “Choose file”, choose a .jpg or .png file and then click “Submit” 

    2. If you are using Chrome (recommended), Press f12, on the developer tool right hand side, click console 

    3. You are expected to see the response from backend that tell “Profile created successfully; this is a {object detected} 
