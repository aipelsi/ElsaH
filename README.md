<!DOCTYPE html>
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
            background: url('neuron.jpg') no-repeat center center fixed;
            background-size: cover;
        }

        /* Main container styling */
        .container {
            padding: 50px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: #333;
            margin: 20px auto;
            width: 90%;
            max-width: 1000px;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Profile photo styling */
        .profile-photo {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            margin: 20px auto;
        }

        /* General text and tab styling */
        h1, h2, p, a, .tab {
            margin: 10px 0;
        }

        a, .tab {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
            transition: background-color 0.3s ease;
        }

        a:hover, .tab:hover {
            background-color: #0056b3;
        }

        footer {
            text-align: center;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.9);
            width: 100%;
        }

        /* Styles for larger screens */
        @media (min-width: 1024px) {
            .container {
                padding: 90px;
                width: 80%;
                max-width: 1200px;
            }

            .profile-photo {
                width: 200px;
                height: 200px;
            }
        }

        /* Styles for smaller screens */
        @media (max-width: 1024px) {
            .container {
                padding: 30px;
                width: 95%;
            }

            .profile-photo {
                width: 150px;
                height: 150px;
            }
        }

        @media (max-width: 600px) {
            /* Further adjust padding and content for mobile devices */
            .container {
                padding: 20px;
                margin: 10px auto;
            }

            .profile-photo {
                width: 120px;
                height: 120px;
            }

            a, .tab {
                padding: 8px 15px;
                font-size: 14px;
            }

            p {
                font-size: 14px;
                line-height: 1.5;
                margin: 10px 0;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <img src="pic.png" alt="Profile Photo" class="profile-photo">
    <p>I recently graduated with MS degree in Information Systems from the University of Washington Foster School of Business. My passion lies in exploring AIML infrastructures and creating meaningful data visualizations. I thrive on working with data, predicting social behaviors, evaluating health metrics, and solving classification challenges.</p>

    <p>Check out the Visualization tab on my website to experience the power of visual storytelling with data. The Projects tab offers a glimpse into the exciting work I've been involved in, while the Blogs tab shares insights and reflections.</p>

    <p>Join me as we explore the intersection of information, technology, and data. I’m excited to share my work and insights with you.</p>

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


