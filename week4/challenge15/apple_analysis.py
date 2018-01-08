import pandas as pd


def quarter_volume():
	data = pd.read_csv('apple.csv', header=0)

	df = pd.DataFrame(data=data['Volume'].values,
					  index=pd.to_datetime(data['Date'].values),
					  columns=['Volume'])

	gf = df.resample('3M').sum()
	volume_list =list(gf['Volume'].values)
	volume_list.sort(reverse=True)
	second_volume = volume_list[1]
	return second_volume

if __name__ == '__main__':
	quarter_volume()