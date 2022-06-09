## Simple Cli

If you dont want to install additional modules to parse your command line arguments, just copy and pase the CliParser class and start working with your scripts.

### Usage

Invoke your main script with

```shell
python main.py --parameter1 yes --parameter2 Bye!
```

In your main file you can use your parameters with

```python
if __name__ == "__main__":
    cli = CliParser(sys.argv)
    print(cli.to_bool(cli.param("--parameter1")))
    print(cli.param("--parameter2"))
```

The script returns

```shell
True
Bye!
```

You can define default values in

```python
class CliParser(object):
    def __init__(self, argv):
        self.args = argv[1:]
        self.defaults = {"--parameter1": "no", "--parameter2": "Hello!"}
```

If you invoke the script

```shell
python main.py
```

The script returns

```shell
False
Hello!
```