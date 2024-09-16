PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS "Employee"
(
    "Employee_Id" TEXT NOT NULL,
    "Last_Name" TEXT NOT NULL,
    "First_Name" TEXT NOT NULL,
    "Middle_Name" TEXT,
    "Date_Employed" TEXT NOT NULL, -- Use TEXT for dates
    "Position_Id" INTEGER,
    "Dgte_Address" TEXT,
    "Home_Address" TEXT,
    "Date_Of_Birth" TEXT, -- Use TEXT for dates
    "Place_Of_Birth" TEXT,
    "Citizenship" TEXT NOT NULL,
    "Non_Filipino_Id" INTEGER,
    "Church" TEXT,
    "Tax_Id" TEXT NOT NULL,
    "Sss_No" TEXT NOT NULL,
    "Philhealth_No" TEXT,
    "Pagibig_No" TEXT,
    "Civil_Status" TEXT NOT NULL,
    "Spouse_Id" TEXT,
    "Academic_Id" INTEGER,
    "Criminal_Record" TEXT,
    "Regular" INTEGER NOT NULL, -- BOOLEAN is INTEGER (1 or 0)
    "Benefit_Id" INTEGER,
    "Salary_Id" REAL, -- MONEY type replaced with REAL
    "Contact_No" TEXT NOT NULL,
    "Archived" INTEGER NOT NULL, -- BOOLEAN is INTEGER (1 or 0)
    PRIMARY KEY ("Employee_Id")
    FOREIGN KEY ("Non_Filipino_Id") REFERENCES "Non_Filipino" ("Non_Filipino_Id") ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY ("Spouse_Id") REFERENCES "Spouse" ("Spouse_Id") ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY ("Academic_Id") REFERENCES "Academic_Record" ("Academic_Id") ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY ("Benefit_Id") REFERENCES "Benefit" ("Benefit_Id") ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY ("Salary_Id") REFERENCES "Salary" ("Salary_Id") ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY ("Position_Id") REFERENCES "Position" ("Position_Id") ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "Non_Filipino"
(
    "Non_Filipino_Id" INTEGER NOT NULL,
    "Passport_No" TEXT NOT NULL,
    "Acr_No" TEXT NOT NULL,
    "Date_Of_Issue" TEXT NOT NULL, -- Use TEXT for dates
    "Place_Of_Issue" TEXT NOT NULL, -- Use TEXT for dates
    PRIMARY KEY ("Non_Filipino_Id")
);

CREATE TABLE IF NOT EXISTS "Organization"
(
    "Organization_Id" INTEGER NOT NULL,
    "Name" TEXT NOT NULL,
    PRIMARY KEY ("Organization_Id")
);

CREATE TABLE IF NOT EXISTS "User"
(
    "User_Id" TEXT NOT NULL,
    "Password" TEXT NOT NULL,
    PRIMARY KEY ("User_Id"),
    FOREIGN KEY ("User_Id") REFERENCES "Employee" ("Employee_Id") ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Employee_Organization"
(
    "Employee_Employee_Id" TEXT NOT NULL,
    "Organization_Organization_Id" INTEGER NOT NULL,
    FOREIGN KEY ("Employee_Employee_Id") REFERENCES "Employee" ("Employee_Id") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ("Organization_Organization_Id") REFERENCES "Organizations" ("Organization_Id") ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Child"
(
    "Child_Id" TEXT NOT NULL,
    "Last_Name" TEXT NOT NULL,
    "First_Name" TEXT NOT NULL,
    "Middle_Name" TEXT,
    "Date_Of_Birth" TEXT NOT NULL, -- Use TEXT for dates
    PRIMARY KEY ("Child_Id")
);

CREATE TABLE IF NOT EXISTS "Employee_Child"
(
    "Employee_Employee_Id" TEXT NOT NULL,
    "Child_Child_Id" TEXT NOT NULL,
    FOREIGN KEY ("Employee_Employee_Id") REFERENCES "Employee" ("Employee_Id") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ("Child_Child_Id") REFERENCES "Child" ("Child_Id") ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "Spouse_Info"
(
    "Spouse_Info_Id" INTEGER NOT NULL,
    "Date_Of_Marriage" TEXT NOT NULL, -- Use TEXT for dates
    "Place_Of_Marriage" TEXT NOT NULL,
    PRIMARY KEY ("Spouse_Info_Id")
);

CREATE TABLE IF NOT EXISTS "Parent"
(
    "Parent_Id" TEXT NOT NULL,
    "Last_Name" TEXT NOT NULL,
    "First_Name" TEXT NOT NULL,
    "Middle_Name" TEXT,
    "Occupation" TEXT,
    "Address" TEXT,
    PRIMARY KEY ("Parent_Id")
);

CREATE TABLE IF NOT EXISTS "Employee_Parent"
(
    "Employee_Employee_Id" TEXT NOT NULL,
    "Parent_Parent_Id" TEXT NOT NULL,
    FOREIGN KEY ("Employee_Employee_Id") REFERENCES "Employee" ("Employee_Id") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ("Parent_Parent_Id") REFERENCES "Parent" ("Parent_Id") ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "Sibling"
(
    "Sibling_Id" TEXT NOT NULL,
    "Last_Name" TEXT NOT NULL,
    "First_Name" TEXT NOT NULL,
    "Middle_Name" TEXT,
    "Occupation" TEXT,
    "Address" TEXT,
    PRIMARY KEY ("Sibling_Id")
);

CREATE TABLE IF NOT EXISTS "Employee_Sibling"
(
    "Employee_Employee_Id" TEXT NOT NULL,
    "Sibling_Sibling_Id" TEXT NOT NULL,
    FOREIGN KEY ("Employee_Employee_Id") REFERENCES "Employee" ("Employee_Id") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ("Sibling_Sibling_Id") REFERENCES "Sibling" ("Sibling_Id") ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE IF NOT EXISTS "Spouse"
(
    "Spouse_Id" TEXT NOT NULL,
    "Last_Name" TEXT NOT NULL,
    "First_Name" TEXT NOT NULL,
    "Middle_Name" TEXT,
    "Spouse_Info_Id" INTEGER NOT NULL,
    PRIMARY KEY ("Spouse_Id"),
    FOREIGN KEY ("Spouse_Info_Id") REFERENCES "Spouse_Info" ("Spouse_Info_Id") ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "Benefit"
(
    "Benefit_Id" INTEGER NOT NULL,
    "Education" REAL NOT NULL, -- Use REAL instead of numeric types
    "Medical" REAL NOT NULL,
    PRIMARY KEY ("Benefit_Id")
);

CREATE TABLE IF NOT EXISTS "Attendance"
(
    "Attendance_Id" INTEGER NOT NULL,
    "Employee_Id" TEXT NOT NULL,
    "Date" TEXT NOT NULL, -- Use TEXT for dates
    "Time_In" TEXT, -- Use TEXT for times
    "Time_Out" TEXT, -- Use TEXT for times
    "Remarks" TEXT,
    PRIMARY KEY ("Attendance_Id")
    FOREIGN KEY ("Employee_Id") REFERENCES "Employee" ("Employee") ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Salary"
(
    "Salary_Id" INTEGER NOT NULL,
    "Monthly_Salary" REAL NOT NULL, -- MONEY type replaced with REAL
    "Overtime_Salary" REAL,
    "Total_Salary" REAL NOT NULL,
    PRIMARY KEY ("Salary_Id")
);

CREATE TABLE IF NOT EXISTS "Academic_Record"
(
    "Academic_Id" INTEGER NOT NULL,
    "Elementary_Id" INTEGER,
    "Elementary_Fin" TEXT, -- Use TEXT for dates
    "HighSchool_Id" INTEGER,
    "HighSchool_Fin" TEXT, -- Use TEXT for dates
    "SeniorHigh_Id" INTEGER,
    "SeniorHigh_Diploma" TEXT,
    "SeniorHigh_Fin" TEXT, -- Use TEXT for dates
    "College_Id" INTEGER,
    "College_Diploma" TEXT,
    "College_Fin" TEXT, -- Use TEXT for dates
    "GradSchool_Id" INTEGER,
    "GradSchool_Diploma" TEXT,
    "GradSchool_Fin" TEXT, -- Use TEXT for dates
    PRIMARY KEY ("Academic_Id"),
    FOREIGN KEY ("HighSchool_Id") REFERENCES "School" ("School_Id") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("Elementary_Id") REFERENCES "School" ("School_Id") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("SeniorHigh_Id") REFERENCES "School" ("School_Id") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("College_Id") REFERENCES "School" ("School_Id") ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY ("GradSchool_Id") REFERENCES "School" ("School_Id") ON UPDATE NO ACTION ON DELETE NO ACTION

);

CREATE TABLE IF NOT EXISTS "School"
(
    "School_Id" INTEGER NOT NULL,
    "Name" TEXT NOT NULL,
    "Address" TEXT NOT NULL,
    PRIMARY KEY ("School_Id")
);

CREATE TABLE IF NOT EXISTS "Publication"
(
    "Publication_Id" INTEGER NOT NULL,
    "Name" TEXT NOT NULL,
    "Link" TEXT,
    PRIMARY KEY ("Publication_Id")
);

CREATE TABLE IF NOT EXISTS "Academic_Record_Publication"
(
    "Academic_Record_Academic_Record_Id" INTEGER NOT NULL,
    "Publication_Publication_Id" INTEGER NOT NULL,
    FOREIGN KEY ("Academic_Record_Academic_Record_Id") REFERENCES "Academic_Record" ("Academic_Record_Id") ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ("Publication_Publication_Id") REFERENCES "Publication" ("Publication_Id") ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "Distinction"
(
    "Distinction_Id" INTEGER NOT NULL,
    "Academic_Id" INTEGER NOT NULL,
    "Year" TEXT NOT NULL, -- Use TEXT for dates
    "Semester" INTEGER,
    FOREIGN KEY ("Academic_Id") REFERENCES "Academic_Record" ("Academic_Record_Id") ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Government_Exam"
(
    "Governmant_Exam_Id" INTEGER NOT NULL,
    "Academic_Id" INTEGER NOT NULL,
    "Title" TEXT NOT NULL,
    "Date" TEXT NOT NULL, -- Use TEXT for dates
    "Score_Achieved" INTEGER NOT NULL,
    "Score_Max" INTEGER NOT NULL,
    PRIMARY KEY ("Governmant_Exam_Id"),
    FOREIGN KEY ("Academic_Id") REFERENCES "Academic_Record" ("Academic_Record_Id") ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "Position"
(
    "Position_Id" INTEGER NOT NULL,
    "Name" TEXT NOT NULL,
    "Department" TEXT NOT NULL,
    PRIMARY KEY ("Position_Id")
);

-- UPDATE ERD !!
