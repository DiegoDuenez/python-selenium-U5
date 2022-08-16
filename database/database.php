<?php
class Database{
	private $dbh;
    protected $table = "";
    protected $primaryKey = "id";

	function __construct(){

		$dsn = "mysql:host=localhost;dbname=selenium_toro;charset=utf8mb4";
		$options = [
			PDO::ATTR_EMULATE_PREPARES   => false,
			PDO::ATTR_EMULATE_PREPARES => true,
			PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
			PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
		];

		$this->dbh = new PDO($dsn, 'root',  '', $options);
		
	}


	function Select($q){
		try{
			$sth = $this->dbh->prepare($q);
			$sth->execute();
			$sth->setFetchMode(PDO::FETCH_ASSOC);
			$result = $sth->fetchAll();
			//$this->dbh = null;
			$result = json_encode($result);
			$obj = json_decode($result, true);
			return $obj;

		}
		catch(PDOException $e){
			error_log('PDOException - ' . $e->getMessage(), 0);
			http_response_code(500);
			die($e->getMessage());
		}
	}


	function ExecuteQuery($array){

        $cols = implode(", ", array_keys($array));
        $vals =  "'" .implode("', '",array_values($array)) . "'";

        $insert = "INSERT INTO $this->table ($cols) VALUES ($vals)";

		try	{
			$sth = $this->dbh->prepare($insert);
			$sth->execute([]);
			return $sth->rowCount() > 0;
		}
		catch(PDOException $e){
			
			error_log('PDOException - ' . $e->getMessage(), 0);
			http_response_code(500);
			if ($e->errorInfo[1] == 1062) {
				echo json_encode(["status" => "error", "error" => $e->getMessage(), "type"=>"duplicate"]);
				die();
			} else {
				throw $e;
			}
			return false;
		
		}
	}
}
?>
