Markdown syntax

https://www.markdownguide.org/basic-syntax/





## References and books

Old fashion classic linux basics book from 2002 
by linux enthusiast Костромин Виктор Алексеевич 

Linux для пользователя

`https://it.wikireading.ru/11239`

***

My gdoc small manual 

`
https://docs.google.com/document/d/14NyQoaWghoC6b5oQCwo1EX9Zr6T6ABMpxSMIp4A2xcg/edit#heading=h.vmbwmera18yh
`

***




## Shell usage

### HotKeys

ctl+C end current bash process

ctl+C end current input

### Running commands: 

`; || && stdin stdout etc` 

https://it.wikireading.ru/11316

Using '&'

`whoami & echo '\n***First echo***\n' & echo '\n***Second echo***\n' &`

Run commands in background and just after return bash control bak 


Using '||'

`eecchhoo '\n***First echo***\n' || echo '\n***Second echo***\n'`

Run command after '||' only prev not return success code, in essence run first success command and stops. 
The example will execute only the second.

Using '&&'

`eecchhoo '\n***First echo***\n' && echo '\n***Second echo***\n'`

Opposite to '|| Second command be executed only if first return the success code.
Example will not be executed.


Using '>', '<' and '<<', '>>'

???

Using '|', '|;'

Direct stdoutput from left commad to sdtin for right command using pipes

`echo “Welcome to Linux” | wc -m`

While | usage run commands in parallel, '|;' waiting until left command will end







### Configuring shell

shopt

### Bash scripting

`https://it.wikireading.ru/11344`

## Package managers

### Pacman

See package info `pacman -Qi <name>`


### Tips & tricks

### How to take 1st (or N) column of command output

`cat <some-file> | grep 'some grep'  | sed 's/\|/ /'|awk '{print $1}'`


E.g. in follow command we looking for all docker containers matched to '3dmm name' 
and output last value of first column (hash) of results, now we can do something with this hash
 
`docker ps -a | grep '3dmm' | sed 's/\|/ /'|awk '{print $1}'|tail -n 1`

`cat /etc/passwd | awk -F':' '{ print $1 }'` - this way to take the 1st col

`cat /etc/passwd | cut -d: -f1` - or this way to take the 1st col

##


### Small utils

#### List of simple utils
echo, printf, time, whoami, wc, pwd, date, hwclock, 
cat, tail, shuf