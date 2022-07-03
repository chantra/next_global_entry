A slightly modified version of https://github.com/mvexel/next_global_entry
which will send you an SMS with all appointments available for a given timeframe.

Main differences:

* added a `not_before` option that enforces a number of seconds before the next appointment. e.g if you need 2 hours to get to the enrollment center, you should set it to 7200.
* perform searches for a specific enrollment center location (SFO => 5446). Use `curl https://ttp.cbp.dhs.gov/schedulerapi/locations/ | jq '.[] | {id, name}'` to find the idea of the office you are interested in.
* The SMS contains the list of all available appointments matching that criteria and a link to make the appoinment.

### How to run it

```
while [ 1 ]
do
    # Run an sleep 5 min if there is appointments
    # otherwise retry in 10s.
    ./next_global_entry.py && sleep 300
    sleep 10
done
```

# Global Entry Interview Openings Checker

Scheduling an interview for your Global Entry application is hard. Some enrollment centers are months out. But they tend to sneakily add slots in the near future. This script will alert you when that happens.

This script uses the new (2017-10) but undocumented API at `https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations` to inform you of Global Entry interview openings.

*There is [another project](https://github.com/oliversong/goes-notifier) on GitHub that used to accomplish the same thing, but the new DHS web site broke it. I found it only after I got this thing working, so I thought I'd post this anyway for whomever may benefit from it.*

## Setup

- If you don't have a Twilio account, [create one]() for free, and create a free [phone number](https://www.twilio.com/console/phone-numbers). This is where your texts will originate from
- Install the dependencies `pip install -r requirements.txt`
- Copy `config.py.template` to a new file `config.py`
- Edit `config.py`:
  - Enter your Twilio [tokens](https://www.twilio.com/console)
  - Enter your Twilio ['from' phone number](https://www.twilio.com/console/phone-numbers)
  - Enter your desired destination cell number, amount of weeks to look ahead, and your city search string
- add this script to your crontab (see [virtualenv notes](https://stackoverflow.com/questions/3287038/cron-and-virtualenv)). Direct the output to a log file to keep track of it
- wait for it

*A [Two Hour Project](http://ma.rtijn.org/two-hour-projects/)*
