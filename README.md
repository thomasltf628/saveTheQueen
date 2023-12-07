Setting up the Django backend 

#  1. Clone the project to your computer

Running this command on your command prompt:
      git clone --branch Importing_API_for_price_search https://github.com/thomasltf628/saveTheQueen.git <Directory path you want>
e.g. if you want to put it in C:\Users\super\OneDrive\Desktop\adcademic\1003 , then put : 
      git clone --branch Importing_API_for_price_search https://github.com/thomasltf628/saveTheQueen.git "C:\Users\super\OneDrive\Desktop\adcademic\1003"

#  2. Create and switch to your new branch before you make any change 

Running this command on your command prompt:
      git branch <your job>
e.g. if you are going to modify the interface:
      git branch modifying_interface

Run this command also to checkout your new branch:
      git checkout <branch you created>
e.g. if you created a branch 'modifying_interface'
      git checkout modifying_interface

#  3. Change directory to the virtual environment 

I. Go to the Repositry of project you just cloned, double click the folder 'backend', then click the folder 'myenv311', go to the path space, copy the directory path 
II. Running this command on your command prompt:
      cd <the directory path you copied>
e.g. if your directory path is 'C:\Users\thomas\Capstone_project\backend\myenv311'
      cd C:\Users\thomas\Capstone_project\backend\myenv311

#  4. Activate the virtual environment
Run this command:
      .\Scripts\activate
if error is encountered, try to run the command prompt as administrator and then run the command:       
      Set-ExecutionPolicy RemoteSigned
Then run this in the command prompt again:
      <your directory to the folder"myenv311">\Scripts\activate

#  5. Install the required library in the virtual environment
Make sure you are in the folder"myenv311"
      cd <your directory to the folder"myenv311">
Run the following command:
      pip install -r requirements.txt

#  6. Get the API key
Contact aurthor for the API key, create a file nameed "config.py" in the "todo" folder
Copy the API key to that file

#  7. Run the django server
Change the directory one step back:
      cd ..
Run server by:
      python manage.py runserver

#  8. Open browser, enter the link “127.0.0.1:8000/admin”, you are expected to see the administrator interface of Django 

 

Setting up the React frontend 

#  1. Install node.js
Download and the install node from https://nodejs.org/en/download

#  2. Check if node correctly installed
open command prompt and run this command:
     node –v
if node is correctly installed, you would see the version of node, if node is not found using VS code terminal, use command prompt instead

#  3. Change directory to (directory of your repository)/frontend 
Run this command:
      cd <directory of your repository>\frontend 
e.g. if your project is at the directory 'C:\Users\thomas\Capstone_project\frontend'
      cd C:\Users\thomas\Capstone_project\frontend 

#  4. Install npm
Run command:
      npm install

#  5. Start the react server
Run command:
      npm start

#  6. Browse the interface
Open your browser and type "127.0.0.1:3000” if it doesn't automatically showns


#  Current functionality 

I. Uploading a car image could get you the best deal of that model of car on used car platform

    1. Click “Choose file”, choose a .jpg or .png file and then click “Submit” 

    2. If you are using Chrome (recommended), Press f12, on the developer tool right hand side, click console 

    3. You are expected to see the make and model of the car and respective best deals avaliable on used car platforms ordered by prices
