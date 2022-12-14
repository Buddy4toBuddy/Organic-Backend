FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# Copy the source from the current directory to the Working Directory inside the container
COPY . /app/ 
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # build-essential \
        curl \
        gcc \
        wget \
        git \
        g++ \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --default-timeout=600 -r requirements.txt

# Copy the source from the current directory to the Working Directory inside the container
COPY . /app/
EXPOSE 9000
# Run the executable
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
