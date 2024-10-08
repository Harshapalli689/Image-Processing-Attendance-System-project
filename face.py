def number_to_words(n):
    # Define word representations for numbers 0 to 19
    words = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    # Define word representations for tens multiples
    tens_words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    # Define word representations for large numbers
    large_words = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']
    # Initialize result string
    result = ''
    # Convert number to string
    str_n = str(n)
    # Reverse string to start from the rightmost digit
    str_n = str_n[::-1]
    # Split string into groups of three digits each
    groups = [str_n[i:i+3][::-1] for i in range(0, len(str_n), 3)]
    # Convert each group to words and append large number words as appropriate
    for i, group in enumerate(groups):
        # Convert hundreds digit to words
        if len(group) > 2 and int(group[2]) != 0:
            result = words[int(group[2])]+ result
        # Convert tens and units digits to words

        if len(group) > 1:
            if int(group[1]) == 1:
                result = words[int(group[1:])] + ' ' + result
            else:
                if int(group[1]) != 0:
                    result = tens_words[int(group[1])] + ' ' + result
                if int(group[0]) != 0:
                    result = words[int(group[0])] + ' hundred ' + result
        else:
            if int(group[0]) != 0 and len(group)==3:
                result =words[int(group[0])] + ' ' + result
        # Append large number words as appropriate
        if i > 0 and int(group) != 0:
            result = large_words[i] + ' ' + result
    # Return result string
    return result.strip() or 'zero'

n=int(input())
print(number_to_words(n))
