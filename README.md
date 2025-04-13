# Addressing the Lusophone technological wishlist proposals - Task 1

## Objective of the task:

Create a JavaScript script to manipulate a json object and print it in a human legible format.

## My approach:

- create a function ```formatDate()``` to transform the date into the required format eg January 12, 2018
- transform each object in the provided input data into a formatted string containing its title, page ID, and creation date and store in a ```results``` array.
- get the *results* element in which the data will be displayed
- assign the content of the *results* element to the ```results``` array (with its contents separated by a newline.)
  
---

# Addressing the Lusophone Technological Wishlist Proposals – Task 2

## Objective of the task
Create a Python script that reads a list of URLs from a CSV file, then fetches and prints the HTTP status code for each URL.

## My approach

1. Define **`load_urls(file_path)`**  which: 
   - Reads URLs from the specified CSV file.
   - Returns a list of URLs.

2. Define **`fetch_status(session, url)`** which:
   - Makes an asynchronous GET request to the given URL.
   - Prints `(STATUS CODE) URL` when successful or `(ERR) URL — ErrorType` if a connection issue occurs.

3. Define **`main()`** which: 
   - Loads all URLs from the CSV file.
   - Uses `aiohttp` to create a session.
   - Concurrently makes requests to all URLs and prints their status codes.

4. **Running the Script**  
   - Invoke the script as a standalone program using `python3 <script_name>.py` (e.g., `python3 Task\ 2.py`).

