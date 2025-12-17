class Solution:
    def interpret(self, command: str) -> str:
        parser = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                parser.append("G")
                i += 1
            elif command[i:i + 2] == "()":
                parser.append("o")
                i += 2
            elif command[i:i+4] == "(al)":
                parser.append("al")
                i += 4
        return "".join(parser)
       
