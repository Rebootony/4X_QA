import jieba

class Question_handle:

    def testjieba(self,str):
        seg_list = jieba.cut(str, cut_all=True, HMM=False)
        print("Full Mode: " + "/ ".join(seg_list))  # 全模式

        #seg_list = jieba.cut(str, cut_all=False, HMM=True)
        #print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

        #seg_list = jieba.cut(str, HMM=False)
        #print(", ".join(seg_list))

        #seg_list = jieba.cut_for_search(str, HMM=False)  # 搜索引擎模式
        #print(", ".join(seg_list))

        # jieba.cut的默认参数只有三个,jieba源码如下
        # cut(self, sentence, cut_all=False, HMM=True)
        # 分别为:输入文本 是否为全模式分词 与是否开启HMM进行中文分词

if __name__ == '__main__':
  test = Question_handle()
  test.testjieba("如何查询文字识别服务调用次数")
