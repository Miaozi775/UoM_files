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

//CREATE TABLE EMPLOYEES 
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
$sql = "CREATE TABLE EMPLOYEES (
emp_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
emp_name VARCHAR(30) NOT NULL,
emp_address VARCHAR(50) NOT NULL,
salary INT(6) NOT NULL,
dob DATE NOT NULL,
nin VARCHAR(9) NOT NULL,
department VARCHAR(30) NOT NULL,
emergency_name VARCHAR(30) NOT NULL,
emergency_relationship VARCHAR(11) NOT NULL,
emergency_phone VARCHAR(11) NOT NULL
)";

if ($conn -> query($sql) === TRUE) {
    echo "Table EMPLOYEES created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>



<!DOCTYPE html>

<html>

<head>
	<meta charset="utf-8">
	<title>cwk2</title>
</head>

<body>

<h1>Company employees</h1>

//add a new employee
<?php
$servername = "localhost";
$username = "root";
$password = "wlx151332"; 
$dbname = "EMPLOYEES";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//insert a new employee
$sql = "INSERT INTO EMPLOYEE (emp_id, emp_name, emp_address, salary, dob, nin, department, emergency_name, emergency_relationship, emergency_phone)
VALUES ('55-3623151', 'Malissia Osgardby', '29416 Grover Alley', '£17424.03', '26/12/1989', 'it152291r', 'Driver', 'Marcie Prattington', 'Mother', '07297 230 400')";

if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

$conn->close();
?>

</body>
</html>


