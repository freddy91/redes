<?php
   if(isset($_FILES['image'])){
      
    $nombre = $_FILES['image']['name'];
     $tmp =$_FILES['image']['tmp_name'];
      
	 move_uploaded_file($tmp,"img/".$nombre);
        
   	$output = shell_exec("D:/python/python.exe predic.py $nombre 2<&1");
	echo $output;
     
   }
?>
