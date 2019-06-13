urldecode
=========

Very simple script for url encoding/decoding the standard input.

Usage
-----
```
Usage:  urldecode [-e|-h]
Options:
    -e: url encode", file=stderr)
    -h: see this help section", file=stderr)
```

Example:
```
$ echo "%22Hey%22" | urldecode
"Hey"
$ echo "%22Hey%22" | urldecode | urldecode -e
"%22Hey%22"
```

Usage with Vim
--------------
This can be used in vim to decode a file in place by typing:
```
:%! urldecode
```

If you want to only decode 1 line, select it in visual mode then:
```
:'<,'>%! urldecode
```

For encoding just use the `-e` flag with the same commands.
