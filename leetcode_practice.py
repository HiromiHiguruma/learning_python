def twoSum(nums, target):


    index_dicc = dict()



    for index, numero in enumerate(nums):

        if target - numero not in index_dicc:

            index_dicc [numero] = index

    for numero in range (0, len(nums)):

        resultado = target - nums[numero]

        if resultado in index_dicc and numero != index_dicc [resultado]:

            return [numero, index_dicc[resultado]]








Lista_de_nums = [0,2,5]



Objetivo = 7

print(twoSum (Lista_de_nums, Objetivo))

