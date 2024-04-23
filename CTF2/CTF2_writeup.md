# CS2107 Assignment CTF2

Lu Bingyuan Axxxx353X

## Easy

### E1 can_you_gdb 10 points

Using GDB, the binary was disassembled. In the main function, a comparison was done iteratively with the input string and the flag string. By setting a breakpoint at the comparison, the flag was obtained segment by segment by examining the register. After concatenating the segments, the flag obtained was: `CS2107{y4y_y0u_c4n_us3_4_d3bugger!GDB_my_best13}`

### E2 keylogger 10 points

WireShark was used to open the capture file, the relevant capture data of USB was downloaded as a json file as in `e2data.json`. Using HID tables of keyboard data, a table of hex value mappings to key presses was created as in `keyd.py`. By examining the keypress data which were in 8 bytes, it can be derived that the first byte was the modifier key and subsequent bytes were keypresses. This logic was applied in `e2_decode.py` to obtain the flag in the output.

flag: `CS2107{K3YL0GGER_1S_@CTIVATED}`

### E3 babypwn 10 points

_Not attempted_

### E4 cat facts 10 points

This challenge involves SQL injection. From `setup.py`, it can be observed that the flag was stored in a separate table in the database from the cat facts.
Thus, to first find the table name containing the flag, a query to sqlmaster was made to find the table names.
The query was `SELECT name FROM sqlite_master WHERE type='table'`. The table name obtained was "flags". Then, the query to obtain the flag was made such that it will not obtain any row from the cat facts table and only from the flags table. The query was then `'UNION SELECT id, flag FROM flags`.

## Medium

### M3 cat breeds

This challenge involves (blind) SQL injection as there is no explicit display of information on the flag on the HTML page. The flag is stored in a table in the database.
Since the HTML page displays a quote letting the user know where cat breed exists, this true/false mechanism was exploited to reveal whether query to the flag database was successful.

Refer to `injection.py`, a script to bruteforce queries to the database to obtain the flag. Firstly, the length of the flag was obtained by iterating through 0 to 100 (arbitrary limit) until a successful query of LENGTH(flag) was made. Using this length, the flag was obtained character at a time by iterating through the ASCII characters until the next appropriate character was found for the prefix of the flag.

flag: `CS2107{bL1nd_1s_n0t_4_Pr0BL3m_f0R_ThE_m1gHtY_Sqli_mASTeR}`

### Appendix

Aside from the hints provided in the CTF, I also referenced this [video](https://www.youtube.com/watch?v=1Qs195_8hNw) for Blind SQL Injection.

It is regrettable that I could not complete the remaining challenges due to other commitments but I am glad to have learnt multiple new techniques through the completion of the challenges.
