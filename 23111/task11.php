<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Lab: Views, Triggers and Web Programming</title>
</head>
<body>
	<h1>Task 11</h1>
	<?php
		require_once("dbconfig.php");
		$pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);

		$sql = "UPDATE resolved 
		        SET    status = :status 
		        WHERE  customerName = :cName;";
		
		$records = $pdo->prepare($sql);
		$records->execute([':status' => 'Shipped',
						   ':cName'  => 'Toys4GrownUps.com']);
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