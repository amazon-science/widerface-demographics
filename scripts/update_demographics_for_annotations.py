"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
Licensed under the CC-BY-NC 4.0 license.
"""
import pandas as pd

def read_original_annotations(annotation_file):
	"""
	Read the original annotation file and create a mapping dict between person and values
	"""
	annotations = open(annotation_file).readlines()
	mappings = {}
	current_id = ""
	current_user = 0
	num_users = 0
	for line in annotations:
		if "jpg" in line:
			current_id = line.rstrip()
			continue
		if num_users == 0:
			num_users = int(line.rstrip())
			current_user = 0
			continue
		key = f"{current_id}_{current_user}"
		mappings[key] = line.rstrip()
		num_users -= 1
		current_user += 1
	return mappings

def extract_column_values(mapping, df_keys, df):
	"""
	Read
	"""
	additional_columns = ["x_min", "y_min", "width", "height", "blur", "expression", "illumination", "invalid",
						  "occlusion", "pose"]
	column_values = {x:[] for x in additional_columns}
	for key in df_keys:
		values = mapping[key].split(" ")
		for index, column in enumerate(additional_columns):
			column_values[column].append(values[index])

	for index, column in enumerate(additional_columns):
		df[column] = column_values[column]
	return df


def add_demographic_annotations(demographic_file, annotation_file, output_file):
	df = pd.read_csv(demographic_file)
	df_keys = []
	for i in range(len(df)):
		key = f"{df.loc[i]['file'].replace('images/', '')}_{df.loc[i]['face']}"
		df_keys.append(key)

	mappings = read_original_annotations(annotation_file)
	df = extract_column_values(mappings, df_keys, df)
	df = df[df.columns.tolist()[1:]]
	df.to_csv(output_file)

def main():
	demographic_file = "../annotations/demographics_val.csv"
	annotation_file = "../annotations/wider_face_val_bbx_gt.txt"
	output_file = "../annotations/demographics_val_merged.csv"

	demographic_file = "../annotations/demographics_train.csv"
	annotation_file = "../annotations/wider_face_train_bbx_gt.txt"
	output_file = "../annotations/demographics_train_merged.csv"
	add_demographic_annotations(demographic_file, annotation_file, output_file)

if __name__ == "__main__":
    main()
