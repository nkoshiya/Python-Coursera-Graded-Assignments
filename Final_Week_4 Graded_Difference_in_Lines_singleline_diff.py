def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    position = 0
    if line1 == line2:
        return -1
    else:
        if len(line1) < len(line2):
            for index in range(len(line2)):
                try:
                    if line1[index] != line2[index]:
                        position = index
                        break
                except IndexError:
                    position = len(line2) - 1
        elif len(line2) < len(line1):
            for index in range(len(line1)):
                try:
                    if line2[index] != line1[index]:
                        position = index
                        break
                except IndexError:
                    position = len(line1) - 1
        elif len(line2) == len(line1):
            for index in range(len(line2)):
                if line2[index] != line1[index]:
                    position = index
                    break
    return position


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    if len(line1.splitlines()) > 1 or len(line2.splitlines()) > 1:
        return ""
    else:
        output = ''
        output += line1 + '\n'
        index = 0
        try:
            idx_1 = int(idx)
            if idx_1 < 0 or idx_1 > len(line2) or idx_1 > len(line1):
                raise ValueError
        except (TypeError, ValueError):
            return ""
        while index < idx:
            output += "="
            index += 1
        output += "^" + '\n'
        output += line2 + '\n'
    return output


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    position = 0
    line = 0
    if lines2 == lines1:
        return -1, -1
    else:
        for index in range(max(len(lines1), len(lines2))):
            try:
                position = singleline_diff(lines1[index], lines2[index])
            except IndexError:
                position = 0
            if position == -1:
                continue
            line = index
            break
    return line, position


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_of_lines = []
    with open(filename, 'r') as file:
        for line in file:
            list_of_lines.append(line.strip())
    return list_of_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    line_1 = get_file_lines(filename1)
    line_2 = get_file_lines(filename2)
    line_number, index = multiline_diff(line_1, line_2)
    output_1 = f'Line {line_number}:'
    output = ""
    try:
        if line_number < 0 or line_number > max(len(line_1), len(line_2)):
            raise IndexError
        try:
            output = singleline_diff_format(line_1[line_number], line_2[line_number], index)
        except IndexError:
            output = singleline_diff_format(line_1[line_number], "", index)
    except IndexError:
        output_1 = 'No differences'

    final = output_1 + '\n' + output
    return final
