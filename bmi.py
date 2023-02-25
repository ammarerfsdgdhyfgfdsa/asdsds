# A simple script to calculate BMI
from pywebio.input import input, FLOAT
from pywebio.output import put_text
import argparse
import gunicorn
from pywebio import start_server

def bmi():
    server=bmi.server
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-p","--port",type=int, default=8080)
   # args=parser.parse_args()

    #start_server(app, port=args.port)
    #app.run(host='localhost',port=80)
    bmi()
