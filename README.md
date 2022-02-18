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

# Sendgrid API Key Setup

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
