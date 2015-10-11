
# VARIABLES
word_file_name = 'words20000.txt'
output_html_file = 'templates/page.html'
input_file = 'input.txt'

threshold1 = 100
threshold2 = 1000
threshold3 = 7500
word_list_size = 20000

common_font_size = 2.5
uncommon_font_size = 3
rare_font_size = 4
somewhat_rare_font_size = 4.5
super_rare_font_size = 5

# OTHER VARIABLES - DO NOT CHANGE

word_list = []

html_code = ""
valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"

# VARIABLES




# Word list cleanup functions
def collapse_double_list(double_list):
    new_list = []
    for x in double_list:
        new_list = new_list + x
    return new_list

def filter_word(word):
    new_word = word
    if '\n' in word:
        new_word = new_word.replace("\n", "")
    if ' ' in word:
        new_word = new_word.replace(" ", "")
    return new_word

def cleanup_non_words(unfiltered):
    filter_out = [None, '']
    return [x for x in unfiltered if x not in filter_out]

def make_lower(unfiltered):
    return [s.lower() for s in unfiltered]


def write_html_for_word(word):
    global html_code
    check_word = word.lower()
    index_list = [i for i,x in enumerate(word_list) if x == check_word]
    if not bool(index_list): # if no index is found
        html_code = html_code + '<font size="' + str(super_rare_font_size) + '">' + word + "</font>"
    else:
        index = index_list[0]
        if index in range(0,threshold1):
            html_code = html_code + '<font size="' + str(common_font_size) + '">' + word + "</font>"
        elif index in range(threshold1,threshold2):
            html_code = html_code + '<font size="' + str(uncommon_font_size) + '">' + word + "</font>"
        elif index in range(threshold2,threshold3):
            html_code = html_code + '<font size="' + str(rare_font_size) + '">' + word + "</font>"
        elif index in range(threshold3,word_list_size):
            html_code = html_code + '<font size="' + str(rare_font_size) + '">' + word + "</font>"


def main():
    global valid_chars, html_code, word_list, word_file_name, output_html_file, input_file, threshold1, threshold2, threshold3, word_list_size, common_font_size, uncommon_font_size, rare_font_size, somewhat_rare_font_size, super_rare_font_size

    word_file = open(word_file_name, 'r')
    raw_word_list = [line.split(',') for line in word_file.readlines()]
    raw_word_list = collapse_double_list(raw_word_list)
    raw_word_list = [ filter_word(word) for word in raw_word_list ]
    raw_word_list = cleanup_non_words(raw_word_list)
    word_list = make_lower(raw_word_list)

    paragraph_file = open(input_file, 'r')
    paragraph = paragraph_file.readline()

    current_build = ""
    for i in range(0, len(paragraph)):
        if paragraph[i] in valid_chars:
            current_build = current_build + paragraph[i]
        elif paragraph[i] == ' ':
            write_html_for_word(current_build)
            html_code = html_code + '<font size="' + str(super_rare_font_size) + '"> </font>'
            current_build = ""
        else:
            write_html_for_word(current_build)
            html_code = html_code + paragraph[i]
            current_build = ""

    #Generate an HTML page
    first_half = "<html><head><link href='../static/styles.css' rel='stylesheet'><title>Converted Text</title></head><body id='convertedbody'><p>"
    second_half = "</body></html>"

    return first_half + html_code + second_half





#UNUSED
# write the html_code string to a file
#output_file = open("output.txt", "w")
#output_file.truncate()
#output_file.write(html_code)

#print(html_code)
