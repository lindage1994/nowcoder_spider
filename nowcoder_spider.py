import requests
import time
from lxml import etree

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
#/html/body/div[1]/div[2]/div[2]/div[2]/div[1]
f = open('./JavaPros.md','a+')
def get_info(url,n):
    res = requests.get(url, headers=header)
    selector = etree.HTML(res.text)
    question = '##### '+str(n)+'、'+selector.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/text()')[0].lstrip('\n')+'\n'
    answer = selector.xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]//text()')
    answer = "".join(answer)
    answer = '```\n'+answer.lstrip('\n')+'\n```\n'
    f.write(question.replace(u'\xa0', u'')+answer.replace(u'\xa0', u''))



if __name__ == '__main__':
    urls = ['https://www.nowcoder.com/ta/review-java/review?query=&asc=true&order=&page={}'.format(str(i)) for i in range(1,121)]

    i = 1;
    for url in urls:
        print(url)
        get_info(url,i)
        i = i + 1
        time.sleep(1)

f.close()