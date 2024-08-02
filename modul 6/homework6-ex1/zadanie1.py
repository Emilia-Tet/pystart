def group_them(**kwargs):
    output_list=[]
    for arg in kwargs:
        output_list.append(f"{arg.title()} is {kwargs[arg]}")
    return '\n'.join(output_list)
    # for key, value in kwargs.items()

# group_them(python='super')