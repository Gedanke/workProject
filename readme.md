# readme

* 首先获取 [http://yss.mof.gov.cn/caizhengshuju/](http://yss.mof.gov.cn/caizhengshuju/) 下，一共四页的 url 
	* [http://yss.mof.gov.cn/caizhengshuju/index.htm](http://yss.mof.gov.cn/caizhengshuju/index.htm)
	* [http://yss.mof.gov.cn/caizhengshuju/index_1.htm](http://yss.mof.gov.cn/caizhengshuju/index_1.htm)
	* [http://yss.mof.gov.cn/caizhengshuju/index_2.htm](http://yss.mof.gov.cn/caizhengshuju/index_2.htm)
	* [http://yss.mof.gov.cn/caizhengshuju/index_3.htm](http://yss.mof.gov.cn/caizhengshuju/index_3.htm)
	* 需要注意的是，我们需要的是数据，带有三公字样的不需要考虑
* 得到所有年份的urlY后，进入每一个urlY，也要获取该urlY下的所有urlYY，大部分的url只有一页，为了方便，统一不翻页，多页的可以单独处理
	* 年份页的url，我们需要的是所有带“支”和“转移”字样的urlYY
	* 同样的，获取年份页下所有需要的urlYY
	* 需要按表格和报告处理对应的ulrYY
* 进入相应的urlYY，提取得到数据，写入excel中
