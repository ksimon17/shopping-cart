# shopping_cart.py
# Bonus Exercises Completed - 1, 4, and 6

from asyncio import selector_events
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient # Sendgrid Email Bonus Section
from sendgrid.helpers.mail import Mail # Sendgrid Email bonus Section
import gspread # Google Sheet Bonus Section
from oauth2client.service_account import ServiceAccountCredentials # Google Sheet Bonus Section
from datetime import datetime # for displaying the date and time 

load_dotenv()


# Sengrid Email Bonus Section
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")



# Google Sheet Bonus Section
DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="shopping-clean")


# Global Variables
tax_rate = float(os.getenv("TAX_RATE", default=0.0875)) # BONUS EXERCISE 1 - CONFIGURING SALES TAX RATE
selected_ids = [] 
subtotal = 0
tax = 0
final_price = 0
products = [] # to hold the list of dictionaries read in from the google sheet



# BONUS EXERCISE 4 - SENDING RECEIPTS VIA EMAIL
def send_email(selected_ids, matching_prices, subtotal, tax, final_price, user_email = "SENDER_ADDRESS"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    #print("CLIENT:", type(client))

    #print("USER EMAIL:", user_email)

    ids_and_prices = []
    for x in range(0,len(matching_prices)):
        ids_and_prices.append(selected_ids[x] + " (" + matching_prices[x] + ")")

    subject = "Your Receipt from the Green Grocery Store"

    # html_content = "Hello World"
    # print("HTML:", html_content)

    html_list_items = ""
    for item in ids_and_prices:
        html_list_items += f"<li>You ordered: Product {item} </li>" 

    html_content = f"""
    <h3>Hello this is your receipt</h3>
    <p>Date: {datetime.today().strftime("%B %d, %Y %I:%M %p")}</p>
    <p>Subtotal: {to_usd(subtotal)}</p>
    <p>Tax: {to_usd(tax)}</p>
    <p>Total Price: {to_usd(final_price)}</p>
    <ol>
        {html_list_items}
    </ol>
    """
    #print(html_content)

    # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
    # ... but we can customize the `to_emails` param to send to other addresses
    message = Mail(from_email=SENDER_ADDRESS, to_emails=user_email, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        # print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        # print(response.status_code) #> 202 indicates SUCCESS
        # print(response.body)
        # print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)


# BONUS EXERCISE 6 - INTERGRATING WITH A GOOGLE SHEETS DATASTORE
def google_sheet_integration():
    #
    # AUTHORIZATION
    #
    # see: https://gspread.readthedocs.io/en/latest/api.html#gspread.authorize
    # ... and FYI there is also a newer, more high level way to do this (see the docs)

    # an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google-credentials.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
   # print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

    client = gspread.authorize(credentials)
    #print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>

    #
    # READ SHEET VALUES
    #
    # see: https://gspread.readthedocs.io/en/latest/api.html#client
    # ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
    # ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet

    #print("-----------------")
    #print("READING DOCUMENT...")

    doc = client.open_by_key(DOCUMENT_ID)
    #print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

    sheet = doc.worksheet(SHEET_NAME)
    #print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records()
    # print("ROWS:", type(rows)) #> <class 'list'>

    # for row in rows:
    #     print(row) #> <class 'dict'>

    return rows
    

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# ****************************
# READ IN THE APPROPRIATE DATA
# ****************************

products = google_sheet_integration() # BONUS CHALLENGE 6 - GOOGLE SHEET INTEGRATION

#store acceptable input from products for input validation
acceptable_inputs = []
for p in products:
    acceptable_inputs.append(str(p['id']))

# *************************
# INFO CAPTURE / INFO INPUT
# *************************

# GREETING THE USER AND INFORMING THEM HOW TO INTERACT WITH THE PROGRAM
print("---------------------------------")
print("HELLO, WELCOME TO CHECKOUT AT GREEN FOODS GROCERY!")
print("Please input the product identifier for all items in your shopping cart")
print("Once you are finished with all of your items, input 'DONE' to exit the program!")
print("You will receipt a copy receipt at the end of the checkout process")
print("---------------------------------")

# LOOP WHERE THE USER ENTER IDs OF THEIR SELECTED PRODUCTS
while True:
    product_id = input("Please input a product identifier: ")
    if product_id.upper() == "DONE":
        break
    elif product_id not in acceptable_inputs:
        print("Sorry, that is not a valid product id. If you are finished checking your") 
        print("products and wish to exit the program, enter 'DONE' at the next prompt.")
        print("Otherwise Please try again! ")
    else:
        selected_ids.append(product_id)

# *********************
# INFO DISPLAY / OUTPUT
# *********************
print("---------------------------------")
print("Thank you for inputting your items. You will receive your receipt shortly.")


# DISPLAY RECEIPT TO USER
print("---------------------------------")
print("YOUR RECEIPT:")
print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WEBSITE: WWW.GREEN-FOODS-GROCERY.COM")
print("ADDRESS: 3700 O St NW, Washington, DC 20057")
print("PHONE NUMBER: (202) 687-0100")
print("---------------------------------")
print("CHECKOUT AT:", datetime.today().strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS: ")

matching_prices= []
# DISPLAY SELECTED PRODUCTS TO THE USER AND CALCULATE SUBTOTAL
for selected_id in selected_ids:
    matching_rows = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_rows[0]
    subtotal = subtotal + matching_product["price"]
    matching_prices.append(to_usd(matching_product["price"]))
    print(" ...", matching_product["name"], "(" + str(to_usd(matching_product["price"])) + ")")

# CALCULATE TAX AND FINAL PRICE
tax = subtotal * tax_rate
final_price = subtotal + tax

# DISPLAY TOTALS TO USER
print("---------------------------------")
print("SUBTOTAL: " + str(to_usd(subtotal)))
print("TAX: " + str(to_usd(tax)))
print("TOTAL: " + str(to_usd(final_price)))
print("---------------------------------")


# PROVIDE THE USER WITH THE OPTION TO RECEIVE AN EMAIL COPY OF THEIR RECEIPT
email_boolean = input("Please enter 'yes' if you wish to receive a copy of your receipt via email. Otherwise, just press enter: ")
if email_boolean.lower() == "yes":
    user_email = input("Please enter your email: ")
    if user_email == "":
        user_email = SENDER_ADDRESS
    send_email(selected_ids, matching_prices, subtotal, tax, final_price, user_email) # BONUS EXERCISE 4 - SENDING RECEIPTS VIA EMAIL

print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")