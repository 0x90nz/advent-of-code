\ Advent of Code Day 1 Part 1
\ Needs to be run with:
\ 	`cat input.txt | gforth avcd1p1.fth`

variable prev
variable counter

9999 prev !
0 counter !

: get-number ( -- n f )
	pad 40 accept
	pad swap s>number?
	>r d>s r> ;		\ convert double to single precision

: process-input ( -- )
	begin
		get-number
	while
		dup prev @ > if
			1 counter +!
		then
		prev !
	repeat ;

process-input
counter ?
bye

