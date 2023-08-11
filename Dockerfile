FROM python:3.7
WORKDIR /app
COPY . /app
# 安裝 chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -qqy && \
    apt-get -qqy install google-chrome-stable && \
    rm /etc/apt/sources.list.d/google-chrome.list && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
# 安裝指定在 requirements.txt 的 python 套件
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
# Define environment variable
ENV NAME World
CMD ["python", "main.py"]
