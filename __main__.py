"""
FreeShow RTP MIDI Bridge

A simple RTP MIDI to HTTP bridge for controlling FreeShow via REST API.

Based on the pymidi library.

Eventually will be packaged and published to PyPI, maybe...
Thinking on create an AU/VST plugin to send FreeShow commands via MIDI from the DAW instead.
 
"""

import logging
from typing import Any, List
from pymidi import server
import requests
 

PRODUCT_NAME = "FreeShow RTP MIDI Bridge"
MIDI_SERVER_HOST = '0.0.0.0'
MIDI_SERVER_PORT = 5051
FREESHOW_API_URL = 'http://localhost:5506'
SLIDE_ACTION = 'next_slide'
C4_KEY_VALUES = ["C4", 60]

logging.basicConfig(
    level=logging.INFO,
    format=f'%(asctime)s [{PRODUCT_NAME}] %(levelname)s: %(message)s',
)

class FreeShowRtpMidiBridgeHandler(server.Handler):
    """Handler for FreeShow RTP MIDI Bridge server."""

    def on_peer_connected(self, peer: Any) -> None:
        """Called when a peer connects to the server."""
        logging.info(f'Peer connected: {peer}')

    def on_peer_disconnected(self, peer: Any) -> None:
        """Called when a peer disconnects from the server."""
        logging.info(f'Peer disconnected: {peer}')

    def on_midi_commands(self, peer: Any, midi_commands: List[Any]) -> None:
        """Handle incoming MIDI commands from a peer."""
        for midi_command in midi_commands:
            if midi_command.command == 'note_on':
                key_value = midi_command.params.key
                velocity_value = midi_command.params.velocity
                if key_value in C4_KEY_VALUES:
                    logging.info(f'C4 (Middle C) triggered with velocity {velocity_value}')
                    try:
                        response = requests.post(FREESHOW_API_URL, json={'action': SLIDE_ACTION}, timeout=2)
                        response.raise_for_status()
                        logging.info(f'Slide control action "{SLIDE_ACTION}" sent successfully.')
                    except requests.RequestException as error:
                        logging.error(f'Failed to send slide control action: {error}')
                else:
                    logging.info(f'Key {key_value} triggered with velocity {velocity_value}')

def main() -> None:
    """Start the RTP MIDI server and add the custom handler."""
    logging.info(f'Starting RTP MIDI server on {MIDI_SERVER_HOST}:{MIDI_SERVER_PORT}...')
    midi_server = server.Server([(MIDI_SERVER_HOST, MIDI_SERVER_PORT)])
    midi_server.add_handler(FreeShowRtpMidiBridgeHandler())
    logging.info('Server is running and ready to receive MIDI commands.')
    try:
        midi_server.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server shutdown requested by user.')
    except Exception as exc:
        logging.error(f'Unexpected error: {exc}')

if __name__ == "__main__":
    main()