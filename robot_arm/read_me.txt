
Matt Dyson
My life, and everything in it

Menu
SKIP TO CONTENT
HOME
ABOUT
BLOG
PROJECTS
PORTFOLIO
Robot Arm
A couple of years ago I was given a Robotic Arm for Christmas, and more recently discovered that you can get a USB control board to allow you to hook it up to any computer. The controller that comes with the arm is pretty naff, and is very difficult to use, so I set about finding a better one! The recent release of the Raspberry Pi had inspired me to start playing around more with hardware-level things, and I’d also recently decided to learn a bit of Python (to replace my knowledge of PHP, which gets me into all kinds of trouble…!) – this seemed like a perfect project!

The controller of choice ended up being an Xbox 360 Wireless Controller for Windows, chosen mainly because I already owned one, but also as they have been around for a while, and have very good support in Linux. I blogged about my adventures getting it set up with the Rasberry Pi here, so I won’t duplicate the content – go read that post before doing anything else here!

The next challenge was getting the Robotic Arm talking to the Raspberry Pi and then creating some way of nicely interfacing with it. Turns out there’s a whole host of posts about this on the internet, the most relevant is probably this blog, which has some interesting information and source code relating to the arm. All of the examples given used PyUSB – a Python module for interfacing with USB devices. For what I needed, the version packaged with Rasbian was too old (version 0.4.something), the latest version being 1.0. In order to install PyUSB 1.0, I needed the following:

$ mkdir ~/pyusb
$ cd ~/pyusb
$ git clone https://github.com/walac/pyusb.git .
$ sudo python setup.py install
The example code that I found all related to reading a set of instructions in from a CSV or DAT file, and then executing them in order. While this is great for defining set routines to be executed over and over, I was more interested in creating a Python class that would let me issue any instruction to the arm, and have it executed straight away. I took the ideas from the blog and created RobotArm.py. This class gives you access to methods for sending instructions to any motor or light at any point, rather than being limited to a set routine. To give it a try yourself:

$ mkdir ~/robotarmcontrol
$ cd ~/robotarmcontrol
$ svn co http://projects.mattdyson.org/projects/robotarm/armcontrol .
$ sudo python testRobotArm.py
Your arm should then start moving! All this test file does is connect to the arm, and then issue instructions to a couple of motors and the light in sequence, to show you what it can do.

So – up next was actually tying the Xbox controller to the robotic arm! With all the above in place, this was extremely simple. All that’s needed is a single Python file that listens for events from the Xbox controller (see blog post for more information on that), and connects them to the relevant motor on the robotic arm. In order to get this fully up and running, including the lego-pi library and my RobotArm library above, you need the following:

$ mkdir ~/robotarm
$ cd ~/robotarm
$ svn co http://projects.mattdyson.org/projects/robotarm/ .
$ git clone https://github.com/zephod/lego-pi.git legopi
$ touch legopi/__init__.py
$ sudo python driveRobot.py
You should then see some output similar to the following. Press Ctrl+C at any point to quit.

Starting RobotArm Controller
Press Ctrl+C at any time to quit
Init'ing RobotArm
RobotArm now ready!
Try moving the analogue sticks on your Xbox controller – and the robotic arm should move!! Controls can be changed by modifying the getMotor(key) method near the top of driveRobot.py, and are set to the following by default:

Left Stick X-Axis: Base rotation
Left Stick Y-Axis: Shoulder joint
Right Stick X-Axis: Elbow joint
Right Stick Y-Axis: Wrist joint
Left Trigger: Open grip
Right Trigger: Close grip
Left Shoulder: Toggle light
Right Shoulder: Flash light
Here’s a video of the arm and controller in action!



Enjoy! Please feel free to submit any patches or suggestions in the comments below, and I’ll do my best to incorporate them.


 
50 thoughts on “Robot Arm”
Alastair says:
Feb 8, 2013 at 11:48 pm
Hopefully simple question for you to save me banging my head any more…

Can you show me how to get the dpad working to control the GPIO pins?

I can get it all to work separately using the keys listed but I add the dpad du, dd etc and it comes up with “I don’t know how to move motor”.

Thanks

Reply
Matt says:
Feb 25, 2013 at 9:46 pm
Hi Alastair

From the sounds of things, you’ve set the getMotor method in driveRobot.py to return “motor” rather than the name of one of the motors (base, shoulder, wrist, grip, elbow). Use one of those instead, and hopefully that should work! If it doesn’t, post a link to your changed code here, and I’ll see what I can do to help ??

Reply
Pingback: Using an Xbox 360 Wireless Controller with Raspberry Pi | Matt Dyson

mardicas says:
Mar 10, 2013 at 1:37 pm
Hey, the download link does not work ?? and SVN gives could not connect to server error. Hope you can fix it ??

Reply
Matt says:
Mar 10, 2013 at 1:43 pm
Unfortunately the server hosting my SVN repository and other project stuff has decided to disappear off the face of the earth! I’m hoping it’ll be available again shortly – should be sorted by the end of the week at the latest. Apologies!

Reply
mardicas says:
Mar 16, 2013 at 3:11 pm
Perhaps you can e-mail it to me if you have it somewhere else? It would be great ??

Reply
Matt says:
Mar 16, 2013 at 3:54 pm
The links should now be working again – might be a bit temperamental as I play around with the server settings though!

Reply
Andrej says:
May 17, 2013 at 11:30 am
Hi Matt, thanks for sharing! Unfortunately, SVN seems a bit “temperamental” again?

Any chance for a download zip to make it available again?

Thanks!.

Reply
Paul says:
May 19, 2013 at 5:01 pm
Hi Matt, just sat down with my son to get this fantastic project going, but cannot access the svn site.
cheers.

Reply
Matt says:
May 19, 2013 at 5:04 pm
Hi Paul,
Glad to hear you’re giving the project a go – but unfortunately my svn repository is unavailable at the moment as I’m in the process of moving house. I’ve just this minute scheduled the broadband installation, so it should be up and running again by Wednesday evening. Hope you any your son can wait that long! Apologies for the inconvenience.

Reply
Matt says:
May 22, 2013 at 11:26 am
Access to the SVN repository should now be restored. Sorry for the delay!

Reply
Peter Hurt says:
Jun 23, 2013 at 3:07 pm
I’m using a custom Xbox 360 wired controller for this project and I have managed to get the output of the controller to print in the terminal but I’m having a bit of trouble controlling the arm with the controller.
‘sudo python driveRobot.py’ worked but it did not see my controller outputs.
Next I tried:
sudo xboxdrv –device-by-id “1bad:f021” –type-xbox360 | sudo python driveRobot.py
(I tried with the commands on both sides of the | )
However, the arm still did not see my controller outputs.
Can you help?

Thanks

Reply
Matt says:
Jun 24, 2013 at 4:56 pm
Hi Peter,
The python script I’ve written (driveRobot.py) isn’t designed to take any kind of input as you’ve given it. If you need custom arguments to get your device to work with xboxdrv, you may need to have a play with RobotArm.py – I’d guess you’ll need to change the VENDOR and PRODUCT variables to match your custom controller. Good luck!

Reply
Peter Hurt says:
Jun 26, 2013 at 6:23 pm
Hi again Matt,
I’ve played around with a bunch of settings from various files and tries making a .sh launcher but still no luck.
And aren’t the VENDOR and Product variables just for the arm itself? I wont bother you about it though, I’ve sent a request for my controller in an xboxdrv patch so I’ll just wait and see if that is released sometime soon.
Thanks for helping though!

Reply
Matt says:
Jun 26, 2013 at 7:02 pm
Oh yes – my bad! The vendor/product variables relate to the arm, not to the controller!
Hope you have better luck with the xboxdrv patch, could you please post any appropriate links back here, so anyone else hoping to achieve this can learn from you adventures? Thanks!

Reply
Peter Hurt says:
Jul 7, 2013 at 11:35 am
Hi Matt,
I finally got it to work!
Here’s the method I have made to use any controller with the arm successfully:

– Open /home/pi/robotarm/legopo/lib/xbox_read.py
– On line 24 replace ‘xboxdrv’ with ‘xboxdrv –device-by-id “1bad:f021” –type xbox360’
(replace “1bad:f021” with the details of your controller instead)

That’s all you need to do for any controller.
I hope this helps people who are struggling!

Peter Hurt says:
Jul 7, 2013 at 11:38 am
In what I just posted, ‘device’ and ‘type’ use two hyphens before them. (I don’t think that they are posted properly)

Rudegnome285 says:
Oct 5, 2013 at 11:00 am
My raspi comes up with “No module named USB.core” what do I do ???

Reply
Matt says:
Oct 5, 2013 at 11:11 am
Hi,
Have you followed the steps for installing pyusb 1.0? A quick google search suggests that you might have 0.* installed, which won’t work with this script.

Reply
Rudegnome285 says:
Oct 5, 2013 at 12:01 pm
Thank you found it and followed it now what do I type I to get it to move

Reply
Rudegnome285 says:
Oct 5, 2013 at 12:10 pm
Thank you now what do I type I to get it to move

Reply
Matt says:
Oct 5, 2013 at 1:32 pm
No typing needed – your controller should be recognised automatically, and moving the joysticks should control the robot arm

Reply
Rudegnome285 says:
Nov 3, 2013 at 2:59 pm
hi matt,

bash: svn: command not found what do i do??

Reply
Matt says:
Nov 3, 2013 at 5:04 pm
Hi there! You need to have the ‘subversion’ package installed before you can use that particular command – you should run sudo apt-get install subversion to install it ??

Reply
Rudegnome285 says:
Nov 3, 2013 at 6:43 pm
thanks that works now but doing the sudo python driveRobot.py it says no module named legopi.lib

Reply
Matt says:
Nov 3, 2013 at 8:10 pm
Make sure that the “git clone” command was done properly – you may need to install the git package if this isn’t already on your system.

Reply
Rudegnome285 says:
Nov 3, 2013 at 6:44 pm
sorry i am complete noob and dont know anything think you the help

Reply
Rudegnome285 says:
Nov 5, 2013 at 4:20 pm
it still not working

Reply
Rudegnome285 says:
Jan 31, 2014 at 6:12 pm
how do you find out the details of your controller?

Reply
Michal says:
Sep 6, 2014 at 6:20 am
I would use pygame module.

Reply
AZ says:
Feb 26, 2014 at 8:43 pm
Hey Matt, Im interested in getting this project to work we got the robotic and and trying to use the WII nunchuck instead of the xbox controller, but what is the purpose of the breadboard connecting to the GPIO pins?

Reply
AZ says:
Feb 26, 2014 at 8:48 pm
You think you can show the wiring schematic for the breadboard to the GPIO?

Reply
Matt says:
Feb 27, 2014 at 6:07 pm
Hi AZ,

The breadboard was for an unrelated project, there’s no need to use the GPIO to enable the Xbox controller or Robot Arm.

Reply
AZ says:
Mar 26, 2014 at 7:25 pm
Tyyy! appreciated bro!

Reply
AZ says:
Apr 30, 2014 at 4:33 am
Hey Matt, everything went successful on downloading on the repisotary. The test script to run the robot went well however, it only worked when I used the top usb, the bottom one doesnt work and tells me that if i connected the usb correctly and run in root. However, when I run the test script when its plug in on the top it worked. Now my question is, when i plugged the robot in the top usb port and the xbox receiver on the bottom and after resyncing the controller, when i run the sudo python driveRobot.py script it gave me this error

‘Starting RobotArm Controller
Press Ctrl+C at any time to quit
Init’ing RobotArm
RobotArm now ready!
nohup: ignoring input and redirecting stderr to stdout
Traceback (most recent call last):
File “driveRobot.py”, line 45, in
for event in xbox_read.event_stream(deadzone=DEADZONE):
File “/home/pi/robotarm/legopi/lib/xbox_read.py”, line 28, in event_stream
raise ValueError(line)
ValueError: Error couldn’t claim the USB interface: LIBUSB_ERROR_BUSY
”
Can you please assist?

Reply
AZ says:
Apr 30, 2014 at 4:43 am
Disregard!! i got! thxxxx

Reply
Michal says:
Sep 6, 2014 at 6:19 am
Thank you for sharing this. This is just GREAT.

And I love the comments too. So many people learning at once: what’s version control, how to read USB, what’s Linux, what’s Raspberry, what’s a robotic arm.

This is so inspiring, I suddenly realized, that I could try to hack all those cheap “made in PRC” toys that my kids managed to destroy at some point, that they may contain salvageable parts.

And, for the USB joystick, I would just use pygame, but not knowing the rest of the software (event loop somewhere perhaps), I’m not sure if this solution would fit.

Reply
Den99999 says:
Mar 8, 2015 at 9:49 pm
Hi matt,
Great work on the arm.

I’m a novice at programming but have been trying to add 2 servo wheels under my arm and control them with the Dpad.

I’ve followed the adafruit pwm tutorial using the pi cobbler and servo controller and it works well separately. I just dont know enough to successfully map the dpad to the servos. Don’t suppose you could help?

Reply
Matt says:
Mar 9, 2015 at 9:37 pm
Hi,
Thanks! Glad you’re finding the tutorial useful!

I think you need to edit the driveRobot.py file and add the relevant python code for controlling the servos into there. You can then add some special cases for the d-pad buttons (dd, du, dl, dr) in the main for event in xbox_read.event_stream... loop to move the servos.

Hope that helps!

Reply
Den99999 says:
Mar 10, 2015 at 9:06 pm
Hi,
I did it and got it working, i just have 2 questions.
1. I cant stop the output from saying ‘don’t know how to move motor none’ when i move the dpad (on the upside the servos work fine), can I change this?

2. I plan on mapping a shutdown command to the start button, to safely close the pi down (with driveRobot.py booting at load), my kids can basically use it as a toy without damaging the pi or sd card. Do you know a good shutdown code to map to a free key?

I’ve found your project well written and easy to follow, keep up the good work.

Future plans for my arm are to
add the camera and see what I can get it to do,
try and write a set routine that imports driveRobot.py and carries out a set command then maybe map that to a spare button,
add some sensors,
maybe swap servos for dc motor’s….

Reply
Matt says:
Mar 10, 2015 at 10:40 pm
Hi,
1) You’ll need to add a continue line in somewhere – see the other special cases in that loop
2) I can’t suggest anything unfortunately, but Google should be your friend there!

Glad to hear my writeup was useful – please share your finished project, I’d love to see what it in action!

Reply
ACI says:
Apr 24, 2015 at 10:03 pm
Hey Matt!

I’m trying to reconfigure the controls so that the wrist is mapped to RB and LB. I re-mapped the light to A and X, which is working fine. However, remapping the wrist gives me some issues. I changed the key to:

return {
‘X1':’base’,
‘Y1':’shoulder’,
‘YS’:’elbow’,
‘RB’:’wrist’,
‘LB’:’wrist’,
‘RT’:’grip’,
‘LT’:’grip’
}.get(key,None)

and added the following few lines of code:
if(event.key==’RB’):
direction=1
elif(event.key==’LB’):
direction=2
else:
if(event.value0):
direction = 1

The problem is that, if the new wrist statement is declared below the grip statement, the grip will function normally – however, the wrist will only ever go up, whether I am pressing RB or LB. If the wrist statement is declared above the grip statement, the opposite is true – full functionality is restored to the wrist, but the grip will only open – whether I press RT or LT.

Reply
ACI says:
Apr 24, 2015 at 10:59 pm
a bit of my code got cut off. This is it here:

else
if(event.value0):
direction = 1

Reply
Geoff says:
Jun 12, 2015 at 9:46 am
Hi,

I have followed various different instructions online but the arm doesn’t seem to respond to the code used in the python file. it does seem to know the arm is connected by USB but does nothing.

I am also having difficulties checking the arm works at all as i only have windows 8 and the control software that comes in the box doesn’t work in windows 8.

any ideas?

Thanks,

Geoff

Reply
tommy knetsch says:
Nov 7, 2016 at 6:27 pm
hi it wont work on mine it say this:
Starting RobotArm Controller
Press Ctrl+C at any time to quit
Traceback (most recent call last):
File “driveRobot.py”, line 42, in
arm = RobotArm.RobotArm()
AttributeError: class RobotArm has no attribute ‘RobotArm’

Reply
Dinie says:
May 21, 2017 at 9:41 pm
Hey I’ve got some confusions here. Were the motors of the robot connected to the Raspberry Pi via the GPIO pins or the USB port? Because I am connecting the motors directly to the Pi. Do I need to include the pyusb.lib if the robot is not connected to the Pi via USB? Which means I also need to change the RobotArm.py code right?
Thanks for your time.

Reply
Matt says:
May 23, 2017 at 9:57 am
The motors were still connected tot he battery of the robot arm, this project used the USB interface to drive them instead of the included controller. I imagine you’ll need a separate motor driver board if you want to run them from the Pi – connecting them directly could be dangerous! The RobotArm.py code will need replacing with code that interacts with the motor driver.

Reply
Stephan says:
Jun 30, 2017 at 12:08 pm
Hi Matt,
thank you for sharing!
Since i do not own an Xbox Controller but a Logitech F310 Gamepad, i took your repository as base to make it work with
the Logitech F310 Gamepad.
Instead of using the Lego-pi library, i took evdev (a generic Linux input driver) and build the scripts around it. Should work with every linux machine.

In case someone wants to try it out, submit patches or suggestions, go ahead:
https://github.com/pastelhh/OWOLogitechF310Control

Reply
hqc says:
Jun 14, 2018 at 3:15 pm
hey Matt,
I am trying to use flick-hat to control my OWI robotic arm with usb kit. I followed the instruction in this website https://www.hackster.io/pi-supply/raspberry-pi-as-a-robotic-arm-controller-with-flick-hat-412827 but after install everything in my raspberry pi , I try to test my robot by using ‘sudo python testRobotArm.py’. And I get following

‘Init’ing RobotArm
Traceback (most recent call last):
File “testRobotArm.py”, line 10, in
arm = RobotArm.RobotArm()
File “/home/pi/armcontrol/RobotArm.py”, line 27, in __init__
raise ValueError(“Could not connect to Robotic Arm USB device. Is the arm connected properly? Perhaps you’re not running as root?”)
ValueError: Could not connect to Robotic Arm USB device. Is the arm connected properly? Perhaps you’re not running as root?
Stopping RobotArm
Exception AttributeError: “‘NoneType’ object has no attribute ‘ctrl_transfer'” in <bound method RobotArm.__del__ of > ignored’
I think I connect the arm correctly and set up everything, and i checked lsusb that the usb is detected asBus 001 Device 004: ID 1267:0001 Logic3 / SpectraVideo plc

Is there any solution?

Reply
hqc says:
Jun 14, 2018 at 8:21 pm
I get it, the idProduct should be 0001 for my case

Reply
Leave a Reply
Your email address will not be published. Required fields are marked *

Comment 

Name * 

Email * 

Website 

Save my name, email, and website in this browser for the next time I comment.

Recent blog posts
Where has ‘the truth’ gone?
The truth about the Gatwick ATC closures
Monitoring Bitcoin with Nagios
Controlling a Sony Bravia TV with Google Home
Talking to a Tesla through Google Home
Twitter
On the menu this evening - my first sample of Tactical Nuclear Penguin by @brewdogofficial -- by far the strongest… https://t.co/bmYQodzkPk - 5 days ago

New #CitiesSkylines expansion just as I start 2 weeks of leave?! Thanks @Cities_PDX for a great excuse to not go outside for a few days! - 6 days ago

As much as I dislike night shifts, there is something incredibly satisfying about getting into bed as everyone else… https://t.co/T5AY6jxSl2 - 7 days ago

Visit My Profile
Donate
Like what you see? Please consider a small donation so I can carry on doing projects like these!

Bitcoin Address: 16EFxXC1JDPkKyW1pRie9U2aM98jjevdUb

Bota WordPress Theme Powered By WordPress