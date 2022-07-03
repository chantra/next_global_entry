#!/usr/bin/env python3
"""Check for Global Entry interview openings in your city."""

import sys
import datetime
import requests
from twilio.rest import Client
import config


def log(text):
    """Write a one-line log message."""
    print("{dt}\t{msg}".format(
        dt=datetime.datetime.now(),
        msg=text))


if __name__ == '__main__':
    # calculate date
    now = datetime.datetime.now()
    delta = datetime.timedelta(weeks=config.look_ahead_weeks)
    future = now + delta
    start_time = now + datetime.timedelta(seconds=config.not_before)

    request_url = config.global_entry_query_url.format(
        location=config.location,
        start_timestamp=start_time.replace(microsecond=0).isoformat(),
        end_timestamp=future.replace(microsecond=0).isoformat()
    )
    result = requests.get(request_url).json()
    text_arr = []
    for r in result:
        if r['active'] > 0:
            text_arr.append(f"{r['active']} openings {r['timestamp']}")

    if len(text_arr) > 0:
        client = Client(config.twilio_account, config.twilio_token)
        message = client.messages.create(
            to=config.to_number,
            from_=config.twilio_from_number,
            body="GE interview\n{}\n{}".format(config.global_entry_goto_url, "\n".join(text_arr))
        )
        log("text message sent {} {}".format(message, "\n".join(text_arr)))
        sys.exit(0)
    log("no news")
    sys.exit(1)
