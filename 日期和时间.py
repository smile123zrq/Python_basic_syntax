import time     # 引入时间模块

# https://www.nowcoder.com/tutorial/10005/d7659dd371c24b8fb84e0ee54a745d82

ticks = time.time()     # 时间戳，每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
print(ticks)

# 获取当前时间
localtime = time.localtime((time.time()))
print(localtime)
# time.struct_time(tm_year=2022, tm_mon=4, tm_mday=11, tm_hour=20, tm_min=7, tm_sec=40, tm_wday=0, tm_yday=101, tm_isdst=0)

# 获取格式化时间
localtime1 = time.asctime(time.localtime(time.time()))
print('本地时间为：', localtime1)
# 本地时间为： Mon Apr 11 20:10:18 2022

# 格式化日期
# 格式化成2022-04-11 20:12:35形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 2022-04-11 20:12:35

# 格式化成Mon Apr 11 20:13:22 2022形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# Mon Apr 11 20:13:53 2022

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
# 1459175064.0

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

# 获取某月日历
import calendar
cal = calendar.month(2022, 4)
print(cal)
'''
     April 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
'''