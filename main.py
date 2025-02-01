<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝚃𝙾𝙺𝙴𝙽 𝙲𝙷𝙴𝙲𝙺𝙴𝚁</title>
    <style>
        /* CSS for styling elements */
        .error {
            color: red;
            font-weight: italic;
        }
        h1{
            text-align: center;
            border: double 2px white
            font-family: cursive;
            font-size: 25px;
        }
        .btn, input {
            height: 33px;
            width: 100%;
            margin-top: 20px;
            background-color: blue;
            border: double 2px white;
            color: white;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            box-sizing: border-box;
        }
        input {
            background: non;
            outline: green;
            border: double 2px white;
            color: non;
            padding: 10px;
            background-color: black;
        }
        h2{
            text-align: center;
            font-size: 15px;
            border-redius: 20px;
            color: white;
             background-color: black;
            border: double 2px white ;
        }
        label{
            color: white;
        }
        body{
            background-image: url('https://i.ibb.co/kVzW4bHc/IMG-20250126-WA0161.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center; /* Center the background image */
            background-attachment: fixed; /* Keep the background fixed on scroll */
            color: white;
            height: 100vh;
            margin: 0;
           display: flex;
      
            align-items: center;
            justify-content: center;
        }
        .container {
            max-width: 350px;
            width: 100%;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 15px white;
            border: double 2px white;
            resize: none;
            background: rgba(0, 0, 0, 0.5);
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: non;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Facebook Token Checker</h1>
    <form method="post">
        <input type="text" name="access_token" placeholder="𝙴𝙽𝚃𝙴𝚁 𝚃𝙾𝙺𝙴𝙽" required>
        <button class="btn" type="submit">𝙲𝙷𝙴𝙲𝙺 𝚃𝙾𝙺𝙴𝙽</button>
    </form>
    
    {% if error_message %}
        <p class="error">{{ error_message }}</p>
    {% elif profile_name %}
        <p>Your Profile Name: {{ profile_name }}</p>
    {% endif %}
    
    <footer>
        <h2>7H3 L3G3ND B0II S9LM9N H3R3</h2>
    </footer>
</div>

</body>
</html>
