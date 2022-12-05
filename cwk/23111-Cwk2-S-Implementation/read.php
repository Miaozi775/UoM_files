<!DOCTYPE html>

<html>

<head>
	<meta charset="utf-8">
	<title>cwk2</title>
</head>

<body>
<h1>Company employees</h1>

<?php

function getFileData($filename)
{
    if (!file_exists($filename))
    {
        echo("File does not exist");
        return;
 }

    $file = fopen($filename, "r");

    while (($data = fgetcsv($file)) !== FALSE)
    {
        $data[0] = iconv('gbk', 'utf-8', $data[0]);

        $records[] = $data;

        print_r($data);

    }

    fclose($file);



}

getFileData("employees.csv");


?>

</body>

</html>








