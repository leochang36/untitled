Money=float(input('请输入销售数额：'))
Cost=float(input('请输入成本：'))
if (Money>Cost):
    print ('盈利！ 盈利金额为：',Money-Cost)
elif (Money==Cost):
    print ('保本！')
else:
    print ('亏损！ 亏损金额为：',Cost-Money)


