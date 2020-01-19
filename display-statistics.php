<!-- Start: PHP Code -->
<?php 
  session_start();
  if(isset($_SESSION['url'])){
    echo '<br />Welcome!,<br /> Your URL Is: ' . $_SESSION['url'];
  }else{
    // Alert Message In Case The Database Hasn't Record About This URL ..
    echo '<script type="text/javascript">alert("SORRY!, This URL Is Not Found.");</script>';
    header('location: adding-url.php');
    exit();
  }
?>
<!-- End: PHP Code -->