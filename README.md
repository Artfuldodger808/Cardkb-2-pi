# Cardkb-2-pi
Use the cardkb from m5stack over i2c with the raspberry pi

Live those cyberpunk DREAMS by using the Cardkb from M5stack over i2c with your raspberry pi and Build the cyberdeck of your competitors NIGHTMARES 😜

https://github.com/Artfuldodger808/Cardkb-2-pi/blob/main/ookpmc_6c723b2c79c6f8d7272078c241c6967f903a596e.jpg
https://github.com/Artfuldodger808/Cardkb-2-pi/blob/main/yd3gr9_6e824cac06cb8ed7b7c7384205168f27c0df57f4.jpg
I wanted to use the cardkb from M5stack as general input for my raspberry pi running Kali Linux, 
At first (being as thorough as usual) I skipped reading the useful information in the user guide for the cardkb and went straight
into trying to figure out how this device works with the help of gpt3.5 🤷‍♂️.

At first we wrote a program to activate the i2c bus and print subsequent ascii returns to the console,
using that template I was able to log each button pressing's code return and build up a library of 
codes relating to each key press.(although looking at the datasheet for the cardkb might have saved me some time)

Then after much pushing and prompting I was able to get chatgpt to write a useful python program using the ascii library
I had developed. Mind you this is a work in progress and not all of the possible button combinations have been mapped or are used,
But using this as a template you should be able to fill in the rest of the blanks relatively easy, 

INSTALLING ON THE PI

You need to install some requirements to run this program

pip3 install smbus

pip3 install keyboard

Here is an instruction to run the program on boot

To run your Python script on bootup of the Raspberry Pi, you can use the cron scheduler. Here are the steps to set it up:

Open the crontab configuration:

crontab -e

Add a line to run your script on boot. For example, if your script is named cardkb-2-pi.py and is located in the home directory, you can add:

@reboot sudo python3 /home/pi/cardkb-2-pi.py

Adjust the path and filename to match your actual script.

Save the file and exit the editor.

This will schedule your script to run at reboot. Note that the @reboot directive in cron is specifically designed for running tasks at startup.

Make sure your script has the necessary permissions to be executed. You can set the execute permission with the following command:

chmod +x /home/pi/cardkb-2-pi.py

This assumes your script is located at /home/pi/cardkb-2-pi.py Adjust the path accordingly.

Reboot your Raspberry Pi, and your script should start running automatically.

