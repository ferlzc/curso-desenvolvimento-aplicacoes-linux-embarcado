
# Para instalar os headers do kernel:

`sudo apt-get install linux-headers-$(uname -r)`

# Para habilitar o módulo:
```
make

sudo insmod hello-world-module.ko
```
# Para desabilitar o módulo:

`sudo rmmod hello-world-module`

# Para limpar os arquivos gerados pelo Makefile:

`make clean`

# Para ler os as mensagens do buffer do kernel:

`dmesg`
