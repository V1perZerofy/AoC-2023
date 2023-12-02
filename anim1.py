from blessed import Terminal
import time
import sys
import re

term = Terminal()

def readInput():
    with open("input/input1.txt") as f:
        lines = f.readlines()
        #remove \n
        lines = [x.strip() for x in lines]
        f.close()
    return lines

def main():
    # Starting values for the variables
    total = 181
    value = 33

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)

        try:                
                # Reprint the normal output
                endres = []
                for line in lines:
                    # Strip newline characters and any trailing whitespace
                    line = line.rstrip()
                    res = []
                    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
                    numerals = ["o\u001b[32;1m1\u001b[30me", "t\u001b[32;1m2\u001b[30mo", "t\u001b[32;1m3\u001b[30me",
                                "f\u001b[32;1m4\u001b[30mr", "f\u001b[32;1m5\u001b[30me", "s\u001b[32;1m6\u001b[30mx",
                                "s\u001b[32;1m7\u001b[30mn", "e\u001b[32;1m8\u001b[30mt", "n\u001b[32;1m9\u001b[30me"]
                    #line = re.sub(r'(\d)', "\u001b[32;1m" + r'\1' + "\u001b[30m", line)
                    for j in range(9):
                        total = sum(map(int, endres))
                        value = int(res[0] + res[-1] if res else '00')
                        variable1 = f"Total: {total}"
                        variable2 = f"Value: {value}"
                        print(term.move_xy(term.width - len(variable1), 0) + variable1)
                        print(term.move_xy(term.width - len(variable2), 1) + variable2)
                        line = re.sub(nums[j], numerals[j], line)
                        print(line)
                        time.sleep(0.001)  # Adjust the sleep time as needed for the animation effect
                    # Extract numbers from the final line
                    for j in line:
                        if j.isdigit():
                            res.append(j)
                    endres.append(res[0] + res[-1] if res else '00')
                    # Print the final result always on the same space
                    #formatted_sentence = f"{line.ljust(8)}{endres[-1]}"
                    #print("\r" + formatted_sentence, end="")
                    print("\n")  # Move to the next line after processing the current line

                # Sleep briefly to simulate time taken by program's main logic
                time.sleep(0.5)
        except KeyboardInterrupt:
            # Exit the program gracefully on a keyboard interrupt (Ctrl+C)
            pass

if __name__ == "__main__":
    lines = readInput()
    main()
