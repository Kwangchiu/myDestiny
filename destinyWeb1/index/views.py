from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response
import argparse
import json
import collections

# Create your views here.
def index(request):
    years = range(1920, 2050)
    month = range(1, 19)
    day = range(1,38)
    
    return render(request, 'index.html', {"year":years, "month":month, "day":day})


        
    

def login(request):
    #获取出生日期以及生辰的信息变成json数据，主要怎么输出
    if request.method == "GET":
        result = {}
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        time = request.GET.get('time')
        result['year'] = year
        result['month'] = month
        result['day'] = day
        result['time'] = time

        return render(request,'index.html',{'field':result})
        #result = json.dumps(result)
        #return render(request, 'test.html', {'times': result})
        #return HttpResponse(result, content_type='application/json;charset=utf-8')
        #return JsonResponse(result, content_type='application/json;charset=utf-8', safe = False)
    

def test(request):
    if request.method == "GET":
       # result = {}
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        time = request.GET.get('time')

        import sxtwl
        lunar = sxtwl.Lunar()

        Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        gan5 = {"甲":"木", "乙":"木", "丙":"火", "丁":"火", "戊":"土", "己":"土", "庚":"金", "辛":"金", "壬":"水", "癸":"水"}
        Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
        numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
        jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
        ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
        rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]
        

        yangli = lunar.getDayBySolar(int(year), int(month), int(day))
        Gans = collections.namedtuple("Gans", "year month day time")
        gz = lunar.getShiGz(yangli.Lday2.tg, int(time))
        gans = Gans(year=Gan[yangli.Lyear2.tg], month=Gan[yangli.Lmonth2.tg], day=Gan[yangli.Lday2.tg], time=Gan[gz.tg])
        Lleap = "闰" if yangli.Lleap else ""
       
        htmlstr=" <div class=\"mdui-dialog-title\">待老夫掐指一算</div>\
                        <div name=times class=\"mdui-dialog-content\">"       
        
        htmlstr+="公历：{}年{}月{}日<br>".format(year, month, day)
        htmlstr+="农历：\t{}年{}{}月{}日".format(yangli.Lyear0 + 1984, Lleap, ymc[yangli.Lmc], rmc[yangli.Ldi])
        gz1 = lunar.getShiGz(int(day),  int(time))
        htmlstr+="<br>八字：{}-{}年  {}-{}月  {}-{}日  {}-{}时".format(Gan[yangli.Lyear2.tg], Zhi[yangli.Lyear2.dz], Gan[yangli.Lmonth2.tg], Zhi[yangli.Lmonth2.dz], \
          Gan[yangli.Lday2.tg], Zhi[yangli.Lday2.dz], Gan[gz1.tg], Zhi[gz1.dz])

        '''print("test:\n")
        gz1 = lunar.getShiGz(int(day),  int(time))  #第一个参数为生日的日天干,参数二为出生的时间(小时)
        print(Gan[gz1.tg], Zhi[gz1.dz])
        print(Gan[yangli.Lyear2.tg], Zhi[yangli.Lyear2.dz], "年", Gan[yangli.Lmonth2.tg], Zhi[yangli.Lmonth2.dz], "月",\
          Gan[yangli.Lday2.tg], Zhi[yangli.Lday2.dz], "日")'''

        htmlstr+="</div>\
                        <div class=\"mdui-dialog-actions\">\
                            <button class=\"mdui-btn mdui-ripple\" onclick=\"window.inst.close();\">确定</button>\
                            <button class=\"mdui-btn mdui-ripple\" onclick=\"window.inst.close();\">取消</button>\
                        </div>"
    
        

        
        '''
        result['year'] = year
        result['month'] = month
        result['day'] = day
        result['time'] = time
        

        result = json.dumps(result)
        #return HttpResponse(result, content_type='application/json;charset=utf-8')
        '''
        return HttpResponse(htmlstr,content_type='text/html; charset=utf-8')
       

