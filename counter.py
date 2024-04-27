def char_count(string):
  char_dict = {}
  for char in string:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

string = "upflairs pvt ltd"
char_counts = char_count(string)

print(char_counts)
