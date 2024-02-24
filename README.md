<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elsa Hagos Portfolio</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }
        .video-background {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%; 
            min-height: 100%;
            width: auto; 
            height: auto;
            z-index: -100;
        }
        .content {
            position: relative;
            z-index: 100;
            color: #fff;
            text-align: center;
        }
        header, .container, footer {
            padding: 20px;
            margin: 20px auto;
        }
        .container {
            max-width: 800px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }
        .about-me, .projects {
            text-align: justify;
            margin-bottom: 20px;
        }
        .projects a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            margin-right: 10px;
        }
    </style>
</head>
<body>

<div class="video-background">
    <video autoplay loop>
        <source src="space.mp4" type="video/mp4">
       
</video>
</div>

<div class="content">
    <header>
        <h1>Elsa Hagos Portfolio</h1>
    </header>

    <div class="container">
        <section id="about">
            <h2>About Me</h2>
            <div class="about-me">
                <p>I am studying Information Systems as a MS graduate student at the University of Washington Foster School of Business. My passion lies in exploring AIML infrastructures and creating meaningful data visualizations. I thrive on diving into data, predicting social behaviors, evaluating health metrics, and tackling classification challenges.</p>
                <p>Check out my website’s Visualization tab to experience the power of visual storytelling with data. The Projects tab gives you a sneak peek into the exciting endeavors I’ve been a part of, and the Blogs tab offers insights and reflections.</p>
                <p>Let’s embark on a journey through the fascinating intersection of information, tech, and data. Excited to have you along!</p>
            </div>
        </section>

        <section class="projects">
    <h2>Projects</h2>
    <a href="content.html">Content</a> <!-- Link to your new content page -->
</section>

            
        </section>
    </div>

    <footer>
        <p>&copy; 2024 Elsa Hagos</p>
    </footer>
</div>

</body>
</html>
