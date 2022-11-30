<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Lab: Views, Triggers and Web Programming</title>
</head>
<body>
	<h1>Task 16</h1>
	<?php
		require_once("dbconfig.php");
		$pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);

		$sql = "SELECT * FROM empOffices 
				WHERE addressLine1 = :address;";
		
		$records = $pdo->prepare($sql);
		$records->execute([':address' => '43 Rue Jouffroy D\'abbans']);

		echo("<table>");
		while($row = $records->fetch())
		{
			echo("<tr>");
			echo("<td>" . $row['employeeNumber'] . "</td>");
			echo("<td>" . $row['firstname']      . "</td>");
			echo("<td>" . $row['lastname']       . "</td>");
			echo("<td>" . $row['addressLine1']   . "</td>");
			echo("<td>" . $row['addressLine2']   . "</td>");
			echo("</tr>");
		}
		echo("</table>");	
	?>
</body>
</html>




<?php
// just to allow a print line for any input given.  Used for debugging. 
function println($input, $param = "")
{
	// return; // uncomment when live, comment when testing. 
	if (is_array($input))
	{
		if ($param == "")
			echo("<pre>" . print_r($input, true) . "</pre>");
		else
		{
			foreach ($input as $key => $value) 
			{
				// echo($key . ":" . $value . "<br>");

				if (strpos($key, $param) !== false)
				{
					echo("<pre>" . print_r($value, true) . "</pre>");
				}

				if (is_array($value))
				{
					println($value, $param);	
				}

			}
		}
	}
	elseif (is_object($input)) 
	{
		echo("<pre>" . print_r($input, true) . "</pre>");
	}
	else
	{
		print ("<br>" . $input . "</br>");
	}	
}

?>