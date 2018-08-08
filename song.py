#!/usr/bin/env python3
"""Print out bottles of beer on the wall lyrics."""
import sys


def main(usr_args):
    """Pass valid interger to bottles_song."""
    counter = arg_int_check(usr_args)
    bottles_song(counter)
    return 0


def arg_int_check(usr_args):
    """Check first cmdline argument and return an interger."""
    warn_msg = "Must enter an int >= 1 or an int <= 99.\n"
    if len(usr_args) >= 2 and usr_args[1].isdecimal():
        usr_num = int(usr_args[1])
        if usr_num <= 99 and usr_num >= 1:
            return usr_num
        else:
            print(warn_msg)
            return 99
    elif len(usr_args) == 1:
        return 99
    else:
        print(warn_msg)
        return 99


def bottles_song(counter):
    """Print out bottles of beer verses"""
    # Lines 3 and 4 are the same no matter what verse in the song. Assigning
    # them once is much better then assigning them over and over again
    # within the while loop.
    line3 = "Take one down"
    line4 = "And pass it around"
    while counter:
        if counter > 1:
            int_as_word = int_to_word(counter)
            line1 = "{0} bottles of beer on the wall!".format(int_as_word)
            line2 = "{0} bottles of beer!".format(int_as_word)
            counter -= 1
            int_as_word = int_to_word(counter)
            line5 = "{0} bottles of beer on the wall!".format(int_as_word)
            # The following if statement will catch the switch in language
            # of bottles to bottle.
            if counter == 1:
                line5 = "{0} bottle of beer on the wall!".format(
                    int_as_word)
        else:
            int_as_word = int_to_word(counter)
            counter, line1, line2, line5 = last_verse(counter, int_as_word)
        verse = "{0}\n{1}\n{2}\n{3}\n{4}\n".format(line1, line2, line3,
                                                   line4, line5)
        print(verse)
    return


def last_verse(counter, int_as_word):
    """Print out 1 bottle of beer verse."""
    line1 = "{0} bottle of beer on the wall!".format(int_as_word)
    line2 = "{0} bottle of beer!".format(int_as_word)
    counter -= 1
    line5 = "No more bottles of beer on the wall!"
    return counter, line1, line2, line5


def int_to_word(counter):
    """Return spelled-out form of intergers 1-99."""
    single_digit = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                    6: "six", 7: "seven", 8: "eight", 9: "nine"}
    double_digit = {2: "Twenty", 3: "Thirty", 4: "Fourty", 5: "Fifty",
                    6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
    tens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    if counter in range(1, 10):
        int_as_word = single_digit[counter]
        return int_as_word.title()
    elif counter in range(10, 20):
        int_as_word = tens[counter]
        return int_as_word
    elif counter in range(20, 100, 10):
        counter = counter // 10
        int_as_word = double_digit[counter]
        return int_as_word
    else:
        counter_str = str(counter)
        int_as_word = "{0}-{1}".format(double_digit[int(counter_str[0])],
                                       single_digit[int(counter_str[1])])
        return int_as_word


if __name__ == "__main__":
    main(sys.argv)
