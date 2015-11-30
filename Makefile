CC=git
LDFLAG=https://github.com/magichal/SMART.git
LPFLAG=-a


all: commit

commit: 
	@$(CC) add --all ./*
	@$(CC) commit -a
	@echo "operation terminee"

push:
	@$(CC) push $(LDFLAG)


pull:
	@$(CC) pull


upstream:
	@$(CC) remote add upstream $(LDFLAG)
