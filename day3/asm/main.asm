	; ----------------------------------------------------------------------
	; Advent of Code Day 3 Part 1
	; ----------------------------------------------------------------------
	section .text

	extern fopen
	extern fscanf
	extern strtoll
	extern printf

	global main
main:
	mov	rdi, infile
	mov	rsi, filemode
	call	fopen

	test	rax, rax
	jz	.exit

	mov	[file], rax
	call	read_records

	xor	rax, rax
	mov	rbx, [totalrecs]
	sar	rbx, 1			; rbx /= 2
	xor	rcx, rcx		; index
	mov	rdx, 1			; active bit
	xor	rdi, rdi		; the "gamma" value
.loop:
	mov	rsi, [poscounts+rcx*8]
	cmp	rsi, rbx

	; the most common bit was zero, so skip this
	jl	.next

	; otherwise set that bit
	or	rdi, rdx
.next:
	shl	rdx, 1
	inc	rcx
	cmp	rcx, bitcount
	jl	.loop

.gamma:
	;; print the gamma and epsilon values
	mov	rbx, rdi		; keep it safe

	mov	rsi, rbx
	mov	rdi, decformat
	xor	al, al			; 0 fp args (tricky part of x86_64 abi!)
	call	printf

.epsilon:
	mov	rsi, rbx
	xor	rsi, 0b111111111111
	mov	rdi, decformat
	xor 	al, al
	call	printf

.power:
	mov	rax, rbx
	xor	rax, 0b111111111111
	mul	rbx

	mov	rsi, rax
	mov	rdi, decformat
	xor	al, al
	call	printf

.exit:
	ret


read_records:
	;; read in the next line
.line:
	mov	rdi, [file]
	; rdi is already ptr to file
	mov	rsi, informat
	mov	rdx, numbuffer
	xor	al, al
	call	fscanf

	cmp	eax, 0			; using eax is important! it's a signed /int/
	jle	.done

	mov	rdi, numbuffer		; the string we just got
	xor	rsi, rsi		; no endptr
	mov	rdx, 2			; base 2
	call	strtoll

	;; update the pos counts
	mov	rdx, rax		; value we have
	xor	rcx, rcx		; counter
.loop:
	mov	rdx, rax
	and	rdx, 1

	test	rdx, rdx
	jz	.noinc
	inc	qword [poscounts+rcx*8]

.noinc:
	inc	rcx
	shr	rax, 1
	cmp	rcx, bitcount
	jl	.loop

	inc	qword [totalrecs]
	jmp	.line
.done:
	ret

bitcount	equ 12

	section .data
infile:		db 'input.txt', 0
filemode:	db 'r', 0
informat:	db `%s\n`, 0
decformat:	db `%d\n`, 0
binformat:	db `%b\n`, 0
file:		dq 0
poscounts:	times bitcount dq 0
totalrecs:	dq 0

	section .bss
numbuffer:	resb 4096
num:		resq 1

