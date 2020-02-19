<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>STAT - SEO Tracking Tool</title>
    <style>
      #stat-body {
        background-image: url(assets/img/stat/image1.jpg);
        background-repeat: no-repeat;
        color: rgba(22, 60, 233, 1);
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;

      }
      /* Table Style Part .. */
      div {
        position: relative;
      }
      td, th {
        border: 1px solid none;
        width: 250px;
        height: 70px;
        text-align: center;
        padding: 5px;
      }
      td:hover {
        background-color: rgba(235, 162, 133, 0.745);
        border-radius: 15px;
        margin: 5px;
      }
      table {
        border-collapse: collapse;
        position: absolute;
        left: 15%;
        right: auto;
        margin-top: 50px;
        box-shadow: 10px 10px 30px black;

      }
      thead {
        background-color: rgba(235, 162, 133, 0.745);
      }
      tbody {
        background-color: rgba(255, 166, 0, 0.158);
        color: black;
        font-weight: bold;
      }
    </style>
</head>
<body id="stat-body">  
  <!-- Start: PHP Code -->
  <?php 
    // session_start();
    // if(isset($_SESSION['url'])){
    //   echo '<br />Welcome!,<br /> Your URL Is: ' . $_SESSION['url'];
    // }else{
    //   // Alert Message In Case The Database Hasn't Record About This URL ..
    //   echo '<script type="text/javascript">alert("SORRY!, This URL Is Not Found.");</script>';
    //   header('location: adding-url.php');
    //   exit();
    // }
    // echo '<br/><br/><b style="color: red;">Welcome To The Statistics Page.</b>';
    /* ********************* The Code Above Just Was For Testing ********************* */ 
    echo "<div><table>";
 echo "<thead>
 <tr>
   <th>WEBSITE URL</th>
   <th>KEYWORDS</th>
   <th>KEYWORDS POSITION</th>
   <th>VERIFICATION DATE</th>
 </tr>
 </thead><tbody>";

class TableRows extends RecursiveIteratorIterator {
    function __construct($it) {
        parent::__construct($it, self::LEAVES_ONLY);
    }

    function current() {
        return "<td>" . parent::current(). "</td>";
    }

    function beginChildren() {
        echo "<tr>";
    }

    function endChildren() {
        echo "</tr>" . "\n";
    }
}
    include 'connect.php';
    $stmt = $dbConnect->prepare('SELECT `url`, `terms` FROM `site` LEFT JOIN `keywords` ON ? = ?');
    $stmt->execute(array(`site`.`terms-ID` , `keywords`.`terms-ID`));
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
    foreach(new TableRows(new RecursiveArrayIterator($fetch = $stmt->fetchAll())) as $k=>$v) {
      if(!$v){
        echo '';
      }else{
        echo $v;
      }
    }
    //include_once 'pos-update.py';
    //$command = "python pos-update.py";
    $run = exec("python pos-update.py");

    $dbConnect = null;
    echo '</tbody>
    </table>
  </div>';
  ?>
  <!-- End: PHP Code -->
</body>
</html>
