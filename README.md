# internet_speed_twitter_complaint_bot

A Python / Selenium script testing intenet speed (https://www.highspeedinternet.com/tools/speed-test) and sending a complaint-tweet to the internet provider if the speed is lower than declared.

It requires to pass into the environment variables:
  * Twitter login
  * Twitter password
  * Twitter username

Individual parameters that have to be set in the __init__ method:
  * Internet provider's Twitter username
  * Minimal declared internet speed down/up

As the Twitter website can change in the future it may be required to change logging in / tweet sending methods.

The logging in method is designed for often logging in users, when Twitter requires additional verification. For users from whom Twitter does not require this type of verification logging in method needs to be changed.
