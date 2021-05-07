
def get_change(m):

  n, m =m//10, m% 10
  p , m = m//5, m%5
  return m+n+p

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
