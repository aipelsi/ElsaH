<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Content Page</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            background: url('neuron.jpg') no-repeat center center fixed;
            background-size: cover;
            overflow-x: hidden; /* Prevents horizontal scroll */
        }

        .container {
            position: relative; /* Changed from absolute for better responsiveness */
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: #333;
            margin: auto; /* Centers the container on smaller screens */
            text-align: center;
            width: 80%;
            max-width: 800px; /* Keeps container width under control on larger screens */
            transform: translateY(-50%); /* Vertically centers the container */
            top: 50%; /* Works with transform to vertically center */
        }

        .profile-photo {
            border-radius: 50%;
            width: 50%; /* Adjust based on preference */
            max-width: 200px; /* Ensures the image does not become too large */
            height: auto; /* Maintains aspect ratio */
            margin: 20px auto; /* Centers the image and adds spacing */
            display: block; /* Treats the image as a block for centering purposes */
        }

        h1, h2 {
            color: #007bff;
            display: block; /* Each heading takes its own line */
            margin: 0 auto; /* Centers headings */
            padding: 5px; /* Adds some padding for spacing */
        }

        p, a, .tab {
            text-align: justify;
            margin-top: 10px;
        }

        a, .tab {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
            width: auto; /* Allows the button to adjust based on text length */
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .profile-photo {
                width: 70%; /* Makes the photo larger on smaller screens */
            }

            h1, h2, p, .tab {
                font-size: 90%; /* Reduces font size for small devices */
            }
        }
    </style>
</head>
<body>

<div class="container">
    <img src="pic.png" alt="Profile Photo" class="profile-photo">
    <h1>Elsa Hagos</h1>
    <p>I am studying Information Systems as a graduate student at the University of Washington Foster School of Business. My passion lies in exploring AIML infrastructures and creating meaningful data visualizations. I thrive on diving into data, predicting social behaviors, evaluating health metrics, and tackling classification challenges.</p>

    <p>Check out my website’s Visualization tab to experience the power of visual storytelling with data. The Projects tab gives you a sneak peek into the exciting endeavors I’ve been a part of, and the Blogs tab offers insights and reflections.</p>

    <p>Let’s embark on a journey through the fascinating intersection of information, tech, and data. Excited to have you along!</p>

    <!-- Tabs for Projects, Data Visualization, and Blogs -->
    <div class="tabs-container">
        <a href="projects.html" class="tab">Projects</a>
        <a href="data-visualization.html" class="tab">Data Visualization</a>
        <a href="blog.html" class="tab">Blog</a>
    </div>
</div>

</body>
</html>

