      * ---------------------------------------------------------------
      * Advent of Code Day 3 Part 1
      * ---------------------------------------------------------------
       IDENTIFICATION DIVISION.
       PROGRAM-ID.    AVCD3P1.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT IN-FILE ASSIGN TO 'input.txt'
                   ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  IN-FILE.
       01  IN-LINE                      PIC X(80).

       WORKING-STORAGE SECTION.
       01  WS-IDX                       PIC 9(9)     VALUE 0.
       01  WS-END-FLAG                  PIC X.
           88 WS-END                                 VALUE 'Y'.
       01  WS-LINE                      PIC X(80).
       01  WS-FREQ-TABLE.
           05 WS-SET-FREQ               PIC 9(12)    OCCURS 12 TIMES.
           05 WS-UNSET-FREQ             PIC 9(12)    OCCURS 12 TIMES.
       01  GAMMA-RATE                   PIC 9(12).
       01  EPSILON-RATE                 PIC 9(12).

       PROCEDURE DIVISION.
       MAINLINE SECTION.
           OPEN INPUT IN-FILE
           PERFORM UNTIL WS-END
                   READ IN-FILE INTO WS-LINE
                           AT END MOVE 'Y' TO WS-END-FLAG
                           NOT AT END PERFORM PROCESS-LINE
                   END-READ
           END-PERFORM
           CLOSE IN-FILE
           PERFORM CALC-RATES
           DISPLAY 'Gamma: ', GAMMA-RATE, ' Epsilon: ', EPSILON-RATE
           STOP RUN
           .

       PROCESS-LINE SECTION.
           MOVE 1 TO WS-IDX.
           PERFORM 12 TIMES
                   IF WS-LINE(WS-IDX:1) = '1' THEN
                           ADD 1 TO WS-SET-FREQ(WS-IDX)
                   ELSE
                           ADD 1 TO WS-UNSET-FREQ(WS-IDX)
                   END-IF
                   ADD 1 TO WS-IDX
           END-PERFORM
           .

       CALC-RATES SECTION.
           MOVE 1 TO WS-IDX
           PERFORM 12 TIMES
                   *> Really this could just be implemented with invert,
                   *> but I'm monumentally lazy rn
                   IF WS-SET-FREQ(WS-IDX) > WS-UNSET-FREQ(WS-IDX) THEN
                           MOVE 1 TO GAMMA-RATE(WS-IDX:1)
                           MOVE 0 TO EPSILON-RATE(WS-IDX:1)
                   ELSE
                           MOVE 0 TO GAMMA-RATE(WS-IDX:1)
                           MOVE 1 TO EPSILON-RATE(WS-IDX:1)
                   END-IF
                   ADD 1 TO WS-IDX
           END-PERFORM
           .

