from typing import Optional

from django.utils import timezone

from kombu import (Exchange, Queue)

from elasticsearch_stream.celery import app


class ElasticSearch:
    def create_schema(self,
                      context: dict,
                      index: str) -> dict:
        """This method is used for preparing schema"""
        self.__context = {
            'index': index,
            'registration_time': timezone.now(),
            'context': context
        }

    def produce(self, body):
        """Produces a task for sending data."""
        queue_ = Queue(name="elasticsearch.queue",
                       exchange=Exchange("elasticsearch.log"),
                       routing_key="elasticsearch.routing")
        with app.producer_or_acquire(None) as producer:
            producer.publish(
                body=body,
                serializer='json',
                exchange=queue_.exchange,
                routing_key=queue_.routing_key,
                declare=[queue_],
                retry=True,
            )
