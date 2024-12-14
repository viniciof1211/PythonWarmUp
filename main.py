# Entry Point -  it's dynamically typed (Python)

from examples.challenges import fizzBuzz
from examples.challenges import palindrome
from examples.challenges import is_anagram
from examples.challenges import bubble_sort
from examples.challenges import factorial_iterative
from examples.challenges import factorial_recursive
from examples.challenges import etl_pipeline

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