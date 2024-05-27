class func:
    '''   一些实验定义的函数   '''

    def func1(turple1):
        '''   返回元组的第二个元素   '''
    
        _,a=turple1
        return a

    def func2(turple2):
        '''   判断元组第二个元素是否大于95   '''

        _,b=turple2
        return b > 95
    
    def func3(turple3):
        '''   返回元组第一个元素的小写字符串   '''

        c,_=turple3
        return c.lower()

if __name__ == '__main__':
    pp = [('Leborn James', 98), ('Kevin Durant', 97),
        ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]
    
    print(list(map(func.func3,pp)))
    print(list(sorted(pp,key=func.func1)))
    print(list(filter(func.func2,pp)))
