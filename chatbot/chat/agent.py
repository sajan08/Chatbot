import os

# Simulated company information database
COMPANY_DATABASE = {
    "OpenAI": {
        "description": "An AI research and deployment company.",
        "founder": "Elon Musk, Sam Altman, and others",
        "founded": "2015",
        "employees": "500+"
    },
    "Google": {
        "description": "A multinational technology company specializing in Internet-related services and products.",
        "founder": "Larry Page and Sergey Brin",
        "founded": "1998",
        "employees": "100,000+"
    }
}

class CompanyInfoAgent:
    def __init__(self):
        pass

    def get_company_info(self, company_name):
        # Retrieve information from the simulated database
        company_info = COMPANY_DATABASE.get(company_name, None)
        if company_info:
            return {
                "name": company_name,
                "description": company_info["description"],
                "founder": company_info["founder"],
                "founded": company_info["founded"],
                "employees": company_info["employees"]
            }
        else:
            return {"message": f"No information available for {company_name}"}
        
    @classmethod
    def handle_request(cls, company_name):
        agent = cls()
        return agent.get_company_info(company_name)


class FileUploadAgent:
    def __init__(self):
        pass

    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'pdf', 'docx'}
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def handle_file_upload(self, file):
        if not self.allowed_file(file.name):
            raise ValueError(f"File type not allowed. Only PDF and DOCX files are supported.")
        
        # Simulate saving the file to a directory
        file_path = os.path.join('uploads', file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        return f"File {file.name} uploaded successfully and saved to {file_path}"

    @classmethod
    def handle_request(cls, file):
        agent = cls()
        return agent.handle_file_upload(file)