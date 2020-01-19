<!-- Start: PHP Code.. -->
<?php 
    // session_start();
    // if(isset($_SESSION['url'])){
    //     header('location: display-statistics.php');  // Redirect To display-statistics Page
    // }
    /* ********************* The Code Above Just Was For Testing ********************* */
?>
<!-- End: PHP Code.. -->
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,400i,700,700i,600,600i">
    <link rel="stylesheet" href="assets/fonts/ionicons.min.css">
    <link rel="stylesheet" href="assets/fonts/simple-line-icons.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.10.0/baguetteBox.min.css">
    <link rel="stylesheet" href="assets/css/Login-Form-Dark.css">
    <link rel="stylesheet" href="assets/css/smoothproducts.css">
</head>

<body>
    <!-- Start: PHP Code.. -->
        <?php
            include 'connect.php';

            /* Check If Data Coming From HTTP Post Request. */
            if($_SERVER['REQUEST_METHOD'] == 'POST'){
                $url = $_POST['url'];
                $keywords = $_POST['keywords'];
                
                //echo $url . '<br /><br />' . $keywords;

                /* Check If The URL Exist In The Database. */
                $stmt = $dbConnect->prepare("SELECT `url` FROM `adding` WHERE `url` = ?");
                $stmt->execute(array($url));
                $fetch = $stmt->rowCount();
                // echo '<br />' . $fetch;
                /* If fetch > 0 This Mean The Database Contain Record About This URL */
                
                    if($fetch > 0){
                        //     echo '<br />Welcome, Your URL is : ' . $url;
                        // }else{
                        //     echo '<br />Sorry! This URL Is Not Found. ';
                        // }
                        // $_SESSION['url'] = $url;  // Register Session Name
                        // header('location: display-statistics.php');  // Redirect To display-statistics Page
                        // exit();
                        echo "<script type='text/javascript'>alert('SORRY!, This URL Is Already Registered In The Database.');</script>";  // Alert Message In Case The given URL Is Already Registered In The Database.
                    }else{
                        $insert = $dbConnect->prepare("INSERT INTO `adding` (`url`,`keywords`) VALUES(?,?)");
                        $insert->execute(array($url,$keywords));
                                               
                        echo "<script type='text/javascript'>alert('Your URL Is Registered Successfully.');</script>";  // Successful Message In Case This URL Isn't Exist In The Database Already..
                        header('location: display-statistics.php');  // Redirect To display-statistics Page
                        exit();
                    }
            }
        ?>
    <!-- End: PHP Code -->
    <!-- Start: Login Form Dark -->
    <div class="login-dark">
        <form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="post">
            <h2 class="sr-only">Login Form</h2>
            <div class="illustration">
                <i class="icon ion-upload"></i>
            </div>
            <div class="form-group">
                <input class="form-control" type="url" id="placeholder-url" placeholder="https://www.website-name.com/" autofocus="" required="" autocomplete="on" inputmode="url" name="url">
            </div>
            <div class="form-group">
                <textarea class="form-control form-control-sm" placeholder="Keywords" rows="3" cols="3" name="keywords" autofocus="" autocomplete="on" required=""></textarea>
            </div>
            <div class="form-group">
                <button class="btn btn-primary btn-block pulse animated infinite" type="submit">Send</button>
            </div>
        </form>
    </div>
    <!-- End: Login Form Dark -->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.10.0/baguetteBox.min.js"></script>
    <script src="assets/js/smoothproducts.min.js"></script>
    <script src="assets/js/theme.js"></script>
    <script src="assets/js/bs-animation.js"></script>
</body>

</html>