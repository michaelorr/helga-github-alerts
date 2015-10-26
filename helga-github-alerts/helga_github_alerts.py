import json
import logging

from helga.plugins.webhooks import route


logger = logging.getLogger(__name__)


@route(r'/github_alerts', methods=['POST'])
def ghithub_alerts(request, client):
    event_name = request.getHeader('X-Github-Event')
    payload = json.load(request.content)

    logger.debug('Received github event %s. Payload: %s', event_name, payload)

    # Setting up a webhook: github will send a 'ping' event
    # See: https://developer.github.com/webhooks/#ping-event
    if event_name == 'ping':
        logger.info('Responding to github webhook PING: %s', payload)
        return 'PONG'

    return 'Success!'
