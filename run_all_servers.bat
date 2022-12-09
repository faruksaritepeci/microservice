@ECHO OFF

:: RUN LOAD BALANCER at 127.0.0.2:8000
start "sv-ip_address_register" /min cmd.exe /k "python ip_address_register/manage.py runserver 127.0.0.1:8000"

start "sv-api_gateway" /min cmd.exe /k "python api_gateway/manage.py runserver 127.0.0.3:8000"

start "sv-orderview" /min cmd.exe /k "python orderview/manage.py runserver 127.0.0.4:8000"

start "sv-ordercontroller" /min cmd.exe /k "python ordercontroller/manage.py runserver 127.0.0.5:8000"

:: start "sv-load_balancer" /min cmd.exe /k "python load_balancer/manage.py runserver 127.0.0.2:8000"
:: start C:\"Program Files"\Google\Chrome\Application\chrome.exe "http://127.0.0.2:8000/"
:: TIMEOUT /T 10 /NOBREAK



ECHO All servers started!
ECHO IP ADDRESS OF API GATEWAY = 127.0.0.3:8000
ECHO TO CLOSE ALL SERVICES:
pause

:: Kill all started services after key enter

taskkill /FI "WindowTitle eq sv-ip_address_register*" /T /F
taskkill /FI "WindowTitle eq sv-api_gateway*" /T /F
taskkill /FI "WindowTitle eq sv-ordercontroller*" /T /F
taskkill /FI "WindowTitle eq sv-orderview*" /T /F
