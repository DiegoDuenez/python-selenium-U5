<?php


include 'Controllers/UserController.php';


$UserController = new UserController();


// echo $UserController->create($_POST);
if($UserController->create($_POST)){
    echo "<script>alert('CREADO')</script>";
}
else{
    echo "<script>alert('NO CREADO')</script>";

}