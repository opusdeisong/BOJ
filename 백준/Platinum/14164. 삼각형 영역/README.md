# [Platinum I] 삼각형 영역 - 14164 

[문제 링크](https://www.acmicpc.net/problem/14164) 

### 성능 요약

메모리: 112140 KB, 시간: 580 ms

### 분류

기하학

### 제출 일자

2024년 2월 13일 22:15:37

### 문제 설명

<p>농부 존은 현금을 마련하기 위해 자신의 땅을 팔려고 한다. 그는 2차원 좌표평면에서 점으로 나타낼 수 있는 나무 N(3 ≤ N ≤ 300)개가 있는데, 세 점이 일직선 상에 있지 않는 꼴로 나무가 배치되어 있다. 농부 존은 서로 다른 세 나무를 꼭짓점으로 하는 삼각형 영역을 후보 삼아 파는 것을 고려하려고 한다. 즉, 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mrow><mjx-texatom texclass="OPEN"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c28 TEX-S1"></mjx-c></mjx-mo></mjx-texatom><mjx-mfrac><mjx-frac atop="true" delims="true" style="vertical-align: -0.345em;"><mjx-num style="padding-bottom: 0.319em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-num><mjx-den><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-texatom></mjx-den></mjx-frac></mjx-mfrac><mjx-texatom texclass="CLOSE"><mjx-mo class="mjx-sop"><mjx-c class="mjx-c29 TEX-S1"></mjx-c></mjx-mo></mjx-texatom></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="OPEN"><mo minsize="1.2em" maxsize="1.2em">(</mo></mrow><mfrac linethickness="0"><mrow data-mjx-texclass="ORD"><mi>N</mi></mrow><mrow data-mjx-texclass="ORD"><mn>3</mn></mrow></mfrac><mrow data-mjx-texclass="CLOSE"><mo minsize="1.2em" maxsize="1.2em">)</mo></mrow></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\({N}\choose{3}\)</span></mjx-container>개의 후보가 존재한다.</p>

<p>삼각형 영역은 세 꼭짓점을 제외한 영역 안에 존재하는 나무의 개수 v에 따라 값이 매겨진다. 세 점이 일직선 상 위에 존재하지 않으므로, 삼각형 영역의 선분 위에 나무가 존재하는 경우가 없음이 자명하다. 0이상 N-3이하의 모든 v에 대해 나무의 개수가 v인 삼각형 영역의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄에 나무의 개수를 나타내는 자연수 N이 주어진다.</p>

<p>그 다음 N개의 줄에 각 나무의 x, y좌표를 나타내는 두 정수가 공백으로 구분되어 주어진다. 주어지는 좌표값은 0이상 1,000,000이하다.</p>

### 출력 

 <p>N-2개의 줄에 걸쳐, i번째 줄에는 v=i-1인 삼각형 영역의 수를 출력한다.</p>

