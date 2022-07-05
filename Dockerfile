# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./Pipfile /code/Pipfile

#
RUN pip install pipenv 
RUN pipenv install

# 
COPY ./sentiment_analyzer /code/sentiment_analyzer

# 
CMD ["pipenv", "run", "uvicorn", "sentiment_analyzer.api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]