<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Jetbrains License ID Service</title>
</head>
<body>
<h3>Jetbrains License ID Service</h3>
<input type="email" id="email" placeholder="E-mail"/>
<input type="password" id="password" placeholder="Password" />
<button id="getLicenseId" onclick="getLicenseId()">Get License ID</button>
<br><br>
<div id="result"></div>

<script src="https://code.jquery.com/jquery-3.7.1.js"></script>
<script>
    function getLicenseId(){
        let email = jQuery('#email').val();
        let password = jQuery('#password').val();

        $.ajax({
            url: '/jetbrains-service.php',
            method: 'POST',
            data: {email,password},
            beforeSend: function(){
                $('#result').text('Loading...');
            },
            success: function(response){
                $('#result').text('LICENSE ID: ' + response);
            }
        })
    }
</script>
</body>
</html>