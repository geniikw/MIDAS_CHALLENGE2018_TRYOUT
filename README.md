# 마이다스 챌린지 2018 예선문제

이 페이지에서는 문제를 풀수 있는 최소한의 부분을 기억에 의존해서 제공합니다.

답안지는 각 파이선 파일(pX.py)로 제공합니다만 오답일 수도 있습니다.


제한시간 4시간 사용언어는 C,C++,JAVA,Python 중 택1 


## 1 패스워드,아이디 조건검출 문제
조건에 맞는 ID와 PW를 검출하는 문제이다. 조건은 다음과 같다.
```
id는 6에서 12자리 pw는 8에서 16 자리여야 한다.

연속된 자리가 3개가 있으면 안된다 (ex, abc)

숫자랑 알파벳 하나씩은 무조건 있어야 한다.
```
처음 입력으로 id를 두번째 입력으로 pw를 줌.

모든조건을 만족할 경우 T 아니면 F를 내보낸다.

## 2 이메일자동 생성기
처음 입력으로 Company이름을 주고 다음 입력으로 콤마(,)로 구분된 이름을 준다.

이름은 FirstName, MiddleName, LastName으로 구성되고 라스트네임에는 하이픈("-")이 있을 수 있다.

이메일은 다음과 같이 구성된다.

```
FirstName의첫글자 + LastName + "@" + Company + ".com"
```

입력은 대문자일 수도 있지만 이메일은 모두 소문자로 출력해야 한고 하이픈은 지워야 한다.

# 3 길찾기문제
처음 입력은 엣지의 수, 

그다음 엣지의 수만큼 엣지에 관한 정보를 준다.(노드 2개) 

그리고 마지막으로 목적지 정보를 준다. (노드 1개)

그래프는 무조건 A부터 시작하며 Z에서 끝날 때 목적지를 경유한 최단루트를 구해라

입력값이
```
5
A,B
B,C
C,D
D,Z
D,E
E,Z
D
```
A->B->C->D->Z

A->B->C->D->E->Z

둘다 D를 지남으로 최단루트는 5



# 4 가장 짧은 키를 찾아라
N과 X 두가지 Int값을 입력으로 준다.

N의 범위는 100에서 99999999

X는 8에서 128


입력받은 두 수를 이진수로 변환하고 X랑 일치하는 N의 부분집합을 지우는 것을 반복할 수 있을 때
가장 작은 결과 값을 구하라.

```
예 )
N => 438 => 110110110

X => 13 => 1101


일때 앞에껄 지운경우[1101]10110 -> 10110 길이는 5

중간껄 지운 경우 110[1101]10 -> [1101]0 -> 0 길이는 1

따라서 1을 리턴한다.
```

# 5 삼항연산자 구현
괄호가 없는 삼항연산자가 많이 중첩된 식을(ex 1 == 1 ? 2 : 3 )을 입력값으로 준다. 결과값을 구하라 오류가 있을 시 -1을 리턴
비교문은 "!=", "==", ">", "<", ">=", "<="를 구현해야 하고 각 토큰은 공백으로 구분되어 있다.

[1 == 2 =! 3 > 4 <= 5 >= 6 ? 7 : 8 ? 9 : 10 ? 11 : 12] 뭐 이런 식을 줬던거 같다. 정확한 기억은 안난다.

# 6 구역크기 계산
가로세로가 10인 지역이 있다. 여러개의 입력값 두좌표로 지정할 수 있는 네모를 전부 그릴 때
가장 큰(작은?) 폐쇄 지역의 크기를 구하라

처음 입력은 네모의 수

그다음 네모의 수 만큼 좌표를  입력 받는다.
입력이
```
2,3,6,9
4,2,9,8
```
이라면 
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 2, 2, 2, 2, 2, 2, 0]
[0, 2, 2, 2, 2, 2, 0, 0, 2, 0]
[0, 2, 0, 2, 0, 2, 0, 0, 2, 0]
[0, 2, 0, 2, 0, 2, 0, 0, 2, 0]
[0, 2, 0, 2, 0, 2, 0, 0, 2, 0]
[0, 2, 0, 2, 0, 2, 0, 0, 2, 0]
[0, 2, 0, 2, 2, 2, 2, 2, 2, 0]
[0, 2, 2, 2, 2, 2, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
이렇게 그릴 수 있고 가장 큰 구역은 10 작은 구역은 4가 된다.

## 감상
잘 써보지도 않은 파이썬으로 문제를 푼 업보일까. 6번 문제는 시간이 없어서 못 풀었다.
워낙 문법에 막혀서 테스트케이스를 만들어서 풀 틈이 없었고 그냥 예시로 나온 케이스만
통과하면 패스했기때문에 정답이 아닐 수도 있음


유니티로 C#만 주로 하는 관계로 새로 언어를 배워야 했다. C++,C는 STL관련 지식을 전부 잃은 관계로
사용 불가능 했고 JAVA는 사용해보질 않았다. 뭐, C#이랑 제일 비슷해서 사용할까 하다가 
그냥 파이썬이 제일 쉬워 보여서 파이썬으로 했다. 하루전날밤(...) 파이썬으로 hackerrank에서 놀다가
1시간정도 자고 시험을 봤다. 

전체적인 난이도는 쉬운편으로 시간복잡도같은 복잡한 생각이 필요없고 그냥 문제가 원하는걸 구현하기만
하면 된다. 문법에 애먹은 1번2번은 각각 한시간씩걸렸고 이후로는 익숙해져서 금방 풀렸던거 같다.
~근데 1번은 길이체크실수로 틀림~
