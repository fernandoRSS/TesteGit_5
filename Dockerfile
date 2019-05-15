FROM python:3


ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y



ADD main.py ./

RUN pip install selenium
RUN pip install bs4
RUN pip install mysql-connector-python

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "main.py"]