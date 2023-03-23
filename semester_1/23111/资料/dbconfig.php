<?php

	$host     = "localhost";
	$dbname   = "classicmodels";
	$username = "root";
	$password = "";

	try 
	{
		$conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
		echo ("Connected to $dbname");
	}
	catch (PDOException $pe)
	{
		exit("Could not connect to database $dbname: " . $pe->getMessage());
	}

?>