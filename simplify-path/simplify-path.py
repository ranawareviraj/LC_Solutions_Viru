class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []

        # Process each token if its is not empty
        for token in tokens:
            if token:
                # If token is .. and there is directory onto stack pop last directory
                if token == "..":
                    if stack:
                        stack.pop()
                # If token is "." -> Ignore
                # Token is not "." or ".." -> push onto stack
                elif token != ".":
                    stack.append(token)
        
        # Build simplified_path from remaining directories/tokens in the Stack
        simplified_path = "/" + "/".join(stack)
        return simplified_path
        