
newl = []

# for i in range(len(lis)):

#     if(lis[i] == 9 or lis[i] == 11 or lis[i] == 10):
#         newl.append(10)

#     elif lis[i] == 18 or lis[i] == 19 or lis[i] == 21 or lis[i] == 20 or lis[i] == 22:
#         newl.append(20)
    

#     elif(lis[i] % 6 >= 3):
        
#         newl.append((lis[i] // 6 ) * 6 + 6)


#     else:
#         newl.append((lis[i] // 6 ) * 6)


# print(newl)

from random import *

# lis = [565,622,635,688,653,689,703,637,666,636,715,691,626,680,621,732,324,157,346,298,513,334,321,324,1036,155,695,176,161,344,164,304,172,345,324,504,319,296,338,319,180,161,172,480,306,173,167,179,328,169,737,297,172,155,325,333,334,333,323,161,339,380,710,143,179,325,164,316,148,350,329,503,332,317,310,1015,184,1172,320,310,165,366,343,523,314,332,292,327,163,361,365,684,156,168,343,138,332,163,346,323,528,317,307,337,665,656,652,693,162,150,173,349,347,457,174,351,160,179,161,332,171,336,377,632,168,167,152,169,176,526,163,178,147,158,182,341,178,168,171,305,496,947,128,268,154,347,154,162,177,330,163,157,302,353,277,188,171,187,327,181,325,201,180,184,330,184,630,347,325,328,171,174,176,312,163,324,184,180,175,283,189,694,682,633,622,414,281,332,285,339,342,344,363,3,160,182,171,182,161,188,2,179,151,2,170,158,149,7,171,169,150,2,146,149,8,164,153,167,139,146,201,165,167,171,170,165,149,179,169,165,168,162,178,165,179,175,190,174,144,175,180,179,162,172,165,170,185,316,150,161,164,165,167,155,641,345,331,534,460,380,341,192,304,465,996,173,180,417,568,361,309,168,349,515,1650,295,322,354,302,335,350,1337,339,498,494,343,1058,311,318,309,324,341,316,168,1241,293,323,322,360,144,361,325,476,338,330,327,328,168,361,311,527,319,344,316,342,154,360,325,506,295,336,328,22084,272,176,539,320,303,335,335,158,349,343,673,167,160,338,159,315,176,335,334,506,345,295,305,1065,313,1009,330,309,182,353,307,485,340,310,181,174,323,185,342,326,727,166,162,286,162,312,148,341,331,488,338,337,344,2706,136,156,166,367,345,472,185,342,306,183,314,166,344,318,695,176,160,174,167,167,479,173,163,173,161,168,309,166,373,345,526,807,167,321,154,308,161,168,152,295,171,565,344,334,159,355,301,186,325,163,345,318,1181,172,180,323,159,466,331,349,173,324,318,3208,322,345,299,313,367,295,380,0,315,310,363,332,552,472,322,1017,320,321,332,351,312,331,187,527,327,468,503,360,317,178,347,325,811,329,344,495,527,325,336,166,331,458,1059,169,169,468,499,315,310,169,371,341,1834,310,338,353,292,318,364,1368,303,468,521,354,1035,323,332,316,310,354,318,175,1200,311,365,309,315,159,342,307,512,325,328,350,358,160,333,311,552,347,303,324,289,177,359,369,481,321,334,309,2647,21749,331,328,331,308,312,305,721,333,322,331,320,304,359,708,337,311,327,332,313,339,691,324,311,348,334,320,332,693,339,301,332,304,318,365,728,352,339,319,307,316,355,661,314,323,342,345,323,348,698,339,308,343,298,342,287,403,340,323,330,326,335,304,337,1382,299,495,518,325,1051,271,314,335,337,320,322,160,543,314,481,541,345,308,168,354,348,499,323,317,650,351,338,363,307,171,348,465,1057,160,176,464,494,356,318,155,321,490,1700,330,312,341,310,345,310,1422,314,515,468,317,670,330,315,316,372,294,385,335,169,1223,294,304,329,335,157,345,303,537,322,342,300,347,168,364,286,568,307,330,320,311,167,348,322,528,346,320,308,991,321,551,497]
# print(len(lis))
# nl = []
# for i in range(len(lis)):
    

#     if(False):

#         pass


#     else:
#         nl.append(int(lis[i] / 50 * 6) + randint(0,2 ) )
# print(nl)

lis = [308,41,21,66,37,39,39,138,19,87,21,21,36,20,42,19,44,38,60,42,41,42,123,20,154,38,38,24,46,41,61,36,40,43,131,20,85,22,22,37,21,41,19,44,40,63,43,41,39,419,37,18,64,44,42,42,45,21,44,38,84,24,20,42,21,43,20,43,38,64,38,41,40,134,19,148,39,39,23,44,38,62,40,39,41,41,23,47,41,83,20,24,41,21,37,20,44,42,66,40,37,42,336,23,15,21,43,40,64,23,44,19,20,21,43,20,41,43,89,19,20,18,21,21,61,22,21,19,21,22,42,20,22,19,43,58,110,22,41,18,47,19,20,22,37,22,66,41,38,21,40,40,66,21,43,43,146,41,38,23,39,44,21,41,20,43,40,395,42,41,43,41,43,39,48,0,41,41,40,44,59,66,44,0,38,41,42,43,41,39,42,41,42,22,63,43,65,53,45,42,21,43,42,107,38,44,61,61,44,42,22,40,56,135,23,19,61,60,38,43,24,45,60,207,41,44,38,41,40,38,172,40,64,59,42,134,40,40,38,42,44,41,22,147,39,42,42,43,21,41,40,61,39,39,42,43,27,46,40,65,41,41,40,43,22,38,40,63,42,35,41,2763,41,19,61,39,41,39,41,19,45,43,82,22,21,43,22,41,20,43,42,59,39,43,38,136,38,126,40,42,22,42,40,65,39,39,21,20,42,19,42,45,85,21,18,44,20,41,22,41,39,63,42,41,40,87,83,85,77,19,19,21,46,45,65,22,44,38,22,41,22,39,41,82,21,21,20,21,22,70,20,21,20,22,21,40,22,38,40,63,105,24,42,21,38,21,20,19,42,20,20,42,40,45,20,20,25,42,20,40,22,44,41,141,19,23,46,22,60,40,43,22,42,38,398,0,42,39,42,39,43,43,44,0,42,38,42,37,73,59,41,132,38,42,38,37,43,44,23,64,39,62,61,43,42,22,43,42,101,44,41,63,67,39,42,21,42,53,133,21,19,60,62,44,40,22,43,41,234,35,40,43,40,40,43,169,42,62,68,39,125,40,40,39,42,49,43,20,147,40,41,41,42,19,45,41,64,43,38,42,40,22,40,40,63,40,41,47,40,22,40,40,61,45,44,39,333,2715,40,37,43,43,42,40,84,43,40,42,38,40,43,91,40,38,44,40,42,43,88,40,40,39,40,39,42,86,39,41,43,40,41,45,87,40,42,44,41,39,45,82,40,41,42,43,40,44,87,40,41,40,42,39,41,43,43,40,43,44,42,36,44,169,39,66,59,38,133,41,41,43,37,43,43,20,61,42,65,55,43,44,21,45,41,63,37,42,82,41,43,42,42,23,40,62,138,20,18,55,63,39,43,22,43,57,217,37,41,41,38,43,43,169,41,67,62,39,79,43,43,39,44,40,41,45,19,153,41,41,39,40,20,41,41,66,39,42,39,43,20,40,41,70,42,41,39,46,17,43,46,69,34,38,40,131,41,63,64],
j = []
for i in range(len(lis)):
    j.append(int(lis[i]) - 1)

print(j)



