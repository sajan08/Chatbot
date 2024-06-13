# Company Chatbot

## Setup Instructions

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure the PostgreSQL database in `settings.py`.

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the server:
    ```bash
    python manage.py runserver
    ```

## User Guide

### Getting Company Information

1. Enter the company name in the text field on the homepage.
2. Click "Get Info" to retrieve the company information.

### Uploading Files

1. Navigate to the "Upload" page.
2. Select a PDF or DOC file to upload.
3. Click "Upload" to upload the file.

## Testing

- Verify company information retrieval with various company names.
- Test file upload functionality with different file types.
