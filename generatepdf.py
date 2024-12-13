# generatepdf.py
from fpdf import FPDF
import datetime
from PySide6.QtWidgets import QMessageBox

def save_pdf(employee_data, pdf_file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Employee Registration", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)

    fields = {
            "Employee ID": employee_data.get('employee_id', 'N/A'),
            "First Name": employee_data.get('first_name', 'N/A'),
            "Middle Name": employee_data.get('middle_name', 'N/A'),
            "Last Name": employee_data.get('last_name', 'N/A'),
            "Position": employee_data.get('position', 'N/A'),
            "Date Employed": datetime.datetime.now().strftime('%Y-%m-%d'),
            "Date of Birth": employee_data.get('date_of_birth', 'N/A'),
            "Place of Birth": employee_data.get('place_of_birth', 'N/A'),
            "Citizenship": employee_data.get('citizenship', 'N/A'),
            "Passport Number": employee_data.get('passport_num', 'N/A'),
            "Contact Number": employee_data.get('contact_num', 'N/A'),
            "Email": employee_data.get('email', 'N/A'),
            "Damage Address": employee_data.get('dmg_address', 'N/A'),
            "Home Address": employee_data.get('home_address', 'N/A'),
            "Civil Status": employee_data.get('civil_status', 'N/A'),
            "Spouse Name": employee_data.get('spouse_name', 'N/A'),
            "Place of Marriage": employee_data.get('place_of_marriage', 'N/A'),
            "Date of Marriage": employee_data.get('date_of_marriage', 'N/A'),
            "Child 1 Name": employee_data.get('child1_name', 'N/A'),
            "Child 1 Birthdate": employee_data.get('child1_birthdate', 'N/A'),
            "Child 2 Name": employee_data.get('child2_name', 'N/A'),
            "Child 2 Birthdate": employee_data.get('child2_birthdate', 'N/A'),
            "Elementary School": employee_data.get('elementary_school', 'N/A'),
            "Elementary Address": employee_data.get('elementary_address', 'N/A'),
            "Elementary Diploma": employee_data.get('elem_diploma', 'N/A'),
            "Elementary Year Graduated": employee_data.get('elem_yeargraduated', 'N/A'),
            "High School Name": employee_data.get('highschool_name', 'N/A'),
            "High School Address": employee_data.get('highschool_address', 'N/A'),
            "High School Diploma": employee_data.get('highschool_diploma', 'N/A'),
            "High School Year Graduated": employee_data.get('highschool_yeargraduated', 'N/A'),
            "College Name": employee_data.get('college_school', 'N/A'),
            "College Address": employee_data.get('college_address', 'N/A'),
            "College Diploma": employee_data.get('college_diploma', 'N/A'),
            "College Year Graduated": employee_data.get('college_yeargraduated', 'N/A'),
            "Graduate School": employee_data.get('graduate_school', 'N/A'),
            "Graduate Address": employee_data.get('graduate_address', 'N/A'),
            "Graduate Diploma": employee_data.get('graduate_diploma', 'N/A'),
            "Graduate Year Graduated": employee_data.get('graduate_yeargraduated', 'N/A'),
            "Related Staff 1": employee_data.get('related_staff1', 'N/A'),
            "Related Staff 1 Relationship": employee_data.get('related_staff1_relationship', 'N/A'),
            "Related Staff 1 Position": employee_data.get('related_staff1_position', 'N/A'),
            "Related Staff 2": employee_data.get('related_staff2', 'N/A'),
            "Related Staff 2 Relationship": employee_data.get('related_staff2_relationship', 'N/A'),
            "Related Staff 2 Position": employee_data.get('related_staff2_position', 'N/A'),
            "Scholarship Awards": employee_data.get('scholarship_awards', 'N/A'),
            "Publications": employee_data.get('publications', 'N/A'),
            "Name of Employer": employee_data.get('name_of_employer', 'N/A'),
            "Position at Workplace": employee_data.get('position_workplace', 'N/A'),
            "Period of Employment": employee_data.get('period_of_employment', 'N/A'),
            "Reason for Leaving": employee_data.get('reason_for_leaving', 'N/A'),
            "Employer Address": employee_data.get('employer_address', 'N/A'),
            "Government Examinations": employee_data.get('government_examinations', 'N/A'),
            "Government Rating": employee_data.get('government_rating', 'N/A'),
            "Government Date": employee_data.get('government_date', 'N/A'),
            "Government Place": employee_data.get('government_place', 'N/A'),
            "Criminal Case Name": employee_data.get('criminal_case_name', 'N/A'),
        }

    for label, value in fields.items():
        pdf.cell(50, 10, label + ":", ln=False)
        pdf.cell(0, 10, str(value), ln=True)

    pdf.output(pdf_file_path)

    QMessageBox.information(None, "Success", f"PDF saved successfully at:\n{pdf_file_path}")
