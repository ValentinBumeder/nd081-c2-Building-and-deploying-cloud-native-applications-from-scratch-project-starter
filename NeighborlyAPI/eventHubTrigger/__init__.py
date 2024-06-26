import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):
    logging.info('Hallo')
    logging.info('Function triggered to process a message: %s', event.get_json())
    #logging.info('  EnqueuedTimeUtc = %s', event.metadata['EnqueuedTimeUtc'])
    #logging.info('  SequenceNumber = %s', event.sequence_number)
    #logging.info('  Offset = %s', event.offset)

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })
    
    logging.info('Python EventGrid trigger processed an event: %s', result)



