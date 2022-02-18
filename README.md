# shopping-cart

## General Environement Setup

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

# SendGrid API Key Setup
First, [sign up for a SendGrid account](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys), then follow the instructions to complete your "Single Sender Verification", clicking the confirmation email to verify your account. 
NOTE: some users in the passed have reported issues with using yahoo-issued, university-issued, or work-issued emails in the past. Consequently, if you run into similar issues when attempt to set up your SendGrid account, perhaps consider using a personal Gmail account. 

Then, [create your SendGrid API Key with "full access" permissions](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys). Once you create your SendGrid API Key, we will want to store the API Key in an environment variable in the .env file called ```SENDGRID_API_KEY```. Also set an environment variable called ```SENDER_ADDRESS``` to be the same email address as the single sender address you just associated with your SendGrid account.

Use a ".env" file approach to manage these files, as mentioned in the ".env file approach" section above. 

# Google Sheet API Key Setup



## Usage

```sh
python shopping_cart.py
```

## Sales Tax Rate Configuration
In order to configure your individual sales tax rate, please enter the following when running the program:
```sh
TAX_RATE="Tax Rate" python game.py
```
Otherwise, the default tax rate will always be set to the NY States Sales Tax Rate of 8.75%.

# Sending Receipts via Email

```sh 
pip install sendgrid
```
You also have the option to install a specific version of sengrid:
```sh
pip install sendgrid==6.6.0
```

# Google Sheet Integration 
```sh
pip install gspread 
pip install oauth2client
```
