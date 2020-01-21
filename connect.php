<?php
$dsn = 'mysql:host=localhost;dbname=seo-tracking-tool';
$user = 'root';
$pass = '';

try{
  $dbConnect = new PDO($dsn, $user, $pass);
  $dbConnect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  // echo 'You are Connected ! Welcome to Database.';
}
catch(PDOException $e){
  echo 'Failed To Connect !' . $e->getMessage();
}