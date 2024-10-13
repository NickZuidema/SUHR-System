from fpdf import FPDF
import os

class PDFGenerator:
    def __init__(self, save_path):
        self.save_path = save_path

    def save_pdf(self, employee_data):
        pdf = FPDF()
        pdf.add_page()

        # Add title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Employee Registration Details", ln=True, align='C')

        # Add employee data
        pdf.set_font("Arial", size=12)
        fields = [
            "Employee ID", employee_data["employee_id"],
            "First Name", employee_data["first_name"],
            "Middle Name", employee_data["middle_name"],
            "Last Name", employee_data["last_name"],
            "Position", employee_data["position"],
            "Dgte Address", employee_data["dmg_address"],
            "Home Address", employee_data["home_address"],
            "Date of Birth", employee_data["date_of_birth"],
            "Place of Birth", employee_data["place_of_birth"],
            "Citizenship", employee_data["citizenship"],
            "Non-Filipino Passport No", employee_data.get("passport_num", ""),
            # Add additional fields as needed...
        ]

        for i in range(0, len(fields), 2):
            pdf.cell(0, 10, f"{fields[i]}: {fields[i + 1]}", ln=True)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.save_path), exist_ok=True)

        pdf.output(self.save_path)
