# DELL server fan control

------

- This Python script uses the CPU temperature to control the speed (RPM) of the fans using ipmitool.
	If not available it can be installed with: 
	
	```shell
	sudo apt update && sudo apt install ipmitool
	```



- For the script, the *`IP`* of the server, the *`username`* and its *`password`* are needed and must be inserted in the code.
  Therefore, the script should be stored so that **only the owner**, who has the password, alone has **rights** to **read** and **write**.
  However, anyone can execute this script.
  The `CHMOD` rule for this would be `711` or `-rwx--x--x` and can be assigned with:
  
  ```shell
  sudo chmod 711 /PATH/TO/FILE
  ```
  
  

- In order for the Python script to run, the package `gpiozero` must be installed. If not available, this can be done with:

  ```shell
  sudo pip3 install gpiozero
  ```

  Make sure that you have the right virtual environment (if used).



- To ensure that the script is started reliably when the server is booted, you should start it using a cronjob.
  To do this, usually open the user-crontab with

  ```shell
  crontab -e
  ```

  and enter the following:

  ```shell
  @reboot python3 /PATH/TO/FILE > /PATH/To/FILE/TO/LOG/ERRORS/WITH/CRON 2>&1
  ```

  If errors occur (for example because the logfile path requires root), the above entry must be entered in the root-crontab. This is edited with:

  ```shell
  sudo crontab -e
  ```
  


- Since I don't have a DELL server myself, I may not have checked the script for all errors.
  Therefore I would be happy if you report bugs immediately so that I can fix them.

