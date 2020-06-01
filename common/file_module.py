# title = "Alice in Wonderland"
# title.split()
# #['Alice', 'in', 'Wonderland']
# print(title.split())

def count_words():
    # 统计一个文件里有多少个单词
    # filename = 'programe.txt'
    # ii="效验"
    try:
        with open(filename,encoding="utf-8") as f_obj:
            contents = f_obj.read()
            print(contents)
            print(type(contents))
    except:
        msg="sorry,the file " + filename +" does not exist."
        print(msg)
    else:
        # words=contents.split("效验")
        # num_words=len(words)
        # i="效验"
        words=contents.split()
        print(words)
        print(type(words))
        i='效验'
        num_words=contents.count(i)
        # for i in list(contents):
        #     print(i)
        #
        #     num_words=contents.count(i)

        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'programe.txt'
count_words()



# if __name__=="__main__":
#     filename = 'programe.txt'
#     count_words()