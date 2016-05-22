比较原始的代码，架构不太合理。
整体思路：
登录
fill_major_page(): fill第一个专业表单，填验证码，跳转到指定专业页面
writeToFile(): 将当前页面存储
page_list.append(): 确定当前专业的总页数（有bug，没考虑最多只能装10页）
url存入url_list
driver.back()：浏览器后退

fill_page2: fill第二个专业表单，跳转到指定专业页面(不用验证码)
writeToFile(): 将当前页面存储
page_list.append(): 确定当前专业的总页数（有bug，没考虑最多只能装10页）
url存入url_list
driver.back():浏览器后退
fill_page2循环，直到遍历完major_list

遍历完：
find_more_page(): 
根据url_list、page_list构造url
driver.get(url)并保存html
