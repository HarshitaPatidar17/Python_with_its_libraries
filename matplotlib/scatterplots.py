import matplotlib.pyplot as plt
hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,60,65,70,75,80,85]
plt.scatter(hours_studies,exam_scores,color='green',marker='o',label='Student Data')
plt.xlabel("hour_stidies")
plt.ylabel("exam_scores")
plt.title("shape between study time and exam score")
plt.legend()
plt.grid(True)
plt.show()