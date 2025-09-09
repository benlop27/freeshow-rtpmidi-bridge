# FreeShow RTP MIDI Bridge

A simple RTP MIDI to HTTP bridge for controlling FreeShow via REST API.

> **Note:** The FreeShow app's API Option must be enabled for this bridge to work. You can enable the API Option in FreeShow's settings. For more information, visit [https://freeshow.app/](https://freeshow.app/).
>
> For more information about the RTP MIDI protocol, see [RTP-MIDI on Wikipedia](https://en.wikipedia.org/wiki/RTP-MIDI).

## Features
- Listens for RTP MIDI note events (e.g., from a DAW or MIDI controller)
- Sends HTTP requests to FreeShow when specific MIDI notes are triggered (e.g., C4 for next slide)
- Easy to configure and extend
- Professional, production-ready codebase

## Usage
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the FreeShow RTP MIDI Bridge:
   ```sh
   python __main__.py
   ```
3. Configure your MIDI device or DAW to send RTP MIDI to this server (default port: 5051).
4. When C4 (Middle C) is pressed, the bridge will send a REST API call to FreeShow (default: http://localhost:5506).

## Configuration
- Edit `FREESHOW_API_URL`, `MIDI_SERVER_HOST`, `MIDI_SERVER_PORT`, and `SLIDE_ACTION` in `__main__.py` as needed.

## Example
- Pressing C4 (Middle C) on your MIDI device triggers a slide change in FreeShow.

## Extending
- Add more MIDI note actions by editing the `on_midi_commands` method in `FreeShowRtpMidiBridgeHandler`.

## License
MIT License (see LICENSE file)

---

### Architecture Diagram

```mermaid
flowchart LR
    subgraph User MIDI Device/DAW
        A[Computer / Mac (DAW, MIDI App, or Controller)]
    end
    subgraph RTP MIDI Network
        B[RTP MIDI Protocol]
    end
    subgraph FreeShow RTP MIDI Bridge
        C[Python Server\n(__main__.py)]
        C1[Future: Plugin Support]
        C2[Future: Configurable Actions]
        C3[Future: Web UI]
    end
    subgraph FreeShow
        D[FreeShow HTTP API]
    end
    A -- Note On (C4) --> B
    B -- RTP MIDI --> C
    C -- HTTP POST /action:next_slide --> D
    C -- "" --> C1
    C -- "" --> C2
    C -- "" --> C3
```

---

## Disclaimer

This project is an independent, community-driven tool and is not affiliated with, endorsed by, or supported by the FreeShow application or its developers. FreeShow is available at [https://freeshow.app/](https://freeshow.app/). All trademarks, product names, and company names or logos mentioned are the property of their respective owners.

Use this bridge at your own risk. I'm not responsible for any issues, damages, or data loss that may result from its use.
