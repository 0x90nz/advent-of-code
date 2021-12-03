       IDENTIFICATION DIVISION.
       PROGRAM-ID.    AVCD2P1.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       SELECT INST-LIST ASSIGN TO 'inst.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  INST-LIST.
       01  INST-LINE                    PIC X(80).

       WORKING-STORAGE SECTION.
       01  WS-EOF                       PIC X.
       01  WS-VERT                      PIC S9(9).
       01  WS-HORIZ                     PIC S9(9).
       01  WS-LINE                      PIC X(80).
       01  WS-INSTRUCTION.
           05  WS-DIRECTION             PIC X(10).
           05  WS-AMOUNT                PIC 9(9).


       PROCEDURE DIVISION.
           OPEN INPUT INST-LIST.
           PERFORM UNTIL WS-EOF = 'Y'
                READ INST-LIST INTO WS-LINE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END PERFORM PROCESS-LINE
                END-READ
           END-PERFORM.
           CLOSE INST-LIST.
           DISPLAY 'HORIZ: ', WS-HORIZ, ' VERT: ', WS-VERT.

        PROCESS-LINE.
           UNSTRING WS-LINE
           DELIMITED BY SPACES
           INTO WS-DIRECTION WS-AMOUNT.
           EVALUATE WS-DIRECTION
                   WHEN 'forward   '
                           ADD WS-AMOUNT TO WS-HORIZ
                   WHEN 'down      '
                           ADD WS-AMOUNT TO WS-VERT
                   WHEN 'up        '
                           SUBTRACT WS-AMOUNT FROM WS-VERT
           END-EVALUATE.



