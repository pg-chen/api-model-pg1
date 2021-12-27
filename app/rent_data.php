<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<h2>確認頁面</h2>
	<?php
		$District = $_POST["District"];
		print "行政區: " . $District . "<br/>";
		$Object = $_POST['Object'];
		print "物件類別: " . $Object . "<br/>";
		$Structure = $_POST["Structure"];
		print "建築類別: " . $Structure . "<br/>";
		$Floor = $_POST["Floor"];
		print "所在樓層: " . $Floor . "<br/>";
		$Building_Height = $_POST["Building_Height"];
		print "總樓高: " . $Building_Height . "<br/>";
		$Square = $_POST["Square"];
		print "坪數: " . $Square . "<br/>";
		$Funitures = $_POST["checkbox"];
		$Funiture = count($Funitures);
		print "提供家具: " . $Funiture . "<br/>";
		$lat = $_POST['lat'];
		$lnt = $_POST['lnt'];
		print "經度: " . $lnt . "<br/>";
		print "緯度: " . $lat . "<br/>";
	?>
    <form action="test.php" method="POST">
    <button type="submit" name="write">預測租金</button>

    <input type="hidden" name="District" value="<?php echo $District?>">
    <input type="hidden" name="Object" value="<?php echo $Object?>">
    <input type="hidden" name="Structure" value="<?php echo $Structure?>">
    <input type="hidden" name="Floor" value="<?php echo $Floor?>">
    <input type="hidden" name="Building_Height" value="<?php echo $Building_Height?>">
    <input type="hidden" name="Square" value="<?php echo $Square?>">
    <input type="hidden" name="Funiture" value="<?php echo $Funiture?>">
    <input type="hidden" name="lat" value="<?php echo $lat?>">
    <input type="hidden" name="lnt" value="<?php echo $lnt?>">
</form>
</body>
</html>