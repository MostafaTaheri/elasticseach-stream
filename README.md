# Elasticsearch Stream

## Introduction
Having reasonable logging messages in the production helps us discover logs that would otherwise be undiscoverable. ELK (Elasticsearch Logstash Kibana) is one of the best platforms for handling desirable logs.


## Setup
For setup Elastic Search, Logstash, Kibana and Rabbitmq via docker-compose use [this docker-compose file](https://gist.github.com/MostafaTaheri)


## Installing

```pip install -r requirements/requirements.txt```


## Usage

```python
from elasicsearch import ElasticSearch

if __name__ == '__main__':
    obj_ = ElasticSearch()
    context = obj_.create_schema(context={'title': 'Test'},
                                 index='ElasticSearch')
    obj_.produce(body=context)    

```