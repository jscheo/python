import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 한글깨짐 방지
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False
        # x축              y축
# plt.plot([1, 2, 3, 4], [3, 6, 10, 12])
x_values = [1, 2, 3, 4]
y_values = [3, 6, 10, 12]
# 연결되는 부분 마킹할 때 o 써주고 선이랑 이어줄려면 - /--두개면 점선
plt.plot(x_values, y_values, "o--")
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.show()