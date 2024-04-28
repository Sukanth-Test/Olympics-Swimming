# Install Python and Anaconda3 Latest Version
- Python Download Link: https://www.python.org/downloads/
- Anaconda3 Download Link (for Windows): https://docs.anaconda.com/free/anaconda/install/windows/ 
- **NOTE:** Ensure you select the check box "Add Python to Path" and "Add Anaconda3 to Path" while insatlling python and anaconda3 respectively.
- In your command prompt when you type the commands **"python --version"** and **"conda --version"**, and if you see respective versions of the softwares, then your installation process is successful.
- Having Anaconda3 is optional, you can install packages using python venv or without virtual environment. But it is recommended to use conda to work with seperate virtual environments for individual projects.

# Create Conda Environment and Install Packages
- Once you successfully installed anaconda3 in your system, now you need to create a virtual environment.
- Go to Anaconda Prompt, initially it is activated in **base** environment.
- Deactivate base environment using **"conda deactivate"** command.
- Now create a new virtual environment with name "my_venv" and python version of 3.9 using the command **"conda create -n my_env python==3.9"**
- Now activate the newly creted environment using the command **"conda activate my_env"**
- Install the packages from requirement.txt using the command **"pip install -r requirements.txt"**
- **NOTE:** Whenever you work with this project you need to activte this conda environment.

# Running Streamlit App
- We have app.py file which is a python code to deploy the model in a web app using streamlit library.
- To run the app, type the command in the terminal **"streamlit run app.py"** and click enter.
- You will be redirected to a localhost web app.
- If you are not redirected, manually click on the Local URL: http://localhost:8501.

## That's it. Happy Coding!
