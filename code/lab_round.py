def sig_index(n: float, digits: int = 1, one_more_digit: str = '1', decimals: int = 20) -> int:
    """
    Get index relative to the '.' to get specific significant digits of a number

    Parameters
    ----------
    n: float
        Number to be rounded
    digits: int = 1
        Number of significant digits
    one_more_digit: str = '1'
        Digits that if at the end of the rounded number require 1 additional significant digit
    decimals: int
        Max number of decimal to take into consideration when rounding

    Returns
    -------
    int
        Index relative to the '.' where to cut the number in order to have the right amount of significant digits
    """

    n_str = f'%.{decimals + digits}f' % n
    n_dot = n_str.index('.')
    n_cln = [digit for digit in n_str if digit != '.']

    # Cut the undesired digits
    removing_zeros = True
    digit_count = 0

    for i, digit in enumerate(n_cln):
        if digit == '0' and removing_zeros:
            continue

        removing_zeros = False

        digit_count += 1

        if digit_count == digits:
            if digit in one_more_digit:
                i += 1
                digit = n_cln[i]

            n_cut = i - n_dot + 1
            return n_cut

    raise Exception("Something went wrong")


def round_zeros(n: float, decimals: int) -> str:
    """
    Round a number to a specific decimal number preserving final zeros

    Parameters
    ----------
    n: float
        Number to be rounded
    decimals: int
        Index relative to the '.' where to round the number

    Returns
    -------
    str
        Number rounded (of type string in order to preserve final zeros)
    """
    
    if decimals <= 0:
        return str(int(round(n, decimals)))
    return f'{n:.{decimals}f}'


def round_sig(n: float, **kwargs):
    i = sig_index(n, **kwargs)
    n_fin = round_zeros(n, i)

    return n_fin


def round_measure(m: float, e: float, **kwargs) -> tuple[str, str]:
    i = sig_index(e, **kwargs)

    m_fin = round_zeros(m, i)
    e_fin = round_zeros(e, i)

    return m_fin, e_fin
