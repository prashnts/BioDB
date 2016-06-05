# BioDB

Hi There!

You're looking at the development repository of web interface of the Biology Softwares catalogue. This is an academic project at @ClusterInnovationCentre  carried out by @devkhan and @prashnts.

## Getting Started

To setup a development instance of BioDB, please make sure you setup a development enviroment consisting of:
- Python 3.5
- NodeJS v4 or above
- NPM 3.9 or above

### 0. Clone this repository and make a virtual environment
For BioDB to have clean environment to run in, it's recommended to use a virtualenvironemnt. Please check and install `virtualenvwrapper` if you're unfamiliar.
- `git clone https://github.com/PrashntS/BioDB.git`
- `cd BioDB`
- `mkvirtualenv BioDB -p python3`

### 1. Install required packages
To install the packages, open your terminal and run the following from the root directory.

- `pip install -r requirements.txt`
- `npm install`

This will download and install all the required packages.
Please note that you may need to install `brunch` as a global module. In that case, run:
- `npm install -g brunch/brunch#aaaee25`

### 2. Update your configurations
Several parameters can be controlled via configuration file.

To create your own, first create a copy of the config file:
- `cp biodb/_config.sample.py biodb/_config.py`

In your favourite editor, open this file and update the configuration.

### 3. Running
To begin, run the following command which will build assets, and database for you:

- `npm run firstrun`

To start the server at any point, simply run:

- `npm start`

Go to http://localhost:8900/ to visit the server.

To rebuild the frontend assets and (optionally) watch for changes, run:

- `brunch w`



