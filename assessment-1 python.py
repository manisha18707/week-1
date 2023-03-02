#reverse substrings in a paragraph using recursion in python
def reverse_para(para):
    if not para:
        return " "
    else:
        words = para.split(" ")
        first_word = words[0]
        rest_of_para = " ".join(words[1:])
        reversed_word = first_word[::-1]
        return reversed_word + " " + reverse_para(rest_of_para)
para= input()
output= reverse_para(para)
print(output)



#reverse of substrings in a paragraph using multithreading in python
import concurrent.futures
def reverse_paragraph(paragraph):
    words = paragraph.split()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(reverse_word, word) for word in words]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return ' '.join(results)
def reverse_word(word):
    return word[::-1]
if __name__ == '__main__':
    input_paragraph = input()
    output_paragraph = reverse_paragraph(input_paragraph)
    print(output_paragraph)
