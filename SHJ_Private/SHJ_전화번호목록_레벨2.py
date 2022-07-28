def solution(phone_book):
    answer = False
    length = set()
    for p in phone_book:
        length.add(len(p))

    for leng in length:
        d = dict()

        for pb in phone_book:
            # 예외 처리.
            if pb[0:leng] in d and (len(pb) == leng or leng == d[pb[0:leng]]):
                return False
            else:
                d[pb[0:leng]] = len(pb)

    return True


# 반례
pb = ["119", "123223123", "112", "123", "1231231234"]
solution(pb)