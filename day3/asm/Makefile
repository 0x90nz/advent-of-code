AS=nasm
LDFLAGS=-static -g

%.o:%.asm
	$(AS) -felf64 $< -o $@

main: main.o

clean:
	rm -f *.o main


