# shopping-cart

# General Environement Setup

Create a virtual environment:

```sh
conda create -n shoppingcart-env python=3.8
```

Activate the virtual environment:

```sh
conda activate shoppingcart-env
```

Install package dependencies (which are individual listed out later in the README):

```sh
pip install -r requirements.txt
```

# Environment Variables - ".env" File Approach


# SendGrid API Key Setup
First, [sign up for a SendGrid account](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys), then follow the instructions to complete your "Single Sender Verification", clicking the confirmation email to verify your account. 
NOTE: some users in the passed have reported issues with using yahoo-issued, university-issued, or work-issued emails in the past. Consequently, if you run into similar issues when attempt to set up your SendGrid account, perhaps consider using a personal Gmail account. 

Then, [create your SendGrid API Key with "full access" permissions](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys). Once you create your SendGrid API Key, we will want to store the API Key in an environment variable in the .env file called ```SENDGRID_API_KEY```. Also set an environment variable called ```SENDER_ADDRESS``` to be the same email address as the single sender address you just associated with your SendGrid account.

Use a ".env" file approach to manage these files, as mentioned in the ".env file approach" section above. 

# Google Sheet API Key Setup
Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials page](https://console.developers.google.com/apis/credentials), follow a process to create and download credentials to use the APIs:

1. Click "Create Credentials" for a "Service Account". Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
2. Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account. Download the resulting .json file (this might happen automatically).
3. Move a copy of the credentials file into your project repository, typically into the root directory or perhaps a directory called "auth", and note its filepath. For the example below, we'll refer to a file called "google-credentials.json" in an "auth" directory (i.e. "auth/google-credentials.json").
Finally, before committing, add the credentials filepath to your repository's ".gitignore" file to ensure it does not get tracked in version control or uploaded to GitHub:
```sh
# the .gitignore file

# ignore environment variables in the ".env" file:
.env

# ignore the google api credentials file at the following location:
auth/google-credentials.json
```
## Configuring Google Spreadsheet Document 
Use this [example Google Sheet](https://docs.google.com/spreadsheets/d/1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE/), or create your own. Note the document's unique identifier (e.g. ```1_hisQ9kNjmc-cafIasMue6IQG-ql_6TcqFGpVNOkUSE```) from its URL, and store the identifier in an environment variable called ```GOOGLE_SHEET_ID```.

If you create your own, make sure it contains a sheet called "shopping-clean" with column headers ```id```, ```name```, ```department```, ```price```, and ```availability_date```. If you choose a different sheet name, customize it via an environment variable called ```SHEET_NAME```. Finally, modify the document's sharing settings to grant "edit" privileges to the "client email" address specified in the credentials file.


# Usage
Once you have properly set up your local environment, installed all necessary packages, and set up your SendGrid API Key and Google Spreadsheet API Key credentials, you are ready to run the program. 
In order to run the program, please enter the following in the command line: 
```sh
python shopping_cart.py
```

## Sales Tax Rate Configuration
By default, the sales tax rate will be automatically set to the NY State Sales Tax Rate of 8.75%.
In order to configure the program to your state's specific sales tax rate, please enter the following when running the program:
```sh
TAX_RATE="Tax Rate" python game.py
```
