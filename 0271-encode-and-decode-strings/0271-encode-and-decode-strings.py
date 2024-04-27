class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Append the length of the string, followed by '#' and then the string itself
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of the delimiter '#', which is just after the length of the next string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # The length of the next string
            # Add the string that starts just after '#' and has the specified length
            strs.append(s[j + 1:j + 1 + length])
            i = j + 1 + length  # Move the index to the start of the next string's length
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
