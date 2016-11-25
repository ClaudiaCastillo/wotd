# Word of the Day

**Word of the Day Flask App using Wordnik**

## Getting Started

To run the application follow these steps:

1. Clone the repository and CD into it.

2. Go to [developer.wordnik.com](http://developer.wordnik.com/) and obtain an API key to fetch data for the word of the day application.

3. Create a .env file and add the following configurations:

    - SECRET_KEY=""
    - WORDNIK_API_KEY=""

4. Run the development server:

        $ ./manage.py runserver

If everything works you should see the word of the day when you open a browser to the localhost URL specified by the `runserver` script.

## Docker

The point of the exercise in creating the WOTD app was to explore the use of Docker (and have a more complex application with a required environment than the cats example). To use the example in docker you can pull the [image from Docker Hub](https://hub.docker.com/r/bbengfort/wotd/) and run the app as follows:

    $ docker run -p 8888:5000 --name wotd --env-file .env bbengfort/wotd

This should fetch the image from docker hub if it's not already on your machine and run it, mapping port 8888 to the Flask port 5000 and loading the environment from the .env file you created above. You should then be able to navigate to [localhost:8888](http://localhost:8888/) to view the app if everything is configured correctly.
