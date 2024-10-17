# Invoice hoadondientu.gdt.gov.vn 

## Description
This project uses reverse engineering techniques to request the API of [hoadondientu.gdt.gov.vn](https://hoadondientu.gdt.gov.vn) for retrieving invoice data.

## Prerequisites

### Set up cookies
 
- You have a valid account on hoadondientu.gdt.gov.vn.
- You need to extract your cookies from [hoadondientu.gdt.gov.vn](https://hoadondientu.gdt.gov.vn) and save them in a file named `cookies.json`. The format of the file should be:

```json
[
    {"name": "name1", "value1": "value"},
    {"name": "name2", "value2": "value"},
    ...
]
```
#### recommendation 
- You can add cookies  [cookie-editor](https://cookie-editor.com/) to your browser for getting cookies json
- follow this [https://techhelpbd.com/en/how-to-use-cookies-in-pc-by-using-cookie-editor-extension/](https://techhelpbd.com/en/how-to-use-cookies-in-pc-by-using-cookie-editor-extension/) 

### Getting Started
1. First install packages in requirements.txt :
``` bash 
      pip install -r requirements.txt 
```

### Usage 

``` bash
      python getInvoice.py --type --month --year
```
- --type : type of invoice (purchase or sold)
- --month : month as a number (1-12)
- --year: Year as a number (e.g., 2024)

- All data will be stored in data_json & data_excel folder 

