import json
import logging

from helga.plugins.webhooks import route


logger = logging.getLogger(__name__)


@route(r'/github_alerts', methods=['POST'])
def ghithub_alerts(request, client):
    event_name = request.getHeader('X-Github-Event')
    payload = json.load(request.content)

    logging.info('Received github event %s. Payload: %s', event_name, payload)

    return 'Success!'
