
import csv


def read_in_data(file_name):
    with open(file_name, newline='', encoding='utf8') as f:
        r = csv.reader(f, delimiter=',') 
        csv_data = []

        for row in r:
            csv_data.extend(map(int, row))  
    return csv_data


def generate_faces_sum_and_min(data):
    faces_sums = []
    smallest_faces = []
    for row in data:
        l, w, h = map(int, row.split('x'))
        faces = [l*w, w*h, l*h]

        faces_sums.append(sum(faces))
        smallest_faces.append(min(faces))
    
    return faces_sums, smallest_faces

def total_wrapping_paper():
    pass