FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Install Playwright dependencies
RUN apt-get update && apt-get install -y wget gnupg && \
    playwright install-deps && \
    playwright install

# Run the tests and generate the HTML report
CMD ["pytest", "--html=report.html"]