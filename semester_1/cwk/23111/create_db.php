
//CREATE DATABASE EMPLOYEES;
<?php
$servername = "localhost";
$username = "root";
$password = "wlx151332";

//create connection
$conn = new mysqli($servername, $username, $password);

//check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//create database
$sql = "CREATE DATABASE EMPLOYEES";
if ($conn -> query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}

$conn->close();
?>



//CREATE TABLE EMPLOYEES_INFO
<?php
$servername = "localhost";
$username = "root";
$password = "wlx151332";
$dbname = "EMPLOYEES";

//create connection
$conn = new mysqli($servername, $username, $password, $dbname);

//check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//create table use mysql
$sql = "CREATE TABLE EMPLOYEES_INFO (
emp_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
address VARCHAR(50) NOT NULL,
salary VARCHAR(40) NOT NULL,
dob DATE NOT NULL,
nin VARCHAR(30) NOT NULL,
department VARCHAR(40) NOT NULL,
emergency_name VARCHAR(40) NOT NULL,
emergency_relationship VARCHAR(40) NOT NULL,
emergency_phone INT(6) NOT NULL
)";

if ($conn -> query($sql) === TRUE) {
    echo "Table EMPLOYEES created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

//load data from csv file
$sql = "LOAD DATA LOCAL INFILE 'employees.csv' INTO TABLE EMPLOYEES_INFO FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\r

' IGNORE 1 LINES";

if ($conn -> query($sql) === TRUE) {
    echo "Data loaded successfully";
} else {
    echo "Error loading data: " . $conn->error;
}

$conn->close();
?>

