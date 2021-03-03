import pytest
def NumIsPerf(n):
	sum=0
	for i in range(1, n//2+1):
		if n%i==0:
			sum+=i
			print(sum)
	return (sum==n)
@pytest.mark.parametrize("test_input,expected", [(6, True), (10, False), (28, True)])
def test1(test_input,expected):
	assert NumIsPerf(test_input) == expected
def test2():
	f = (lambda x: (x**2+3*x-1)/(x+1))
	try:
		assert f(-1)
	except:
		print("Error")
def test3():
	nums = [x for x in range(10)]
	assert (5 in nums)
def test4():
	dictionary = {"Tolkien":0,"Book":1,"Tomato":2}
	assert ("Tolkien" in dictionary.keys())
def test5():
	char = 'a'
	words = [char*i for i in range(1,10)]
	assert (all([len(words[x])==x+1 for x in range (4,7)]))
def test6():
	names = {'Joe', 'Sam', 'Ann', 'Mike', 'Lucy'}
	guests = {'Joe', 'Sam', 'Mike'}
	assert (all (nm in names for nm in guests))