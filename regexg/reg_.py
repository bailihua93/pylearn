import re

# 从字符串起始位置开始匹配正则，成功返回结果，失败返回None
content = 'hello 1234567 World_this is Regex Demo'
result = re.match('^hello\s(\d+)\s\w{4}(.*?)', content)
print(result)
print(result.group())  # hello 123 4567 Worl    group()返回总的结果
print(result.group(1))  # hello 123 4567 Worl   group(n)返回小括号的结果
print(result.span())

# result = re.match('^hell.*(\d+)\s.*',content)
# print(result.group(1))  # 结果只有7     .*贪婪模式匹配尽量多的字符，

result = re.match('^hel.*?(\d+)\s.*Demo', content)
print(result.group(1))  # 结果只有7     .*非贪婪模式匹配尽量少的字符，后面没有正则的话，当前只匹配最初的匹配方式；
cs = 'abbbb'
result = re.match('ab+', cs)  #abbbb
result = re.match('ab+?', cs)  # ab  非贪婪模式，只会返回最少的匹配
print(result.group(1))
