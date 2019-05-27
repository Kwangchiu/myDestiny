'''import datetime
import unittest
import pprint
def Get8Zi(nGreYear,nGreMonth,nGreDay,nHour,nMinute):
    (sShuxiang,sTianGan,sDiZhi,sNongliMonth,sNongliDay)=\
        GetLunarString(Gregorian2Lunar((nGreYear,nGreMonth,nGreDay)))
    nTianGan=((nGreYear-4)%60)%10
    #时辰    
    nShiCheng=nHour/2
    if nHour%2==1:#[a<=x<b)半开半闭 
	nShiCheng+=1
    if nShiCheng==12:
	nShiCheng=0
    #分钟
    nFeng=nMinute/10
    if nHour%2==0:
	nFeng+=6#1'分'含120分钟
    
    #年干支
    str_Year=sTianGan+sDiZhi
    #月干支 
    cListMonth=(
           #甲己	 乙庚	     丙辛     丁壬	     戊癸   
        (u"丙寅",u"戊寅",u"庚寅",u"壬寅",u"甲寅"),
        (u"丁卯",u"己卯",u"辛卯",u"癸卯",u"乙卯"),
        (u"戊辰",u"庚辰",u"壬辰",u"甲辰",u"丙辰"),
        (u"己巳",u"辛巳",u"癸巳",u"乙巳",u"丁巳"),
        (u"庚午",u"壬午",u"甲午",u"丙午",u"戊午"),
        (u"辛未",u"癸未",u"乙未",u"丁未",u"己未"),
        (u"壬申",u"甲申",u"丙申",u"戊申",u"庚申"),
	(u"癸酉",u"乙酉",u"丁酉",u"己酉",u"辛酉"),
	(u"甲戌",u"丙戌",u"戊戌",u"庚戌",u"壬戌"),
	(u"乙亥",u"丁亥",u"己亥",u"辛亥",u"癸亥"),
	(u"丙子",u"戊子",u"庚子",u"壬子",u"甲子"),
	(u"丁丑",u"己丑",u"辛丑",u"癸丑",u"乙丑")    
    )
    # 天干名称
    cTianGan=(u"甲",u"乙",u"丙",u"丁",u"戊",u"己",u"庚",u"辛",u"壬",u"癸")
    #地支名称
    cDizhi=(u"子",u"丑",u"寅",u"卯",u"辰",u"巳",u"午",u"未",u"申",u"酉",u"戌",u"亥")
    
    (sFeast,nFeastMonth)=Get24LunarFeast((nGreYear,nGreMonth,nGreDay))
    nMonth=nFeastMonth #二十四节气定年月支
    if nGreMonth==12:
        if nFeastMonth==13:
            nMonth=1
            for nTG in range(0,10):
                if sTianGan==cTianGan[nTG]:
                    sTianGan=cTianGan[(nTG-1)%10]
                    break
            for nDZ in range(0,12):
                if sDiZhi==cDizhi[nDZ]:
                    sDiZhi=cDizhi[(nDZ-1)%12]
                    break
        if nFeastMonth==13:
            nMonth=1
            
    if nTianGan>=5:
        nTianGan-=5
    str_Month=cListMonth[nMonth-1][nTianGan]
    #日干支  
    #1.求元旦干支 以阳历日期来求  
    nGongYuanYear=nGreYear%100#公元纪年的最后两位 
    if nGongYuanYear==0:
	nGongYuanYear=100#百年逢百
    nA=(nGongYuanYear%12)*5
    nB=int(nGongYuanYear/4)
    if not nGongYuanYear%4==0:
        nB=nB+1
    nYuanDanGanZHi=nA+nB
    #2.查表 以cListMonth排列
    #1901～2000年间以甲戌作1向后推某年C的值，既是该年元旦的干支﹙2001～2100年间以己未作1﹚
    nGongYuan=nGreYear
    nX=int(nYuanDanGanZHi/12)%5
    nY=nYuanDanGanZHi%12
    if nGongYuan>2000:
        nX=(nX+4)%5
        if nY+5>12:nX=(nX+1)%5
        nY=(nY+4)%12
    if nGongYuan<=2000:
        if nY+8>12:nX=(nX+1)%5
        nY=(nY+7)%12
    str_YuanDanDay=cListMonth[nY][nX]
    #3.求当日干支
    nDayGan,nDayZhi=0,0
    for n in range(0,10):
        if str_YuanDanDay[:1]==cTianGan[n]:#C源码中文为两个字节，Python为一个
            nDayGan=n
            break
    for k in range(0,12):
        if str_YuanDanDay[1:]==cDizhi[k]:
            nDayZhi=k
            break
    
	#诗诀 
	# 一月干支均减１    二月干加０支加６   三月干减二支加10 
	# 四月干减１支加５  五月干支均减１     六月干加０支加６ 
	# 七月干支均加０    八月干加１支加７   九月干支均加２ 　
	# 十月干加２支加８  十一月干支均加３ 　十二月干加３支加９
    nGanRun,nZhiRun=0,0
    if nGreMonth==1:
	nGanRun=nGanRun-1;nZhiRun=nZhiRun-1
    elif nGreMonth==2:
	nZhiRun=nZhiRun+6
    elif nGreMonth==3:
	nGanRun=nGanRun-2;nZhiRun=nZhiRun+10
    elif nGreMonth==4:
	nGanRun=nGanRun-1;nZhiRun=nZhiRun+5
    elif nGreMonth==5:
	nGanRun=nGanRun-1;nZhiRun=nZhiRun-1
    elif nGreMonth==6:
	nZhiRun+=6
    elif nGreMonth==8:
	nGanRun+=1;nZhiRun+=7
    elif nGreMonth==9:
	nGanRun+=2;nZhiRun+=2
    elif nGreMonth==10:
	nGanRun+=2;nZhiRun+=8
    elif nGreMonth==11:
	nGanRun+=3;nZhiRun+=3
    elif nGreMonth==12:
	nGanRun+=3;nZhiRun+=9
	
    nRunYear=0
    #四年一闰,百年不闰,四百年再闰
    if (nGreYear%400==0) or (not nGreYear%100==0) and (nGreYear%4==0):
	if nGreMonth>2:
	    nRunYear+=1
    # (nDayGan）+（nDay）+（所求月的天干加减数、闰年三月以后减1）÷10
    nTodayGan=(nDayGan+nGreDay+nGanRun+nRunYear)%10
    #（所求年份的元旦地支）+（所求日期）+（所求月的地支加减数、闰年三月以后减1）÷12
    nTodayZhi=(nDayZhi+nGreDay+nZhiRun+nRunYear)%12
    str_TodayGan=cTianGan[nTodayGan]
    str_TodayZhi=cDizhi[nTodayZhi]
    str_Day=str_TodayGan+str_TodayZhi
    #//时干支
    cListTime=(
              #甲己	     乙庚	 丙辛      丁壬	  戊癸   
            (u"甲子",u"丙子",u"戊子",u"庚子",u"壬子"),
            (u"乙丑",u"丁丑",u"己丑",u"辛丑",u"癸丑"),
            (u"丙寅",u"戊寅",u"庚寅",u"壬寅",u"甲寅"),
            (u"丁卯",u"己卯",u"辛卯",u"癸卯",u"乙卯"),
            (u"戊辰",u"庚辰",u"壬辰",u"甲辰",u"丙辰"),
            (u"己巳",u"辛巳",u"癸巳",u"乙巳",u"丁巳"),
            (u"庚午",u"壬午",u"甲午",u"丙午",u"戊午"),
            (u"辛未",u"癸未",u"乙未",u"丁未",u"己未"),
            (u"壬申",u"甲申",u"丙申",u"戊申",u"庚申"),
            (u"癸酉",u"乙酉",u"丁酉",u"己酉",u"辛酉"),
            (u"甲戌",u"丙戌",u"戊戌",u"庚戌",u"壬戌"),
            (u"乙亥",u"丁亥",u"己亥",u"辛亥",u"癸亥")
	);   
    str_Time=cListTime[nShiCheng][nTodayGan%5]
    #考刻分 时上起刻
    nTimeGan=0
    for j in range(0,10):
	if str_Time[:1]==cTianGan[j]:
	    nTimeGan=j
	    break
    str_Minute=cListTime[nFeng][nTimeGan%5]
    
    #四柱 + 考时   十字
    return str_Year,str_Month,str_Day,str_Time,str_Minute
    
    
    
       
       
class FuncTestCase(unittest.TestCase):
    def testGet8Zi(self):
	self.assertEqual(Get8Zi((2012,5,4,0,0)),(u'壬辰',u'甲辰',u'乙丑',u'丙子',u'甲午'))
	#0时0分应为子时午分

if __name__=='__main__':
    #print Gregorian2Lunar('2012-1-3')
    #print Lunar2Gregorian('2013-4-10')
    #print GetLunarString(2013, 5, 26, False)
   # print  Get24LunarFeast((2013,5,4))
    print Get8Zi((2012,5,4,0,0))
'''

