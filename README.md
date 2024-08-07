<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            flex-direction: column;
            font-family: Arial, sans-serif;
            font-size: 16px; /* Increased font size */
            background: url('neuron.jpg') no-repeat center center fixed;
            background-size: cover;
        }

        .container {
            padding: 90px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: #333;
            margin: 20px auto; /* Centering the container */
            text-align: left;
            width: 90%;
            max-width: 1000px; /* Adjusted max width for larger screens */
            flex: 1; /* Allow the container to grow and take up available space */
            display: flex;
            flex-direction: column;
            justify-content: center; /* Center content vertically */
        }

        .profile-photo {
            border-radius: 50%;
            width: 200px; /* Maintains a fixed width */
            height: 200px;
            object-fit: cover;
            display: block; /* For centering */
            margin: 20px auto; /* Adds margin on top and bottom, and auto centers horizontally */
        }

        h1, h2, p, a, .tab {
            margin: 10px 0; /* Adds margin to top and bottom for spacing */
        }

        a, .tab {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
        }

        footer {
            text-align: center;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.9);
        }

        /* Styles for larger screens */
        @media (min-width: 1024px) {
            .container {
                width: 80%; /* Increased width for desktop */
                max-width: 1200px; /* Adjusted for even larger screens */
            }

            .profile-photo, h1, h2, p, a, .tab {
                font-size: 100%;
            }
        }

        /* Styles for smaller screens */
        @media (max-width: 1023px) {
            body, html {
                overflow-x: hidden; /* Prevents horizontal scrolling on smaller screens */
            }

            .container {
                width: 90%; /* More width for smaller screens */
            }

            .profile-photo {
                width: 150px; /* Smaller photo on smaller screens */
                height: 150px;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <img src="pic.png" alt="Profile Photo" class="profile-photo">
    <p>I am studying Information Systems as a graduate student at the University of Washington Foster School of Business. My passion lies in exploring AIML infrastructures and creating meaningful data visualizations. I thrive on diving into data, predicting social behaviors, evaluating health metrics, and tackling classification challenges.</p>

    <p>Check out my website’s Visualization tab to experience the power of visual storytelling with data. The Projects tab gives you a sneak peek into the exciting endeavors I’ve been a part of, and the Blogs tab offers insights and reflections.</p>

    <p>Let’s embark on a journey through the fascinating intersection of information, tech, and data. Excited to have you along!</p>

    <div class="tabs-container">
        <a href="Protest.html" class="tab">Projects</a>
        <a href="data-visualization.html" class="tab">Data Visualization</a>
        <a href="blog.html" class="tab">Blog</a>
    </div>
</div>

<footer>
    <p>&copy; 2024 Elsa Hagos</p>
</footer>

</body>
</html>


