import requests
import os
import argparse
import json
from load_cookies import load_cookies_from_json

# Create argument parser
parser = argparse.ArgumentParser(description="Get type, month and year from command line.")

# Add arguments for month and year
parser.add_argument('--type', type=str, required=True, help="type of invoice (purchase or sold)")
parser.add_argument('--month', type=int, required=True, help="Month as a number (1-12)")
parser.add_argument('--year', type=int, required=True, help="Year as a number (e.g., 2024)")

# Parse the arguments
args = parser.parse_args()

# Access the arguments
month = f"{args.month:02d}"  # Format the month to have two digits
year = args.year
cookies = load_cookies_from_json('cookies.json')

# Print or use the values
print(f"Month: {month}, Year: {year}")

#get argument month 


url = "https://hoadondientu.gdt.gov.vn:30000/query/invoices/purchase"
state = None
TOTAL = 0


search = f"tdlap=ge=01/{month}/{year}T00:00:00;tdlap=le=31/{month}/{year}T23:59:59;ttxly==5"
os.environ['REQUESTS_CA_BUNDLE'] = 'C:\working\\nhi\\venv\Lib\site-packages\certifi\cacert.pem' 
# Parameters from the image
params = {
    "sort": "tdlap:desc,khmshdon:asc,shdon:desc",
    "size": 50,
    "search": search
    
}

# Headers (Add the necessary headers as per your requirements)
headers = {
    "Host": "hoadondientu.gdt.gov.vn:30000",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Action": "T%C3%ACm%20ki%E1%BA%BFm%20(h%C3%B3a%20%C4%91%C6%A1n%20mua%20v%C3%A0o)",  # URL encoded value
    "Authorization": f"Bearer {cookies['jwt']}",  # Replace 'mytoken' with your actual token
    
    "End-Point": "/tra-cuu/tra-cuu-hoa-don",
    "Origin": "https://hoadondientu.gdt.gov.vn",
    "Connection": "keep-alive",
    "Referer": "https://hoadondientu.gdt.gov.vn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Priority": "u=0"
}

# Sending the GET request

def getInvoice(url, headers, params, cookies, state ,size = 50)-> list:

    if state != None:
        params['state'] = state
    

    params['size'] = size
    
    response = requests.get(url, headers=headers, params=params, verify=False, cookies=cookies)
    
    
    data = response.json()
    
    if len(data['datas']) < size:
        return data
    
    total = data['total']
    state = data['state']
    
    invoices_list = getInvoice(url, headers, params, cookies, state, size)
    
    invoices_list['datas'] = data['datas'] + invoices_list['datas']
    
    return invoices_list
# Print the response text (raw) and JSON (if applicable)
if __name__ == "__main__":
    

    data = getInvoice(url, headers, params, cookies, state)


    # # save data to json file


    json_output_path = f"data_json/data-{month}-{year}"
    # Save with UTF-8 encoding and proper Vietnamese characters
    with open(f'{json_output_path}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Data saved with UTF-8 encoding.")


    from extractThueExcel import save_to_excel
    excel_output_path = f"data_excel/data-{month}-{year}"

    save_to_excel(f'{json_output_path}.json', f'{excel_output_path}.xlsx')


