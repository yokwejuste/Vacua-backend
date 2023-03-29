<h1 align="center">VACUA PROJECT BACKEND</h1>

## About
****
**Vacua Backend provides all the API calls and queries of this project.**

## Installation
1. Fork, clone the repository and change directory into it.
   ```bash
    # Cloning the repository
    git clone https://github.com/<username>/Vacua-backend
   
   # Change directory
   cd Vacua-backend
    ```
2. Setup a new postgres database
Assuming postgresql is install in the computer follow what's next or get to [here for linux](https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04) or [here for windows](https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm).
   - ```bash
      # accessing the postgres CLI
      sudo -u postgres psql
      ```
   - ```postgresql
     -- Create a database
     CREATE DATABASE vacua_db;
     
     -- create a new user with the details below
     CREATE USER admin WITH ENCRYPTED PASSWORD 'password';
     -- Grant all priviledges
     GRANT ALL PRIVILEGES ON DATABASE vacua_db TO yokwejuste;
       ```
3. Create, activate a virtual environement in the project
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. Install dependencies from the pypi
    ```bash
    pip intall -r requirements.txt
   ```
5. Do some data migration and predata seeding to the database
    ```bash
   python manage.py migrate && python manage.py post_data --mode clear
   ```
6. Run the project and view the documentation at the default port: [http://127.0.0.1:8000](http://127.0.0.1:8000)
