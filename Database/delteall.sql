PRAGMA foreign_keys = ON;

DELETE FROM "Employee_Organization";
DELETE FROM "Employee_Child";
DELETE FROM "Employee_Parent";
DELETE FROM "Employee_Sibling";
DELETE FROM "Academic_Record_Publication";
DELETE FROM "Distinction";
DELETE FROM "Government_Exam";


DELETE FROM "Attendance";
DELETE FROM "Spouse";
DELETE FROM "Benefit";
DELETE FROM "Salary";
DELETE FROM "Academic_Record";
DELETE FROM "Publication";
DELETE FROM "Position";
DELETE FROM "School";
DELETE FROM "Child";
DELETE FROM "Parent";
DELETE FROM "Sibling";
DELETE FROM "Spouse_Info";
DELETE FROM "Non_Filipino";
DELETE FROM "Employee";

-- Optionally, reset the primary key sequences if needed
-- DELETE FROM sqlite_sequence WHERE name='Employee';
-- DELETE FROM sqlite_sequence WHERE name='Non_Filipino';
-- DELETE FROM sqlite_sequence WHERE name='Organization';
-- DELETE FROM sqlite_sequence WHERE name='User';
-- DELETE FROM sqlite_sequence WHERE name='Child';
-- DELETE FROM sqlite_sequence WHERE name='Spouse_Info';
-- DELETE FROM sqlite_sequence WHERE name='Parent';
-- DELETE FROM sqlite_sequence WHERE name='Sibling';
-- DELETE FROM sqlite_sequence WHERE name='Spouse';
-- DELETE FROM sqlite_sequence WHERE name='Benefit';
-- DELETE FROM sqlite_sequence WHERE name='Attendance';
-- DELETE FROM sqlite_sequence WHERE name='Salary';
-- DELETE FROM sqlite_sequence WHERE name='Academic_Record';
-- DELETE FROM sqlite_sequence WHERE name='School';
-- DELETE FROM sqlite_sequence WHERE name='Publication';
-- DELETE FROM sqlite_sequence WHERE name='Position';
