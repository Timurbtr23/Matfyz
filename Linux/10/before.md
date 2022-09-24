# Before class quiz (#10)

The quiz has to be submitted to your GitLab project before your lab starts.

Every question is worth 25 points.

Insert your answer inside the marked block (replace the ellipsis).



## Question Q1

Write here a short feedback about last lab. What was the most
interesting part or what was the most difficult part or any other
thoughts related to the last lab. Please, answer reasonably.

Your answer: **[A1]** the most difficult is daemons. The most interesting is wrking with disks **[/A1]**



## Question Q2

We have executed the following two commands (they both terminated
without any errors).

```
dd if=/dev/zero of=disk.img bs=1024 count=$(( 512 * 64 ))
mkfs.fat disk.img
```

Select which of the statements below _best_ describes what we have
performed. Feel free to use manual pages or even try the commands
yourself (then also consider using file type identification
utility `file(1)`).

1. We have deleted file `disk.img` in the current directory.
2. We have created an empty file full of zeros.
3. We have created an empty disk image and then initialized it
   with a FAT filesystem.
4. We have created a FAT filesystem on file `/dev/zero`.
5. We have copied 64 MB of photos from a camera mounted
   under `/dev/zero`.

Your answer: **[A2]** 4 **[/A2]**



## Question Q3

Look at the following fragment of pseudo-Python code of a simple
service.

```python
def on_signal(signal_number, frame_info):
    if signal_number == signal.SIGTERM:
        terminate = True
        signal_received = True
    elif signal_number == signal.SIGHUP:
        signal_received = True
    else:
        raise Exception("Unexpected signal")

def init():
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGHUP, on_signal)
    # No other signals are handled (i.e. they keep the default
    # implementation)

    with open('./service.pid', 'w') as f:
        f.write(os.getpid())

def main():
    init()
    while not terminate:
        load_configuration()
        signal_received = False
        for req in get_requests():
            handle_request(req)
            if signal_received:
                break
    cleanup()
```

Select _all_ statements that are correct.

1. Service will reload configuration after receiving SIGHUP signal.
2. Service will cleanly terminate after receiving SIGTERM signal.
3. Service will cleanly terminate after receiving SIGINT signal.
4. There is no way how to let this service reload its configuration
   (apart from forceful shutdown and starting anew).
5. File `service.pid` will contain service process ID.
6. Command `kill -TERM $( cat service.pid )` will cleanly terminate
   the service.
7. Command `kill -HUP $( echo service.pid )` will tell the service to
   reload its configuration.
8. Request processing can be interrupted by a SIGTERM but the actual
   termination will happen only after current request is processed.

Your answer: **[A3]** 2 5 6 **[/A3]**



## Question Q4

Select _all_ correct statements about disk mounting.

1. Root filesystem `/` must be mounted first.
2. The volume mounted under `/home` must always be a local physical disk.
3. `/home` must be always mounted as a separate volume (partition).
4. `/proc` behaves like a normal filesystem but the contents of the
   files is not stored anywhere directly (i.e. the contents is
   created on-the-fly as needed).
5. Any user can unmount `/`.
6. There is virtually no difference whether user works with files
   mounted from a real drive or from a disk image.
Your answer: **[A4]** 2 3 6 **[/A4]**
number 1 no bcz /boot /efi must be first



