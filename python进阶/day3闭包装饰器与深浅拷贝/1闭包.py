# 闭包可以保存
# 使用外部函数变量的内部函数是闭包
# 有嵌套  有引用   有返回


def get_sum(a,b):
    return a+b

print (get_sum) #<function get_sum at 0x0000020E0EB7EA60>
print (get_sum(1,2))

# 函数名赋值给变量----函数对象
get_sum_1 = get_sum
print (get_sum_1)


print("-"*35)

def fn_outer(num1):
    def fn_inner(num2):
        sum =  num1 + num2
        print("结果",sum)
    return fn_inner

fn_inner = fn_outer(10)
fn_inner(20)

print("-"*35)

fn_outer(10)(20)
