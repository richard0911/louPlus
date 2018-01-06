import matplotlib.pyplot as plt
import pandas as pd
import json


def show_pic():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	ax.set_title('StudyData')

	with open('user_study.json') as file:
		data = json.loads(file.read())

	df = pd.DataFrame(data)
	sf = df[['user_id', 'minutes']].groupby('user_id').sum()

	user_id = list(sf.index)
	minutes = list(sf['minutes'])

	ax.plot(user_id, minutes)


if __name__ == '__main__':
	show_pic()