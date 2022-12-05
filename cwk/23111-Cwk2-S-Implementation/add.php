<!DOCTYPE html>

<html>

<head>
	<meta charset="utf-8">
	<title>cwk2</title>
</head>

<body>
<h1>Company employees</h1>

<p>Click on the link below to add a new employee</p>
<a href="add.php">Add new employee</a>

//add a new employee
<?php
require_once("creaet_db.php");

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








