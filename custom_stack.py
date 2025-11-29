def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # Implement stack logic to validate parentheses
    stack = []

    # Map each closing bracket to its matching opening bracket
    matching = {")": "(", "]": "[", "}": "{"}
    openings = set(matching.values())

    for ch in s:
        # If it's an opening bracket, push onto the stack
        if ch in openings:
            stack.append(ch)

        # If it's a closing bracket, the top of the stack must match
        elif ch in matching:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    # Valid if no unmatched openings remain
    return len(stack) == 0
