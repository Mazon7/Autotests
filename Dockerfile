# Use an official Python runtime as a parent image
FROM joyzoursky/python-chromedriver:3.9

# Set the working directory in the container
WORKDIR /tests

# Use ENV variables
ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

# Install Chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get -y update
# RUN apt-get install -y google-chrome-stable

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
# COPY . .

# Run your tests using pytest
CMD ["/home/chrome/.local/bin/pytest"]