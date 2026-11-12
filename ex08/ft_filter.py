def ft_filter(function, iterable):
    """\
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        function = bool
    for item in iterable:
        if function(item):
            yield item


# def main():
#     my_list = [False, "Hello", True, 0, 3]
#     for item in ft_filter(None, my_list):
#         print(item)
#     for item in filter(None, my_list):
#         print(item)

# main()
