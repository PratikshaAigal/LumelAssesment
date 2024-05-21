# Install the requirements
pip install -r requirements.txt

# Start the server
cd Lumel

## Migrate the Database
python manage.py migrate

## Run the script to load the data from csv file
python manage.py runscript dataloading

## Start the server
python manage.py runserver

## Endpoints
http://127.0.0.1:8000/customer_analysis?start_date=2024-02-28&end_date=2024-04-28

