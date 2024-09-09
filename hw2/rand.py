"""This module utilizes the subprocess.run function in order to generate
random arrays."""
import subprocess


def random_array(arr):
    """This function accepts an array of size n as a parameter,
    and uses the subprocess.run function in order to generate random integers between
    1 and 20 and fill the array with these random values."""
    print(arr)
    shuffled_num = None
    # for val in enumerate(arr):
    for i in range(len(arr)): 
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)  # val = 
    print(arr)
    return arr
