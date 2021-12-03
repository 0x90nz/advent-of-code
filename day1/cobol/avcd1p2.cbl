      * Advent of Code 2021 Day 1 challenge

       IDENTIFICATION DIVISION.
       PROGRAM-ID.      AVCD1P2.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT NUMBER-LIST ASSIGN TO 'input.txt' ORGANISATION IS LINE
                   SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  NUMBER-LIST.
       01  NUMBER-ENTRY                 PIC 9(4).

       WORKING-STORAGE SECTION.
       01 WS-NUMBER                     PIC 9(4)        VALUE 0.
       01 WS-PREV                       PIC 9(4)        VALUE 9999.
       01 WS-EOF                        PIC X.
       01 WS-CNT                        PIC 9(9)        VALUE 0.

       PROCEDURE DIVISION.
           OPEN INPUT NUMBER-LIST.
           PERFORM UNTIL WS-EOF = 'Y'
                   READ NUMBER-LIST INTO WS-NUMBER
                           AT END MOVE 'Y' TO WS-EOF
                           NOT AT END PERFORM PROCESS-READING
                   END-READ
           END-PERFORM.
           DISPLAY 'Number times increased: ', WS-CNT.
           CLOSE NUMBER-LIST.

       PROCESS-READING.
           IF WS-NUMBER > WS-PREV THEN
                   ADD 1 TO WS-CNT
           END-IF.
           MOVE WS-NUMBER TO WS-PREV.


