# Entry Point

from FizzBuzz import fizzBuzz
from palindrome import palindrome
from anagram import is_anagram
from bubble_sort import bubble_sort
from factorial import factorial_iterative
from factorial import factorial_recursive
from etl import etl_pipeline

def main():
    print(fizzBuzz(101))
    print("is 'level' palindrome? " + str(palindrome("level")))
    print("is 'rose' palindrome? " + str(palindrome("rose")))
    print("are 'listen' and 'silent' anagrams? " + str(is_anagram("listen", "silent")))
    print("are 'יהוה' and 'היוה' anagrams? " + str(is_anagram("יהוה", "היוה")))
    print("Bubble Sort([10,22,56,43,67,6,777]) = " + str(bubble_sort([10,22,56,43,67,6,777])))
    print("10! (Recursive) = " + str(factorial_recursive(10)))
    print("10! (Iterative) = " + str(factorial_iterative(10)))

    rawdata = "abgitz kryastn ngidksh btrtztg khkvtna iglpzk shkuxit brj shm kvd mlcto lolam vaed yahdvohnai"
    print("ETL Rawdata [" + rawdata  + "] \n ==> ETL Pipeline: " + str(etl_pipeline(rawdata)))

    rawdata = "אָ֑בְּגִ֣י־תֵּ֔ץ קָ֑רַע־שָׁ֔טַן נֶ֑גֶב־כָּ֔עַשׁ יִ֑תְגַּ֣ר־צַ֔ג בֶּֽטֶ֑נ־חַ֔קָּל שָֽׁקוֹ֑צִי־תֵּ֔ת עַ֑נְפַּ֣ע־צַ֔תּ"
    print("ETL Rawdata [" + rawdata + "] \n ==> ETL Pipeline: " + str(etl_pipeline(rawdata)))

if __name__ == "__main__":
    main()