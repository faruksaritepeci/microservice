@ECHO OFF

:: RUN LOAD BALANCER at 127.0.0.2:8000
start "sv-ip_address_register" /min cmd.exe /k "python ip_address_register/manage.py runserver 127.0.0.1:8000"

start "sv-load_balancer" /min cmd.exe /k "python load_balancer/manage.py runserver 127.0.0.2:8000"
:: start C:\"Program Files"\Google\Chrome\Application\chrome.exe "http://127.0.0.2:8000/"
:: TIMEOUT /T 10 /NOBREAK



ECHO All servers started!
ECHO IP ADDRESS OF LOAD BALANCER = 127.0.0.2:8000
ECHO TO CLOSE ALL SERVICES:
pause

:: Kill all started services after key enter
taskkill /FI "WindowTitle eq sv-load_balancer*" /T /F
taskkill /FI "WindowTitle eq sv-ip_address_register*" /T /F