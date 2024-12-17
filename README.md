# LambdaTest Certification - Playwright (PYTHON)

This project was created to meet the challenge of Lambdatest certification with Playwright,
Python and running the LambdaTest platform with GitPod to execute the project.

**Prerequisites**
- Python 3 & Pip
- LambdaTest Account - https://www.lambdatest.com/

# Configure environment variables
To run the test on the LambdaTest platform remotely, you need to configure the environment variables
which are in the settings.py file (LN11 / LN12)

![image](https://github.com/user-attachments/assets/69976eec-8f76-436f-9047-f35e8cc1e441)

-----

- Inside LambdaTest in the "Automation" tab, click on "Access Key"
  
![image](https://github.com/user-attachments/assets/a1347bec-9d24-47e1-a3c5-73030ddd91d5)

- Configure the environment variables on your machine with the LambdaTest values
```bash
export LT_USERNAME="<Username>"
export LT_ACCESS_KEY="<Access Key>"
```

# Run the project with Gitpod
- Install the Gitpod browser extension
  https://www.gitpod.io/docs/configure/user-settings/browser-extension

- When accessing the repository, click the "Open" button
![Screenshot 2024-08-23 at 12 14 42](https://github.com/user-attachments/assets/9941ed99-54ed-451b-9f97-0ea3630a20ba)


- Once your GitPod workspace connects, run the project in the terminal
```bash
# Run tests serial mode
pytest test_playwright.py

# run tests parallel mode
pytest test_playwright.py -n 3
```

# Local Installation and Run
```bash
# Clone repository
git clone https://github.com/WallPetrucci/LambdaTestPlaywrightCertification

# Enter the project directory
cd LambdaTestPlaywrightCertification

# Install dependencies
pip install -r requirements.txt
playwright install-deps
playwright install

# Run tests serial mode
pytest test_playwright.py

# Run tests parallel mode
pytest test_playwright.py -n 3
```

**Any questions? Contact us!**

Wallace - Linkedin: https://www.linkedin.com/in/wallacepetrucci - wallacepetrucci@gmail.com

Project Link: https://github.com/WallPetrucci/LambdaTestPlaywrightCertification
