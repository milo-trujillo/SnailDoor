# SnailDoor!

*The socketless backdoor with a bandwidth of roughly one byte per second!*

## Objective

SnailDoor provides a (very slow) backdoor when you are unable to create sockets on the remote machine (for sending or receiving), but a web server is running and you can host static files.

## How

SnailDoor creates a file for every possible byte, then polls those files regularly, looking for a change in access time. When a client requests one of the byte-files this updates the access time, and SnailDoor reads in the appropriate byte.

When SnailDoor reads a newline it executes the command now in its buffer, and saves the results to another hosted file (output.txt).

Tada! You have a painfully slow remote shell!
