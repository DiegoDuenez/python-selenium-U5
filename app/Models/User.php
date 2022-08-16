<?php

include '../database/database.php';

class User extends Database{

    protected $table = "users";
    
    function create($array){

        return $this->ExecuteQuery($array);

    }

}