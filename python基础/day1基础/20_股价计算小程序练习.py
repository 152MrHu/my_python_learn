# 20_股价计算小程序练习.py
# 自动生成的Python文件
name = "黑马程序员"
stock_price = 6.5
stock_code = "002564"
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}元")
print("每日增长系数:%.1f,经过%d天增长后,股价达到了:%.2f" %
      (stock_price_daily_growth_factor,
       growth_days,
       stock_price * (stock_price_daily_growth_factor ** growth_days)))