def max_sub_array_sum(arr):
	max_so_far = arr[0]
	curr_max = arr[0]

	for i in range(1, len(arr)):
		curr_max = max(arr[i], curr_max + arr[i])
		max_so_far = max(max_so_far, curr_max)

	return max_so_far


def main():
	lst = []
	n = int(input("Enter number of elements : "))

	for i in range(0,n):
		elem = int(input())
		lst.append(elem)

	print("Abhay Onkar")
	print(max_sub_array_sum(lst))

if __name__ == "__main__":
	main()
