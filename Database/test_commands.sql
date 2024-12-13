select * from Spouse_Info where Spouse_Info_Id = (select Spouse_Info_Id from Spouse where Spouse_Id = (select Spouse_Id from Employee where Employee_Id = '20241212-009'));


select Father_Last_Name, Father_First_Name, Father_Middle_Name, Father_Occupation, Father_Address, Mother_Last_Name, Mother_First_Name, Mother_Middle_Name, Mother_Occupation, Mother_Address
from Parent where Parent_Id = (select Parent_Parent_Id from Employee_Parent where Employee_Employee_Id = '20241120-001');


select * from Employee where Academic_Id = 16;


select * from Academic_Record where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241212-027');

select * from Academic_Record where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241212-015');


select * from Publication where Publication_Id = (select Publication_Publication_Id from Academic_Record_Publication 
    where Academic_Record_Academic_Record_Id = (select Academic_Id from Employee where Employee_Id = '20241212-027'));
    

select Name from position where position_id = (select position_id from Employee where Employee_Id = '20241212-027');

Update Position Set Name = 'professor' where position_id = (select position_id from Employee where Employee_Id = '20241212-027');

select * from position;


select * from Parent where Parent_Id = (select Parent_Parent_Id from Employee_Parent where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id = '20241212-027'));

Update Parent Set Father_Last_Name = 'F', Father_First_Name = 'F', Father_Middle_Name = 'F', Father_Occupation = 'F', Father_Address = 'F',
                Mother_Last_Name = 'M', Mother_First_Name = 'M', Mother_Middle_Name = 'M', Mother_Occupation = 'M', Mother_Address = 'M'
                where Parent_Id = (select Parent_Parent_Id from Employee_Parent where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id = '20241212-027'));


select * from Spouse where Spouse_Id = (select spouse_id from Employee where Employee_id = '20241212-027');

Update Spouse Set Last_Name = 'S', First_Name = 'S', Middle_Name = 'S' where Spouse_Id = (select spouse_id from Employee where Employee_id = '20241212-027');


select * from Child where Child_Id = (select Child_Child_Id from Employee_Child where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id ='20241212-027') );

Update Child Set Last_Name = 'Ch', First_Name = 'Ch', Middle_Name = 'Ch', Date_of_Birth='01/01/1900' 
where Child_Id = (select Child_Child_Id from Employee_Child where Employee_Employee_Id = (select Employee_Id from Employee where Employee_Id ='20241212-027') );



select * from Sibling where Sibling_Id = (select Sibling_Sibling_Id from Employee_Sibling where Employee_Employee_Id = '20241212-027');


Update Sibling Set Last_Name = 'Sib', First_Name = 'Sib', Middle_Name = 'Sib', Occupation = 'Sib', Address = 'Sib'
where Sibling_Id = (select Sibling_Sibling_Id from Employee_Sibling where Employee_Employee_Id = '20241212-027');


select * from Spouse_Info where Spouse_Info_Id = (select Spouse_Info_Id from Spouse where Spouse_id = (select spouse_id from Employee where Employee_Id = '20241212-027') );

Update Spouse_Info
Set Date_Of_Marriage = 'dom', Place_Of_Marriage = 'pom' where Spouse_Info_Id = (select Spouse_Info_Id from Spouse where Spouse_id = (select spouse_id from Employee where Employee_Id = '20241212-027') );



select * from Government_Exam;

SELECT count(*) from Government_Exam;

SELECT 1 FROM Government_Exam WHERE Government_Exam_Id = 11;



-- government exam and publication
select * from Government_Exam where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-005');


select * from Publication where Publication_Id = (select Publication_Publication_Id from Academic_Record_Publication where Academic_Record_Academic_Record_Id = (select Academic_Id from Employee where Employee_Id = '20241213-005') );


select * from Academic_Record where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');


select * from Government_Exam where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');


select Name,Link from Publication where Publication_Id = (select Publication_Publication_Id from Academic_Record_Publication
 where Academic_Record_Academic_Record_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006') );



select Elementary_Name, Elementary_Address, Elementary_Fin, HighSchool_Name, HighSchool_Address, HighSchool_Fin, College_Name, College_Address, College_Fin
 from Academic_Record where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');



select Title,Score_Achieved,Date from Government_Exam where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');


select * from Distinction where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');



select Last_Name,First_Name, Middle_Name from Sibling where Sibling_Id = (select Sibling_Sibling_Id from Employee_Sibling where Employee_Employee_Id = '20241213-006');

select Name,Link from Publication where Publication_Id = (select Publication_Publication_Id from Academic_Record_Publication
 where Academic_Record_Academic_Record_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006') );
 
select Elementary_Name, Elementary_Address, Elementary_Fin, HighSchool_Name, HighSchool_Address, HighSchool_Fin, College_Name, College_Address, College_Fin
 from Academic_Record where Academic_Id = (select Academic_Id from Employee where Employee_Id = '20241213-006');
 
select * from Non_Filipino;

select Passport_No, Acr_No, Date_Of_Issue from Non_Filipino where Employee_Id = '20241213-006';



--updating


