from openai import OpenAI
import pandas as pd
client = OpenAI()

df = pd.read_csv("data.csv")

# Convert each column to a list using pandas
columns = {col: df[col].tolist() for col in df.columns}

print("Processing Dates...")
dates_response = client.responses.create(
    model="gpt-5-nano",
    input="Turn this list of dates into a standardized MM/DD/YYYY format where the month day and year are separated by / and the items stay in their original order. All dates provided contain a month date and year, and do not return any other output than the CSV formatted dates.\n " + ",".join(str(columns.get("Date")))
)

dates = dates_response.output_text
dates = dates.split(",")

print("Processing Merchants...")
merchants_response = client.responses.create(
    model="gpt-5-nano",
    input="Turn this list of merchants into a standardized CSV format where duplicate merchants with slightly different names are aligned to have the same name. Make sure that all values are outputted in their original order with the updated names.  (e.g., UBER *TRIP,Uber Technologies,UBER EATS would become Uber,Uber,Uber).\n" + ",".join(str(columns.get("Merchant")))
)

merchants = merchants_response.output_text
merchants = merchants.split(",")

print("Processing Amounts...")
amounts_response = client.responses.create(
    model="gpt-5-nano",
    input="Turn this list of amonuts of money into a standardized CSV format with all non numeric elements removed while keeping elements in order. (e.g. $5,1.20 USD,4.00,3 becomes 5,1.20,4.00,3).\n" + ",".join(str(columns.get("Amount")))
)

amounts = amounts_response.output_text
amounts = amounts.split(",")

# Get top merchant by spending amount
totals = {}
for merchant, amount in zip(merchants, amounts):
    totals[merchant] = totals.get(merchant, 0) + float(amount)

top_merchant = max(totals, key=totals.get)
print("The max spending category was " + top_merchant + " with a total amount of " + str(round(totals[top_merchant], 2)))

# Get top date by spending amount
totals = {}
for date, amount in zip(dates, amounts):
    totals[date] = totals.get(date, 0) + float(amount)

top_date = max(totals, key=totals.get)
print("The max spending date was " + top_date + " with a total amount of " + str(round(totals[top_date], 2)))