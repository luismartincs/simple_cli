import sys

class CliParser(object):
    def __init__(self, argv):
        self.args = argv[1:]
        self.defaults = {"--parameter1": "no", "--parameter2": "Hello!"}
        self.options = []
        self.values = []
        self.parameters = {}
        self.__parse__()

    def to_bool(self, val):
        return True if val.lower() == "yes" else False

    def param(self, option=""):
        if option in self.parameters:
            return self.parameters[option]
        elif option in self.defaults:
            return self.defaults[option]
        else:
            raise ValueError("Unknown option %s" % option)

    def __parse__(self):
        if len(self.args) % 2 == 0:
            for i in range(len(self.args)):
                if (i + 1) % 2 == 0:
                    self.values.append(self.args[i])
                else:
                    self.options.append(self.args[i])

            self.parameters = dict(zip(self.options, self.values))

        else:
            raise ValueError("Missing value for options")


if __name__ == "__main__":

    cli = CliParser(sys.argv)

    bool_parameter = cli.to_bool(cli.param("--parameter1"))
    string_parameter = cli.param("--parameter2")

    print(bool_parameter)
    print(string_parameter)
