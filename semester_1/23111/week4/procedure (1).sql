DROP TABLE IF EXISTS People;

CREATE TABLE People (
 name varchar(20),
 age INT);

INSERT INTO People 
    VALUES ('Jim',23), ('Pam', 19);

-- now define procedure listPeople()
DELIMITER /
CREATE PROCEDURE listPeople()
BEGIN
   SELECT * FROM People ORDER BY age;
END /
DELIMITER ;




