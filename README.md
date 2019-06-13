urld3c
======

Very simple script for url encoding/decoding the standard input.

Usage
-----
```
Usage: urld3c [-e|-h]
Options:
    -e: url encode
    -h: see this help section
```

Example:
```
$ echo "%22Hey%22" | urld3c
"Hey"
$ echo "%22Hey%22" | urld3c | urld3c -e
"%22Hey%22"
```

Usage with Vim
--------------
This can be used in vim to decode a file in place by typing:
```
:%! urld3c
```

If you want to only decode 1 line, select it in visual mode then:
```
:'<,'>%! urld3c
```

For encoding just use the `-e` flag with the same commands.
