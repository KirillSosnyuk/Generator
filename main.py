from functools import wraps
from datetime import datetime

def logger(path: str='logs/file.log'):

    def logging_func(function):

        @wraps(function)
        def save_info(*args, **kwargs):

            with open(path, 'a', encoding='utf-8') as log_file:
                result = function(*args, **kwargs)
                log_file.write(f'Fuction {function.__name__}\nstarted at {datetime.now()}\nwith arguements {args, kwargs}\nand returned result: {result}\n\n')
            
            return result
    
        return save_info
    
    return logging_func


@logger()
def func_from_previous_hometask(mylist: list):
    new_list = []
    while any(filter(lambda x: type(x) == list, mylist)):
        for item in mylist:
            if isinstance(item, list):
                new_list.extend(item)
            else:
                new_list.append(item)

        mylist = new_list[:]
        new_list.clear()

    return mylist



nested_list = [
    {1, 2, 3, 3}, 
    {'a': 1, 'b': 2},
    ['a', 'b'],
	['a', 'b', [1, ['I love Python', 'hey', 0, -4], 2], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    print(func_from_previous_hometask(nested_list))