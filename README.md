# Media Browser Application

## Description
This Media Browser application is a Flask-based web server that allows users to navigate and view media files (images and videos) stored in a specified directory. It features a clean, responsive interface with pagination for easy browsing.

## Features
- Browse directories and media files.
- View images and videos directly in the browser.
- Responsive design with Bootstrap for improved mobile experience.
- Pagination for easy navigation of directories with many files.

## Installation
To get this project running on your local machine, follow these steps:
1. **Clone the Repository**
2. **Set Up a Virtual Environment** (Optional but recommended)
3. **Install Required Packages**
4. **Running the Application**


The application will start running on `http://127.0.0.1:8000` by default.

## Usage

After starting the application, navigate to `http://127.0.0.1:8000` in your web browser. The interface allows you to:

- Click on folder names to navigate through the directory structure.
- Click on images or videos to view them.
- Use the pagination controls at the bottom to navigate through lists of files.

## Configuration

To configure the application for your needs, modify the `MEDIA_FOLDER` variable in `app.py` to point to the directory containing your media files.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Flask, a lightweight WSGI web application framework.
- Bootstrap, for responsive front-end design.
