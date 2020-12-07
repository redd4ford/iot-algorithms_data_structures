"""Custom finite-state machine implementation."""


class FiniteStateMachine:
    """
    custom finite-state machine implementation.
    a finite-state machine is a model which contains a finite number
    of states. for this problem, the states store characters of a pattern
    and are used to check each symbol in a string to find a matching
    substring.
    """

    def __init__(self):
        self.states = dict()
        self.states[0] = None
        self.curr_state_idx = 0

    def fill_states(self, pattern) -> None:
        """
        add states and set their values as each character of the pattern.
        :param pattern: a pattern to match
        :return: none
        >>> test = FiniteStateMachine()
        >>> test.fill_states('test')
        >>> print(test.states[0])
        None
        >>> print(test.states[1])
        t
        """
        for pattern_idx in range(1, len(pattern) + 1):
            self.states[pattern_idx] = pattern[pattern_idx - 1]

    def is_curr_trailing(self) -> bool:
        """
        check if the current state is the last (trailing) one.
        :return: True if the current state really is the trailing one,
        False if it is not
        >>> test = FiniteStateMachine()
        >>> test.fill_states('test')
        >>> test.curr_state_idx = 0
        >>> test.is_curr_trailing()
        False
        >>> test.curr_state_idx = 4
        >>> test.is_curr_trailing()
        True
        """
        return self.curr_state_idx == len(self.states) - 1

    def is_next_matching(self, symbol: str) -> bool:
        """
        check if a symbol matches the next state's value.
        :param symbol: a character to be checked
        :return: True if the symbol equals to the next state, False if it
        does not
        >>> test = FiniteStateMachine()
        >>> test.fill_states('test')
        >>> test.curr_state_idx = 0
        >>> test.is_next_matching('e')
        False
        >>> test.is_next_matching('t')
        True
        """
        return self.states[self.curr_state_idx + 1] == symbol
