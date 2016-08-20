print "How old are you?",

# 读取控制台的输入与用户实现交互,直接读取控制台的输入，任何类型的输入都可接受，返回字符串类型
age = raw_input()

print "How tall are you"

height = raw_input()

print "How much do you weight?",

weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
