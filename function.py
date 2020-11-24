names = ["boney", ["gdl", ["mexico", "india"]], "diana", "carlos", ["sonora"],
         'alfredo', 'vanessa', 'lupe', "bevin", ["berlin", "dubai"]]
print(names)


def function_loop():
    for each_item in names:
        if isinstance(each_item, list):
            for nested_item in each_item:
                if isinstance(nested_item, list):
                    for deeper_item in nested_item:
                        print(deeper_item)
                else:
                    print(nested_item)
        else:
            print(each_item)


function_loop()