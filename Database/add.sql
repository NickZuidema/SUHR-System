INSERT INTO Employee (Employee_Id, Last_Name, First_Name, Middle_Name, Date_Employed, Position_Id, Dgte_Address, Home_Address, Date_Of_Birth, Place_Of_Birth, Citizenship, Non_Filipino_Id, Church, Tax_Id, Sss_No, Philhealth_No, Pagibig_No, Civil_Status, Spouse_Id, Academic_Id, Criminal_Record, Regular, Benefit_Id, Salary_Id, Contact_No, Archived) 
VALUES 
('E001', 'Doe', 'John', 'A', '2022-05-10', 1, 'Dgte Street 123', 'Home Street 456', '1985-06-25', 'Dumaguete', 'Filipino', NULL, 'Local Church', '123-456-789', '1234567', 'PH123456', 'PG123456', 'Single', NULL, 1, NULL, 1, 1, 1, '09123456789', 0);

INSERT INTO Employee (Employee_Id, Last_Name, First_Name, Middle_Name, Date_Employed, Position_Id, Dgte_Address, Home_Address, Date_Of_Birth, Place_Of_Birth, Citizenship, Non_Filipino_Id, Church, Tax_Id, Sss_No, Philhealth_No, Pagibig_No, Civil_Status, Spouse_Id, Academic_Id, Criminal_Record, Regular, Benefit_Id, Salary_Id, Contact_No, Archived) 
VALUES 
('E002', 'Smith', 'Jane', NULL, '2021-07-15', 2, 'Dgte Street 789', 'Home Street 123', '1990-04-18', 'Manila', 'Non-Filipino', 1, NULL, '987-654-321', '7654321', 'PH654321', 'PG654321', 'Married', 'S001', 2, NULL, 1, 2, 2, '09876543210', 0);


INSERT INTO Non_Filipino (Non_Filipino_Id, Passport_No, Acr_No, Date_Of_Issue, Place_Of_Issue) 
VALUES 
(1, 'P1234567', 'ACR123456', '2019-08-01', 'Manila');

INSERT INTO Non_Filipino (Non_Filipino_Id, Passport_No, Acr_No, Date_Of_Issue, Place_Of_Issue) 
VALUES 
(2, 'P7654321', 'ACR654321', '2020-02-14', 'Cebu');


INSERT INTO Organization (Organization_Id, Name) 
VALUES 
(1, 'Tech Corp');

INSERT INTO Organization (Organization_Id, Name) 
VALUES 
(2, 'Health Solutions');




INSERT INTO User (User_Id, Password) 
VALUES 
('E001', 'password123');

INSERT INTO User (User_Id, Password) 
VALUES 
('E002', 'password789');

INSERT INTO User (User_Id, Password) 
VALUES 
('111', '111');

INSERT INTO User (User_Id, Password) 
VALUES 
('admin', 'admin');





INSERT INTO Employee_Organization (Employee_Employee_Id, Organization_Organization_Id) 
VALUES 
('E001', 1);

INSERT INTO Employee_Organization (Employee_Employee_Id, Organization_Organization_Id) 
VALUES 
('E002', 2);




INSERT INTO Child (Child_Id, Last_Name, First_Name, Middle_Name, Date_Of_Birth) 
VALUES 
('C001', 'Doe', 'Emily', 'B', '2015-03-12');

INSERT INTO Child (Child_Id, Last_Name, First_Name, Middle_Name, Date_Of_Birth) 
VALUES 
('C002', 'Smith', 'Jake', 'M', '2017-07-09');



INSERT INTO Employee_Child (Employee_Employee_Id, Child_Child_Id) 
VALUES 
('E001', 'C001');

INSERT INTO Employee_Child (Employee_Employee_Id, Child_Child_Id) 
VALUES 
('E002', 'C002');




INSERT INTO Spouse_Info (Spouse_Info_Id, Date_Of_Marriage, Place_Of_Marriage) 
VALUES 
(1, '2018-09-12', 'Cebu');

INSERT INTO Spouse_Info (Spouse_Info_Id, Date_Of_Marriage, Place_Of_Marriage) 
VALUES 
(2, '2017-05-23', 'Manila');




INSERT INTO Parent (Parent_Id, Last_Name, First_Name, Middle_Name, Occupation, Address) 
VALUES 
('P001', 'Doe', 'John Sr.', NULL, 'Teacher', 'Home Street 123');

INSERT INTO Parent (Parent_Id, Last_Name, First_Name, Middle_Name, Occupation, Address) 
VALUES 
('P002', 'Smith', 'Jane Sr.', 'B', 'Doctor', 'Health Avenue 456');



INSERT INTO Employee_Parent (Employee_Employee_Id, Parent_Parent_Id) 
VALUES 
('E001', 'P001');

INSERT INTO Employee_Parent (Employee_Employee_Id, Parent_Parent_Id) 
VALUES 
('E002', 'P002');



INSERT INTO Sibling (Sibling_Id, Last_Name, First_Name, Middle_Name, Occupation, Address) 
VALUES 
('S001', 'Doe', 'Sam', 'A', 'Engineer', 'City Street 789');

INSERT INTO Sibling (Sibling_Id, Last_Name, First_Name, Middle_Name, Occupation, Address) 
VALUES 
('S002', 'Smith', 'Sophia', 'C', 'Nurse', 'Medical Street 123');



INSERT INTO Employee_Sibling (Employee_Employee_Id, Sibling_Sibling_Id) 
VALUES 
('E001', 'S001');

INSERT INTO Employee_Sibling (Employee_Employee_Id, Sibling_Sibling_Id) 
VALUES 
('E002', 'S002');



INSERT INTO Spouse (Spouse_Id, Last_Name, First_Name, Middle_Name, Spouse_Info_Id) 
VALUES 
('S001', 'Smith', 'Anna', 'B', 1);

INSERT INTO Spouse (Spouse_Id, Last_Name, First_Name, Middle_Name, Spouse_Info_Id) 
VALUES 
('S002', 'Doe', 'Linda', 'M', 2);



INSERT INTO Benefit (Benefit_Id, Education, Medical) 
VALUES 
(1, 10000.00, 5000.00);

INSERT INTO Benefit (Benefit_Id, Education, Medical) 
VALUES 
(2, 12000.00, 6000.00);




INSERT INTO Attendance (Attendance_Id, Employee_Id, Date, Time_In, Time_Out, Remarks) 
VALUES 
(1, 'E001', '2024-10-05', '08:00', '17:00', 'On time');

INSERT INTO Attendance (Attendance_Id, Employee_Id, Date, Time_In, Time_Out, Remarks) 
VALUES 
(2, 'E002', '2024-10-05', '08:30', '17:30', 'Late arrival');




INSERT INTO Salary (Salary_Id, Monthly_Salary, Overtime_Salary, Total_Salary) 
VALUES 
(1, 30000.00, 2000.00, 32000.00);

INSERT INTO Salary (Salary_Id, Monthly_Salary, Overtime_Salary, Total_Salary) 
VALUES 
(2, 35000.00, 2500.00, 37500.00);




INSERT INTO Academic_Record (Academic_Id, Elementary_Id, Elementary_Fin, HighSchool_Id, HighSchool_Fin, SeniorHigh_Id, SeniorHigh_Diploma, SeniorHigh_Fin, College_Id, College_Diploma, College_Fin, GradSchool_Id, GradSchool_Diploma, GradSchool_Fin) 
VALUES 
(1, 101, '2001', 102, '2005', 103, 'Diploma', '2007', 104, 'Degree', '2011', 105, 'Masters', '2015');

INSERT INTO Academic_Record (Academic_Id, Elementary_Id, Elementary_Fin, HighSchool_Id, HighSchool_Fin, SeniorHigh_Id, SeniorHigh_Diploma, SeniorHigh_Fin, College_Id, College_Diploma, College_Fin, GradSchool_Id, GradSchool_Diploma, GradSchool_Fin) 
VALUES 
(2, 106, '2002', 107, '2006', 108, 'Diploma', '2008', 109, 'Degree', '2012', 110, 'Masters', '2016');



INSERT INTO School (School_Id, School_Name, School_Address) 
VALUES 
(101, 'Elementary School 1', 'Street 1'),
(102, 'High School 1', 'Street 2'),
(103, 'Senior High School 1', 'Street 3'),
(104, 'College 1', 'Street 4'),
(105, 'Graduate School 1', 'Street 5');



INSERT INTO User (User_Id, Password) 
VALUES 
('111', '111');

INSERT INTO User (User_Id, Password) 
VALUES 
('admin', 'admin');