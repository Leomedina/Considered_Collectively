#  Considered Collectively

### Considered Collectively is a web app that allows you to track and follow bills in the United States Congress.The application is built using Python, Flask, Bootstrap 5, and deployed on Heroku using a PostgreSQL database.

## Technologies in Used:
* **Front-End:**
  * **In Use:** HTML, CSS, and Bootstrap 5 (alpha) using templates built with Jinja.
  * **Not in used:** JQuery (because it's 2020).

* **Back-End:**
  * **In Use:** Python, Flask, PostgreSQL, and Bcrypt.
  
##  Database Information:

* **DATABASE:**
  * Data is stored in a many-to-many PostgreSQL database on Heroku.
  * User password data is encrypted using Bcrypt.
  * Bills are only saved when a user clicks on "Follow The Bill". This saves space on the server.
  * Bills are updated every morning when an external cron job makes a  request to a secret route, allowing for the user to see the latest bills whenever they login.
* **DATA USED:**
  * [ProPublica's Congress API.](https://www.propublica.org/datastore/api/propublica-congress-api)

## Testing
All Functions will be broken down and unit tested wherever possible. This section is still a WIP, more to come soon.

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported. Report it here by creating an issue: https://github.com/Leomedina/Follow_Your_Rep/issues.

Help me fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Team:

* **UI / UX:** Leo Medina
* **Front-End Developer:** Leo Medina
* **Back-End Engineer:** Leo Medina

## Screenshots:

![User landing page](https://i.imgur.com/FJTdpc7.jpg)

![User Search page](https://i.imgur.com/ySnn9ty.jpg)