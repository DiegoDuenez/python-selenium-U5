<?php

include 'Models/User.php';


class UserController{


    public function create($array)
    {

        $user = new User();

        return $user->create($array);

    }

}
