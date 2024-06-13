from django.shortcuts import render
from chat.agent import CompanyInfoAgent, FileUploadAgent
import os

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

def index(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        try:
            info_agent = CompanyInfoAgent()
            info = info_agent.handle_request(company_name)
        except KeyError as e:
            info = f"Error: Missing key {str(e)}"
        except Exception as e:
            info = f"An unexpected error occurred: {str(e)}"
        return render(request, 'index.html', {'info': info})
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            file_agent = FileUploadAgent()
            message = file_agent.handle_request(uploaded_file)
        except KeyError:
            message = "No file uploaded"
        except ValueError as e:
            message = str(e)
        except Exception as e:
            message = f"An unexpected error occurred: {str(e)}"
        return render(request, 'upload.html', {'message': message})
    return render(request, 'upload.html')
