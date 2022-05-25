# metropi

## Overview
This project is used to displays the nearest four trains at a specific metro stop in Washington DC. The project runs on a Raspberry Pi and the display used is the [e-ink hat from Waveshare]([https://www.adafruit.com/product/4687](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(D))).

The display shows the following information for each train (up to 4):
* Destination of the metro - example being "Largo"
* Which line the train is running on - example being "BL"
* The arrival time of the nearest train - example being "5"

## Installation
* Create API access token on the [WMATA developer site](https://developer.wmata.com/)
* Clone the repository on your Raspberry Pi with the following `git clone https://github.com/ozzy-simpson/metropi.git`
* Change into the working directory of the cloned repository `cd metropi`
* Install the required dependencies `pip3 install -r requirements.txt`
* Create a file named `.env` in your directory with the following content `METRO_API_KEY = 'YOUR_METRO_API_KEY'`
* Run the main program `python3 main.py`

## Configuration
* To change the station being displayed modify `line 56` in `main.py` with the station code you want to use.
* Station codes can be found in [the following JSON](https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe3311?) from the WMATA API.

## Running on boot and restarting when it freezes
You can use [these instructions](https://thepihut.com/blogs/raspberry-pi-tutorials/auto-starting-programs-on-the-raspberry-pi) and [metropi.service](/metropi.service) to setup the Pi to run main.py on boot and restart it when the program crashes/freezes.
