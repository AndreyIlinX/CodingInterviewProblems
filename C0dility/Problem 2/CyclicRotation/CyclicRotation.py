def solution(A, K):
    if K == 0 or A == []:
        return A
    N = len(A)
    K_actual = K % N
    for i in range(K_actual):
        last_element = A.pop()
        A.insert(0, last_element)
    return A

def solution_alternative(A, K):
    if K == 0 or A == []:
        return A
    A_copy = A.copy()
    N = len(A)
    K_actual = K % N
    for i in range(N):
        A[i] = A_copy[i - K_actual]
    return A




def main():
    print(solution([3, 8, 9, 7, 6], 3))


if __name__ == '__main__':
    main()
