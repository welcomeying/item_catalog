# Item Catalog Web App
Project 4 of the **Udacity Full Stack Web Developer Nanodegree**

## About the project
Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

This is a RESTful web application using the Python framework Flask along with implementing Google OAuth2 authentication.

## How to run project
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
2. Clone or download project files in this repository.
3. Clone or download [Udacity full-stack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
4. Find the `catalog` folder from step 3 and replace it with content from step 2.
5. Start the virtual machine:
- Open your shell interface and navigate to the project directory, run the command `vagrant up`.
- Run `vagrant ssh` when `vagrant up` is finished running.
- Change directory to `/vagrant/catalog`
6. Run `sudo python -m pip install SomePackage` to install required python packages(replace `SomePackage` with `flask`, `squalchemy`, `requests` and `oauth2client`).
7. Setup application database `python database_setup.py`
8. (Optional)Insert sample database `python lotsofitems.py`
9. Run `python main.py` to execute the program.
10. Access the application in your web browser using [http://localhost:5000](http://localhost:5000)

## How to use the application
This application is initially presented with a list of categories. Clicking a category presents the associated items of that category. 

If you preferred to have an empty database to start with, please skip step 8.

After login with Google, user will be able to create/edit/delete new categories and items.

## JSON Endpoints

The following API endpoints are in JSON format and are open to the public:

Catalog JSON: `/catalog/JSON` - Displays all categories. 

Category JSON: `/catalog/<string:category_name>/JSON` - Displays items for a specific category.

Category Item JSON: `/catalog/<string:category_name>/item/<string:item_name>/JSON` - Displays a specific category item.
