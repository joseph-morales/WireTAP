# What is 'WireTAP'?
WireTAP is a Python script that can be used to record the microphone on your desktop/laptop
you can use it on a Raspberry Pi as a small remotely controlled spy bug using a USB sound card.

you can also use it if you create a little circuit that can intercept inbound and outbound calls
on a telephone line connected to the RPi using a USB sound card, you would just need to modify the
code a bit to sense the difference in sound to start and stop recording automatically.

That's a project for a later date MAYBE, depending on how many request I get on that topic.

# Setting up the prerequisites before running
username@localhost: [~] $ pip install -r requirements.txt

# How do I use wiretap.py
it's very simple just open your shell and type the following command to start recording:

python wiretap.py --record

or you can type "python wiretap.py --help" to see a list of options that you can use.

wiretap.py will name the .wav file using a random number generated MD5 hash, for example: D68260409E76CC8D225BE9882130CE4E--063723-2019.wav

# User Defined Settings
In wiretap.py in the Record() function, you can change the seconds variable to what ever amount of seconds you wish wiretap to record for.
The default record time is set to 30 seconds.
