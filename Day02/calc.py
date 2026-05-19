m_something = 'hai'

m_name = __name__

def find_sum(num1, num2):
    result = num1 + num2
    return result

def find_diff(num1, num2):
    result = num1 - num2
    return result

if __name__ == "__main__":
    print(find_sum(4,6))
    print(find_diff(7,2))
    print(m_name)

