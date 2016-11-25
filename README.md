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
