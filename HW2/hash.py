def counter(file_name, word_list_and_counts):
    inputfile = open(file_name, 'r')#唯讀
    line = inputfile.readline().rstrip()#切割行數
    # 若檔案非空
    while line != '':
        # 將沒有出現在字典裡的字預設為0
        word_list_and_counts.setdefault(line, 0)
        # 已存在的字直接加1
        word_list_and_counts[line] += 1
        # 換讀下一行
        line = inputfile.readline().rstrip()

    # 計算不同字的個數
    word_count = len(word_list_and_counts)
    return word_count, word_list_and_counts

#印出結果
def print_results(word_count, word_list_and_counts):
    print('總共有{}個不重複的英文字'.format(word_count))
    print('每一個英文字出現次數:')
    for word, count in word_list_and_counts.items():
        print(word, count)


def main():
    # 建立一個字典
    my_dict = {}
    # 讀檔案並將結果紀錄在 result 中
    result = counter('hw2_data.txt', my_dict)
    # 印出結果
    print_results(result[0], result[1])

if __name__ == "__main__":
    main()
