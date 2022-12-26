from elasicsearch import ElasticSearch


def execute_elasticsearch():
    obj_ = ElasticSearch()
    context = obj_.create_schema(context={'title': 'Test'},
                                 index='ElasticSearch')
    obj_.produce(body=context)
